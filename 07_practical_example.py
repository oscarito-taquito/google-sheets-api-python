import pandas as pd
from pygs import Pygs

df = pd.read_csv('data/1000 Sales Records.csv')
df = df[df['Total Revenue'] > 55000]

summary = df.groupby(['Region']).agg(
		{
			'Order ID': 'nunique',
			'Total Revenue': 'sum'
		}
	)


summary = summary.reset_index()
summary.columns = ['Region', 'Orders', 'Revenue']
summary['Avg Order Rev'] = summary['Revenue'] / summary['Orders']

print(summary.head())

pg = Pygs(spreadsheet_id='1FtopfMof8tEaB7h4DwMjr5MZAv9mff_TFMZJduZVv0M')

pg.create_sheet(sheet_name="Summary Revenue")
pg.dataframe_to_sheet(sheet_name='Summary Revenue', dataframe=summary)
