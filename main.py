import os
import math

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1j2aWRBBqD1WZRQs5BYdEuEIf27r-dB6ojgJL1xHoQtE'


def get_student_status(student: list[str], total_lessons: int) -> list[str]:
    abscences = int(student[2])
    abscence_rate = abscences / total_lessons
    abscent_reproval = abscence_rate > 0.25
    grade_1, grade_2, grade_3 = student[3:6]
    average_score = math.ceil((int(grade_1) + int(grade_2) + int(grade_3)) / 3)

    status = ''
    needed_grade = ''
    match average_score:
        case _ if abscent_reproval:
            status = 'Reprovado por Falta'
            needed_grade = '0'
        case _ if average_score >= 70:
            status = 'Aprovado'
            needed_grade = '0'
        case _ if 50 <= average_score < 70:
            final_score = 100 - average_score
            status = 'Exame Final'
            needed_grade = f'{final_score}'
        case _ if average_score < 50:
            status = 'Reprovado'
            needed_grade = '0'

    return [status, needed_grade]


def get_credentials():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file(
            'token.json', SCOPES
        )
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    return credentials


def update_table():
    credentials = get_credentials()
    try:
        service = build('sheets', 'v4', credentials=credentials)
        sheets = service.spreadsheets()
        table = (
            sheets.values()
            .get(spreadsheetId=SPREADSHEET_ID, range='A1:H')
            .execute()
        )
        students_list = table['values'][3:]
        total_lessons = int(table['values'][1][0].split(': ')[1])

        students_grades = list(
            map(
                lambda student: get_student_status(student, total_lessons),
                students_list,
            )
        )

        body = {'values': students_grades}

        sheets.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range='G4:H',
            valueInputOption='RAW',
            body=body,
        ).execute()

    except HttpError as error:
        print(error)


if __name__ == '__main__':
    update_table()
