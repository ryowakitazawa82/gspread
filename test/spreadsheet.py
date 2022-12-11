from datetime import date
from turtle import color

import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import *

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# シートを取得
sheets = client.open("Legislators")
# 必要な情報を取得・定義
index = 1
args = sys.argv[1]
initialPosition = 3
data_fmt = cellFormat(
    backgroundColor=color(1, 0.9, 0.7)
)
data_fmt_white = cellFormat(
    backgroundColor=color(1, 1, 1)
)


def create_template(sheet):
    for i in range(int(args)):
        sheet.insert_row([""], initialPosition + i)
        if i != 0:
            format_cell_range(sheet, '{0}:{0}'.format(initialPosition + i), data_fmt_white)
    sheet.update_cell(initialPosition, 2, '{0:%Y/%m/%d}'.format(date.today()))
    format_cell_range(sheet, '3:3', data_fmt)


create_template(sheets.get_worksheet(0))
create_template(sheets.get_worksheet(1))
