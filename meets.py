import csv
import json
import os
import pandas as pd

csv_file_path = 'meets.csv'

df = pd.read_csv('meets.csv')
df

meets = df
meets.columns

json_file_path = 'work/output/meets.json'

data = []


with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        transformed_row = {
            'MeetID': row['MeetID'],
            'Federation': row['Federation'],
            'Date': row['Date'],  # Additional transformations can be applied here
            'MeetCountry': row['MeetCountry'],  # Additional transformations can be applied here
            'MeetState': row['MeetState'].strip(),  # Example: Removing leading/trailing whitespaces
            'MeetTown': row['MeetTown'].strip(),  # Example: Removing leading/trailing whitespaces
            'MeetName': row['MeetName'].strip()  # Example: Removing leading/trailing whitespaces
        }
        data.append(transformed_row)


if os.path.isfile(json_file_path):
    
    with open(json_file_path, 'r') as json_file:
        existing_data = json.load(json_file)
    
    
    existing_data.extend(data)
    
    
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file)
else:
   
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)


directory = 'work/output/'
json_files = [file for file in os.listdir(directory) if file.endswith('.json')]

if len(json_files) > 0:
    print("JSON file exists")
else:
    print("JSON file does not exist")
