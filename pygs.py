from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
import random
import pandas as pd

current_dir = os.path.dirname(os.path.realpath(__file__))
key_file = os.path.join(current_dir, 'osk-demo-277900-e4f32ed9854e.json')

scopes = ['https://www.googleapis.com/auth/drive']

spreadsheet_id = '1FtopfMof8tEaB7h4DwMjr5MZAv9mff_TFMZJduZVv0M'
credentials = Credentials.from_service_account_file(key_file, scopes=scopes)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()


class Pygs:
	def __init__(self, spreadsheet_id=spreadsheet_id, sheet=sheet):
		self.spreadsheet_id = spreadsheet_id
		self.sheet = sheet

	def list_sheet_names(self):
		spreadsheets = self.sheet.get(spreadsheetId=self.spreadsheet_id).execute()
		sheet_names = [s['properties']['title'] for s in spreadsheets['sheets']]
		sheet_ids = [s['properties']['sheetId'] for s in spreadsheets['sheets']]

		return sheet_names, sheet_ids

	def create_sheet(self, sheet_name, sheet_index=1):
		sheet_names = self.list_sheet_names()[0]
		i = random.randint(1, 100)
		if sheet_name in sheet_names:
			sheet_name = f'{sheet_name} ({i})'
		body = {
			"requests": [{
				"addSheet": {
					"properties": {
						"title": sheet_name,
						"index": sheet_index
					}
				}
			}]
		}

		response = self.sheet.batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
		return response

	def read_sheet(self, sheet_name=None, sheet_range=None):
		if sheet_range is None:
			worksheet_range = sheet_name
		else:
			worksheet_range = f'{sheet_name}!{sheet_range}'

		response = self.sheet.values().get(spreadsheetId=self.spreadsheet_id,
						range=worksheet_range).execute()

		values = response.get('values', [])

		return values

	def clear_sheet(self, sheet_name=None, sheet_range=None):
		if sheet_range is None:
			worksheet_range = sheet_name
		else:
			worksheet_range = f'{sheet_name}!{sheet_range}'
		response = self.sheet.values().clear(spreadsheetId=self.spreadsheet_id,
						range=worksheet_range,
						body={}).execute()

		return response

	def append_to_sheet(self, sheet_name=None, sheet_range=None, values=None):
		if sheet_range is None:
			worksheet_range = sheet_name
		else:
			worksheet_range = f'{sheet_name}!{sheet_range}'

		if all(isinstance(v, list) for v in values):
			values = values
		else:
			values = [values]

		response = self.sheet.values().append(
				spreadsheetId=self.spreadsheet_id,
				range=worksheet_range,
				valueInputOption="USER_ENTERED", 
				insertDataOption="OVERWRITE",
				body={"values": values}
				).execute()

		return response

	def overwrite_sheet(self, sheet_name=None, sheet_range=None, values=None):
		clear = self.clear_sheet(sheet_name=sheet_name)
		append = self.append_to_sheet(sheet_name=sheet_name, sheet_range=sheet_range, values=values)

		return clear, append

	def dataframe_to_sheet(self, sheet_name=None, dataframe=None, overwrite=True):
		if overwrite:
			clear = self.clear_sheet(sheet_name=sheet_name)
			append = self.append_to_sheet(sheet_name=sheet_name, values=dataframe.columns.tolist())
		else:
			clear = None

		append = self.append_to_sheet(sheet_name=sheet_name, values=dataframe.values.tolist())
		return clear, append

