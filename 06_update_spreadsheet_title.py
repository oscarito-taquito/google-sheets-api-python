from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
import datetime as dt

current_dir = os.path.dirname(os.path.realpath(__file__))
key_file = os.path.join(current_dir, 'osk-demo-277900-e4f32ed9854e.json')

scopes = ['https://www.googleapis.com/auth/drive']

spreadsheet_id = '1FtopfMof8tEaB7h4DwMjr5MZAv9mff_TFMZJduZVv0M'

credentials = Credentials.from_service_account_file(key_file, scopes=scopes)

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

# variables
today = dt.datetime.today().strftime('%Y-%m-%d')
spreadsheet_title = 'Python Google Sheets ' + today 


request = sheet.batchUpdate(spreadsheetId=spreadsheet_id,
			body={
				"requests": [{
					"updateSpreadsheetProperties": {
						"properties": {
							"title": spreadsheet_title
						}, "fields": "title"
					}
				}]
			})

response = request.execute()
print(response)
