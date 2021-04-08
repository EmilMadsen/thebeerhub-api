import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_sheets_data(spreadsheet_id,cell_range):
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Insert the name of the generated OAut2 .json file exported from the Sheets API
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_882546321084-mhrogt5i184i7c11qav25k0rbe53v4dg.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=cell_range).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        raise ValueError("No Sheets data found.")
    else:
        return pd.DataFrame(values_input[1:], columns=values_input[0])

#sheet_import = get_sheets_data('1XWo5ZkoweSnvKIlnR0X1tuKgKaq7UcQgQrDI0cA_KpQ','C1:G1000')

#print(sheet_import)

#sheet_import["Timepoint"] = pd.to_datetime(sheet_import["Timepoint"],format="%m/%d/%Y %H:%M:%S")