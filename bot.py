#!/usr/bin/env python3
"""
Beeline Multilingual Test Bot
Диалог → Опрос → Google Sheets
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from content import (
    DIALOGUES,
    LANG_BUTTONS,
    LANG_INTRO,
    SCENARIO_BUTTONS,
    SCENARIO_QUESTION,
    SURVEY,
)
from sheets import save_response

# ─────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]

# ─────────────────────────────────────────────
# FSM STATES
# ─────────────────────────────────────────────
class S(StatesGroup):
    lang_select     = State()
    scenario_select = State()
    in_dialogue     = State()
    survey_q1       = State()
    survey_q2       = State()
    survey_q3       = State()
    survey_q4       = State()
    survey_q5       = State()


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def make_kb(buttons: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    """Создать inline-клавиатуру из списка (label, callback_data)."""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=t, callback_data=d)] for t, d in buttons]
    )


async def send_node(bot: Bot, chat_id: int, node: dict) -> None:
    """Отправить все сообщения узла диалога."""
    texts = node.get("text", [])
    if isinstance(texts, str):
        texts = [texts]
    for text in texts:
        if text:
            await bot.send_message(chat_id, text)

    question = node.get("question")
    buttons  = node.get("buttons", [])

    if question and buttons:
        await bot.send_message(chat_id, question, reply_markup=make_kb(buttons))
    elif question:
        await bot.send_message(chat_id, question)
    elif buttons:
        await bot.send_message(chat_id, "👇", reply_markup=make_kb(buttons))


# ─────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────

async def cmd_start(message: Message, state: FSMContext) -> None:
    """
    Поддерживает deep-links:
      /start           → выбор языка
      /start imei      → выбор языка, потом IMEI
      /start ebs       → выбор языка, потом EBS
      /start imei_uz   → сразу IMEI на узбекском
    """
    await state.clear()
    args = message.text.split(maxsplit=1)[1] if " " in message.text else ""

    lang, scenario = None, None
    if "_" in args:
        parts = args.split("_", 1)
        scenario, lang = parts[0], parts[1]
    elif args in ("imei", "ebs"):
        scenario = args

    if lang and scenario:
        # Полный deep-link → сразу в диалог
        await state.update_data(lang=lang, scenario=scenario, node="start", path=[])
        await state.set_state(S.in_dialogue)
        node = DIALOGUES[lang][scenario]["start"]
        await send_node(message.bot, message.chat.id, node)
    elif scenario:
        # Только сценарий → сначала выбор языка
        await state.update_data(preset_scenario=scenario)
        await state.set_state(S.lang_select)
        await message.answer(LANG_INTRO, reply_markup=make_kb(LANG_BUTTONS))
    else:
        # Обычный старт
        await state.set_state(S.lang_select)
        await message.answer(LANG_INTRO, reply_markup=make_kb(LANG_BUTTONS))


# ─────────────────────────────────────────────
# ВЫБОР ЯЗЫКА
# ─────────────────────────────────────────────

async def cb_lang(callback: CallbackQuery, state: FSMContext) -> None:
    lang = callback.data
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)

    data = await state.get_data()
    preset_scenario = data.get("preset_scenario")

    await state.update_data(lang=lang, path=[])

    if preset_scenario:
        # Сценарий уже задан через deep-link — сразу стартуем
        await state.update_data(scenario=preset_scenario, node="start")
        await state.set_state(S.in_dialogue)
        node = DIALOGUES[lang][preset_scenario]["start"]
        await send_node(callback.bot, callback.message.chat.id, node)
    else:
        await state.set_state(S.scenario_select)
        q = SCENARIO_QUESTION[lang]
        kb = make_kb(SCENARIO_BUTTONS[lang])
        await callback.message.answer(q, reply_markup=kb)


# ─────────────────────────────────────────────
# ВЫБОР СЦЕНАРИЯ
# ─────────────────────────────────────────────

async def cb_scenario(callback: CallbackQuery, state: FSMContext) -> None:
    scenario = callback.data
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)

    data = await state.get_data()
    lang = data["lang"]

    await state.update_data(scenario=scenario, node="start")
    await state.set_state(S.in_dialogue)

    node = DIALOGUES[lang][scenario]["start"]
    await send_node(callback.bot, callback.message.chat.id, node)


# ─────────────────────────────────────────────
# ДИАЛОГ — переходы по узлам
# ─────────────────────────────────────────────

async def cb_dialogue(callback: CallbackQuery, state: FSMContext) -> None:
    next_node_id = callback.data
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)

    data     = await state.get_data()
    lang     = data["lang"]
    scenario = data["scenario"]
    path     = data.get("path", [])

    path.append(next_node_id)
    await state.update_data(node=next_node_id, path=path)

    node = DIALOGUES[lang][scenario].get(next_node_id)
    if not node:
        logger.error(f"Node not found: {lang}/{scenario}/{next_node_id}")
        return

    await send_node(callback.bot, callback.message.chat.id, node)

    if node.get("is_end"):
        # Конец диалога → запускаем опрос
        await asyncio.sleep(1)
        survey = SURVEY[lang]
        await callback.bot.send_message(
            callback.message.chat.id,
            survey["intro"],
            parse_mode="Markdown",
        )
        await asyncio.sleep(0.5)
        await callback.bot.send_message(
            callback.message.chat.id,
            survey["q1"],
            reply_markup=make_kb(survey["q1_btn"]),
            parse_mode="Markdown",
        )
        await state.set_state(S.survey_q1)


# ─────────────────────────────────────────────
# ОПРОС — Q1 (Понятность 1-5)
# ─────────────────────────────────────────────

async def cb_survey_q1(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(sq1=callback.data)

    data   = await state.get_data()
    lang   = data["lang"]
    survey = SURVEY[lang]

    await callback.bot.send_message(
        callback.message.chat.id,
        survey["q2"],
        reply_markup=make_kb(survey["q2_btn"]),
        parse_mode="Markdown",
    )
    await state.set_state(S.survey_q2)


# ─────────────────────────────────────────────
# Q2 (Естественность)
# ─────────────────────────────────────────────

async def cb_survey_q2(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(sq2=callback.data)

    data   = await state.get_data()
    survey = SURVEY[data["lang"]]

    await callback.bot.send_message(
        callback.message.chat.id,
        survey["q3"],
        reply_markup=make_kb(survey["q3_btn"]),
        parse_mode="Markdown",
    )
    await state.set_state(S.survey_q3)


# ─────────────────────────────────────────────
# Q3 (Понял ли)
# ─────────────────────────────────────────────

async def cb_survey_q3(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(sq3=callback.data)

    data   = await state.get_data()
    survey = SURVEY[data["lang"]]

    await callback.bot.send_message(
        callback.message.chat.id,
        survey["q4"],
        parse_mode="Markdown",
    )
    await state.set_state(S.survey_q4)


# ─────────────────────────────────────────────
# Q4 (Свободный комментарий — текстовый ввод)
# ─────────────────────────────────────────────

async def msg_survey_q4(message: Message, state: FSMContext) -> None:
    await state.update_data(sq4=message.text)

    data   = await state.get_data()
    survey = SURVEY[data["lang"]]

    await message.answer(
        survey["q5"],
        reply_markup=make_kb(survey["q5_btn"]),
        parse_mode="Markdown",
    )
    await state.set_state(S.survey_q5)


# ─────────────────────────────────────────────
# Q5 (Рекомендация) + сохранение
# ─────────────────────────────────────────────

async def cb_survey_q5(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(sq5=callback.data)

    data = await state.get_data()
    lang = data["lang"]

    # Собираем запись для Google Sheets
    record = {
        "lang":     lang,
        "scenario": data.get("scenario", ""),
        "path":     " → ".join(data.get("path", [])),
        "q1":       data.get("sq1", ""),
        "q2":       data.get("sq2", ""),
        "q3":       data.get("sq3", ""),
        "q4":       data.get("sq4", ""),
        "q5":       data.get("sq5", ""),
        "user_id":  str(callback.from_user.id),
    }

    try:
        await asyncio.get_event_loop().run_in_executor(None, save_response, record)
        logger.info(f"Saved response for user {callback.from_user.id}")
    except Exception as e:
        logger.error(f"Failed to save to Sheets: {e}")

    survey = SURVEY[lang]
    await callback.bot.send_message(callback.message.chat.id, survey["thanks"])
    await state.clear()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp  = Dispatcher(storage=MemoryStorage())

    # Регистрация handlers
    dp.message.register(cmd_start, CommandStart())
    dp.message.register(msg_survey_q4, S.survey_q4)

    # Callback handlers — важен порядок регистрации
    dp.callback_query.register(cb_lang,      S.lang_select)
    dp.callback_query.register(cb_scenario,  S.scenario_select)
    dp.callback_query.register(cb_dialogue,  S.in_dialogue)
    dp.callback_query.register(cb_survey_q1, S.survey_q1)
    dp.callback_query.register(cb_survey_q2, S.survey_q2)
    dp.callback_query.register(cb_survey_q3, S.survey_q3)
    dp.callback_query.register(cb_survey_q5, S.survey_q5)

    logger.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
