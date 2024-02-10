import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.protobuf import service
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1j2aWRBBqD1WZRQs5BYdEuEIf27r-dB6ojgJL1xHoQtE"
API_KEY = "AIzaSyAMIz6KxsyusnXcgpXInBoVzEESIIWfv3E"


def calculate_final_score():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build('sheets', 'v4', credentials=credentials)
        sheets = service.spreadsheets()
        table = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range="A4:A").execute()
        table_value = table.get("values", [])
        size = len(table_value)
        total_lessons_string = \
            sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="engenharia_de_software!A2:H2").execute().get(
                "values")[
                0][0]
        total_lessons_number = total_lessons_string.split(":")
        i = 4

        for row in range(4, size):
            if i <= (size):
                student1 = sheets.values().get(spreadsheetId=SPREADSHEET_ID,range="engenharia_de_software!A4:H").execute().get("values", [])
                score_average = (int(student1[i-4][3]) + int(student1[i-4][4]) + int(student1[i-4][5])) / 3
                if score_average >= 50:
                    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"engenharia_de_software!G{row}",valueInputOption="USER_ENTERED",body={"values": [["reprovado teste"]]}).execute()

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    calculate_final_score()
