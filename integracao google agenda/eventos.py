from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

print(creds)


def criaEvento(nomeEvento, data, id_calendario):
    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
          'summary': f'{nomeEvento}',
        #   'location': '800 Howard St., San Francisco, CA 94103',
        #   'description': 'A chance to hear more about Google\'s developer products.',
          "start": {
            "date": f"{data}"
          },
          "end": {
              "date": f"{data}"
            # "date": "2023-10-10"
          },
          "transparency": "transparent",
        #   'recurrence': [
        #     'RRULE:FREQ=DAILY;COUNT=2'
        #   ],
          # 'attendees': [
          #   {'email': 'email@gmail.com.br'},
          # ],
          'reminders': {
            'useDefault': False,
            'overrides': [
            #   {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10080},
            ],
          },
        }

        event = service.events().insert(calendarId=id_calendario, body=event).execute()
        print ('Event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print('An error occurred: %s' % error)

def buscaEvento(id_calendario):
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming events')
        events_result = service.events().list(calendarId=id_calendario, timeMin=now,
                                              maxResults=1000, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return
        
        return events


    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    idAgenda = 'primary'
    criaEvento('teste', '2023-10-10', idAgenda)
    buscaEvento(idAgenda)