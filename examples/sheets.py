"""Example of dealing with Google spreadsheets API"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main() -> list:
    """Returns data from Google sheet"""
    scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("examples/creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("people").sheet1
    data = sheet.get_all_records()

    return data


if __name__ == "__main__":
    print(main())
