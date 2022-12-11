from datetime import date

import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

def main():
    # 必要な情報を用意
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Legislators")
    sheet1 = sheet.sheet1
    # args = sys.argv[0]

    # シートを操作する
    row = ["", '{0:%Y/%m/%d}'.format(date.today())]
    index = 1
    sheet.insert_row(row, index)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
