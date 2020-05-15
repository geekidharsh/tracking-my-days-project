from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import pprint

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a spreadsheet.
SPREADSHEET_ID = '1hCFu3Ux-eLlQnVaGa6ZNmOPS0QWD12r_6NQU0mH1dfU'
ranges = 'Mood'
include_grid_data = True
def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    request = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=ranges, includeGridData=include_grid_data)
    response = request.execute()
    keys = [key for key, val in response.items()]
    print(keys)
    sheet_val = response['sheets']
    pp = pprint.PrettyPrinter()

    for i in sheet_val:
        if type(i) == dict:
            for k, v in i.items():
                if k == 'data':
                    pp.pprint(v)




if __name__ == '__main__':
    main()