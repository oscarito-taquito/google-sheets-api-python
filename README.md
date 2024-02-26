# google-sheets-api-python
Mastering the Google Sheets API with Python

```markdown
# Pygs: Google Sheets Python Interface

Pygs provides a convenient way to interact with Google Sheets using Python. This guide will help you get started with setting up and using the Pygs class to perform various operations like reading, writing, and modifying Google Sheets.

## Setup

Before using Pygs, ensure you have the following prerequisites:

- A Google Cloud Platform project with the Google Sheets API enabled.
- A service account key file for authentication.
- Python 3.6 or later.
- Google Client Library and Pandas installed in your environment.

You can install the required libraries using pip:

```bash
pip install google-api-python-client google-auth pandas
```

## Authentication

The Pygs class uses a service account for Google Sheets API authentication. Make sure you have your service account JSON key file saved in the same directory as your script, or update the `key_file` path in the code.

## Initialization

First, import the necessary libraries and initialize the Pygs class with your spreadsheet ID:

```python
from pygs import Pygs

# Initialize with your spreadsheet ID
pygs = Pygs(spreadsheet_id='your_spreadsheet_id_here')
```

## Usage

### Listing Sheet Names

To get a list of sheet names and their IDs in the spreadsheet:

```python
sheet_names, sheet_ids = pygs.list_sheet_names()
print(sheet_names)
print(sheet_ids)
```

### Creating a New Sheet

To create a new sheet within the spreadsheet:

```python
response = pygs.create_sheet(sheet_name='New Sheet Name', sheet_index=1)
print(response)
```

### Reading from a Sheet

To read data from a specific sheet and range:

```python
values = pygs.read_sheet(sheet_name='Sheet1', sheet_range='A1:C10')
print(values)
```

### Clearing a Sheet

To clear the contents of a specific sheet or range:

```python
response = pygs.clear_sheet(sheet_name='Sheet1', sheet_range='A1:C10')
print(response)
```

### Appending to a Sheet

To append values to a specific sheet or range:

```python
values = [["Value1", "Value2", "Value3"]]
response = pygs.append_to_sheet(sheet_name='Sheet1', values=values)
print(response)
```

### Overwriting a Sheet

To clear and then append values to a specific sheet or range:

```python
values = [["New Value1", "New Value2", "New Value3"]]
clear_response, append_response = pygs.overwrite_sheet(sheet_name='Sheet1', sheet_range='A1', values=values)
print(clear_response, append_response)
```

### Exporting a DataFrame to a Sheet

To export a Pandas DataFrame to a sheet (with an option to overwrite):

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})

# Export to Google Sheets
clear_response, append_response = pygs.dataframe_to_sheet(sheet_name='Sheet1', dataframe=df, overwrite=True)
print(clear_response, append_response)
```

## Conclusion

Pygs simplifies the process of interacting with Google Sheets through Python. With it, you can automate the management and analysis of your data. Remember to replace 'your_spreadsheet_id_here' with your actual Google Sheets spreadsheet ID and ensure your service account has the appropriate permissions.
```
