"""
sheets.py — сохранение ответов опроса в Google Sheets
"""

import json
import os
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

# Колонки в таблице (строка 1 = заголовки)
COLUMNS = [
    "Дата/время",
    "User ID",
    "Язык",
    "Сценарий",
    "Путь по диалогу",
    "Q1 Понятность (1-5)",
    "Q2 Естественность",
    "Q3 Понял ли",
    "Q4 Комментарий",
    "Q5 Рекомендует",
]

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def _get_sheet():
    """Подключиться к Google Sheets и вернуть первый лист."""
    creds_json  = os.environ["GOOGLE_CREDENTIALS_JSON"]
    sheet_id    = os.environ["SPREADSHEET_ID"]

    creds_dict  = json.loads(creds_json)
    credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    client      = gspread.authorize(credentials)

    spreadsheet = client.open_by_key(sheet_id)
    sheet       = spreadsheet.sheet1

    # Добавить заголовки если лист пустой
    if sheet.row_count == 0 or not sheet.row_values(1):
        sheet.append_row(COLUMNS)

    return sheet


def save_response(record: dict) -> None:
    """
    Сохранить одну строку ответов опроса.
    record = {lang, scenario, path, q1, q2, q3, q4, q5, user_id}
    """
    sheet = _get_sheet()

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        record.get("user_id", ""),
        record.get("lang", ""),
        record.get("scenario", ""),
        record.get("path", ""),
        record.get("q1", ""),
        record.get("q2", ""),
        record.get("q3", ""),
        record.get("q4", ""),
        record.get("q5", ""),
    ]

    sheet.append_row(row, value_input_option="RAW")
