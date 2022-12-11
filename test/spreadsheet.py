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
# 必要な情報を取得
index = 1
# sheet.insert_row(row, index)
args = sys.argv[1]
initialPosition = 2
data_fmt = cellFormat(
    backgroundColor=color(1, 0.9, 0.7)
)


def main(sheet):
    for i in range(int(args)):
        sheet.insert_row([""], initialPosition + i)

    sheet.update_cell(initialPosition, 2, '{0:%Y/%m/%d}'.format(date.today()))
    format_cell_range(sheet, f'2:2', data_fmt)


main(sheets.get_worksheet(0))
main(sheets.get_worksheet(1))
