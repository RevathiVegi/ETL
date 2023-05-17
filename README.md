# ETL
## Extraction of csv file, Transformation and Loading to PostGreSQL - amazon_sale_report.csv(zip file)
### Extraction 
1) Importing Required Libraries
```Python
from sqlalchemy import create_engine
import pandas as pd
```
- This code imports the create_engine function from the sqlalchemy library and the pandas library.
2) Defining the Connection String
```Python
connection_str = 'postgresql+psycopg2://username:password@host/database name'
```
- This code defines a connection string to the PostgreSQL database.
- It includes the username , password , host , and database name .
3) Creating the Engine
```Python
engine = create_engine(f'{connection_str}')
```
- This code creates an engine using the create_engine function from the sqlalchemy library. 
- The engine connects to the PostgreSQL database using the connection string defined in the previous step.
4) Creating the Connection
```Python
connection = engine.connect()
```
- This code creates a connection to the database using the connect method of the engine created in the previous step.
5) Reading Data from CSV
```Python
readfile = "amazon_sale_report.csv/Amazon Sale Report.csv" 
df = pd.read_csv('amazon_sale_report.csv/Amazon Sale Report.csv',
                       dtype={
                           'index': int,
                           'order_id': str,
                           'date': str,
                           'status': str,
                           'fulfilment': str,
                           'sales_channel': str,
                           'ship_service_level': str,
                           'style': str,
                           'sku': str,
                           'category': str,
                           'size': str,
                           'asin': str,
                           'courier_status': str,
                           'qty': int,
                           'amount': int,
                           'ship_city': str,
                           'ship_state': str,
                           'ship_postal_code': str,
                           'ship_country': str,
                           'promotion_ids': str,
                           'b2b': bool,
                           'fulfilled_by': str,
                           'unnamed_22': str,
                           'currency': str 
                       })
```
- This code reads the data from a CSV file called Amazon Sale Report.csv and stores it in a pandas dataframe called df. 

### Transformation
- The dtype parameter is used to specify the data types of the columns in the dataframe.
6) Renaming Columns
```Python
sales=sales.rename(columns={"Order ID": "order_id","Date":"date", "Status":"status", "Fulfilment":"fulfilment", "Sales Channel ":"sales_channel", "ship-service-level":"ship_service_level", "Style":"style", "SKU":"sku", "Category":"category", "Size":"size", "ASIN":"asin", "Courier Status":"courier_status", "Qty":"qty", "Amount":"amount", "ship-city":"ship_city", "ship-state":"ship_state", "ship-postal-code":"ship_postal_code", "ship-country":"ship_country", "promotion-ids":"promotion_ids", "B2B":"b2b", "fulfilled-by":"fulfilled_by", "Unnamed: 22":"unnamed_22"})
sales.columns
```
- This code renames the columns in the sales dataframe to match the column names in the database table that we'll be creating in the next step.
7) Creating the Table
```Python
conn.execute('''
    CREATE TABLE sales (
        index SERIAL PRIMARY KEY,
        order_id VARCHAR(256),
        date DATE,
        status VARCHAR(64),
        fulfilment VARCHAR(64),
        sales_channel VARCHAR(64),
        ship_service_level VARCHAR(64),
        style VARCHAR(64),
        sku VARCHAR(256),
        category VARCHAR(64),
        size VARCHAR(64),
        asin VARCHAR(64),
        courier_status VARCHAR(64),
        qty INTEGER,
        amount NUMERIC(10, 2),
        ship_city VARCHAR(64),
        ship_state VARCHAR(64),
        ship_postal_code VARCHAR(64),
        ship_country VARCHAR(64),
        promotion_ids TEXT,
        b2b BOOLEAN,
        fulfilled_by VARCHAR(64),
        unnamed_22 VARCHAR(64),
        currency VARCHAR(64)
    )
''')
```
- This code uses the connection object to execute a SQL query that creates a new table called sales. 
- The table has 23 columns, including an index column that is used as the primary key.  

### Load
8) Inserting Data into the Table
```Python
sales.to_sql('sales', con=conn, if_exists='append', index=False)
```
- This code inserts the data from the sales dataframe into the sales table in the database using the to_sql method of the dataframe. 
- The if_exists parameter is set to 'append', which means that if the table already exists, the data will be added to the end of the table. 
- The index parameter is set to False, which means that the index column of the dataframe will not be included in the database table.
9) Closing the Connection
```Python
connection.close()
```
- This code closes the connection to the database. 
- It's always a good practice to close the connection when you're finished using it.
## Issues that I faced while writing this code:
- Understanding the data types of the columns in the CSV file and mapping them correctly to the appropriate data types in the database table. 
- This can be tricky especially when dealing with dates, booleans, and numeric data.
- Incorrectly specifying the file path or table name in the code.
- Incorrectly specifying the database credentials or database name in the connection string.
- Dealing with errors that may occur during the data loading process such as missing or invalid data in the CSV file, or database connection errors.




## CSV Extraction, Transformation, and Loading to .csv. (Files : fpl_tweets.csv(zip); Output file: tweets1.csv(zip))
### Introduction
- This code performs data extraction, transformation, and loading from a CSV file. 
- It utilizes the pandas library for data manipulation and analysis, psycopg2 library for PostgreSQL database connection, and numpy library for support with arrays and matrices. 
- The code reads a CSV file, performs various transformations and cleaning operations, and saves the processed data into another CSV file.
### Extraction 
```Python
import pandas as pd
import psycopg2
import numpy as np
pd.options.mode.chained_assignment = None
```
- The first line imports the pandas library, which provides data manipulation and analysis tools.
- The second line imports the psycopg2 library, which is used for connecting to PostgreSQL databases.
- The third line imports the numpy library, which provides support for large, multi-dimensional arrays and matrices.
- The fourth line disables the warning for chained assignments in pandas.

```Python
dtypes = {
    'ID': str,
    'Timestamp': str,
    'User': str,
    'Text': str,
    'Hashtag': str,
    'Retweets': float,
    'Likes': float,
    'Replies': float,
    'Source': str,
    'Location': str,
    'Verified_Account': bool,
    'Followers': float,
    'Following': float
}

df = pd.read_csv('FPL_tweets.csv/fpl_tweets.csv', dtype=dtypes, low_memory=False)
```
- Here, I have defined the column data types for the DataFrame using the dtypes dictionary.
- The pd.read_csv function is used to read the CSV file named 'fpl_tweets.csv' and store it in the DataFrame df. 
- The dtype parameter specifies the data types for each column.
- The low_memory=False parameter is set to prevent a warning related to mixed data types in columns.

```Python
df = df.rename(columns={'Following':'following'})

tweets = df
tweets.columns
tweets = tweets.rename(columns={"ID": "id","Timestamp":"timestamp", "User":"user", "Text":"text", "Hashtag":"hashtag", "Retweets":"retweets", "Likes":"likes", "Replies":"replies", "Source":"source", "Location":"location", "Verified_Account":"verified_account", "Followers":"followers", "Following":"following"})

tweets1 = tweets[['id', 'location', 'user', 'text', 'hashtag', 'retweets', 'likes', 'replies', 'source', 'location', 'verified_account', 'followers', 'following']]
```
- In the first line, I have renamed the column 'Following' to 'following' in the DataFrame df.
- The next few lines create a new DataFrame called tweets and rename several columns using the rename() method.
- Finally, I have created another DataFrame tweets1 by selecting specific columns from tweets.

## Transformation

```Python
numeric_columns = ['retweets', 'likes', 'replies']
unique_values = df[numeric_columns].apply(pd.Series.unique)

columns_to_drop = ['id', 'timestamp', 'hashtag', 'source', 'location']
df = df.drop(columns=columns_to_drop)
```
- The first line creates a list called numeric_columns containing the names of numeric columns.
- The second line finds the unique values for the columns specified in numeric_columns using apply() and pd.Series.unique.
- The third line creates a list called columns_to_drop containing the names of columns to be dropped.
- The last line drops the columns specified in columns_to_drop from the DataFrame df.

```Python
df = df.drop_duplicates()
df = df.dropna()
```
- The second line drops rows with missing values (NaN) from the DataFrame df.

```Python
df['text'] = df['text'].str.replace('[^a-zA-Z\s]', '', regex=True)
```
- This line uses the str.replace() method to remove non-alphabetic characters and special characters from the 'text' column in the DataFrame df. 
- The regular expression '[^a-zA-Z\s]' matches any character that is not a letter or a whitespace.

```Python
df['verified_account'] = df['verified_account'].astype(bool)
df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
df['following'] = pd.to_numeric(df['following'], errors='coerce')
```
- The first line converts the 'verified_account' column to boolean data type.
- The second line converts the 'followers' column to numeric data type, using pd.to_numeric() with the errors='coerce' parameter to replace invalid values with NaN.
- The third line converts the 'following' column to numeric data type, also handling invalid values.

```Python
df = df.reset_index(drop=True)
print(df.head())
```
- This line resets the index of the DataFrame df and drops the old index.
- The print() function is used to display the first few rows of the modified DataFrame.

## Load

```Python
tweets1.to_csv('tweets1.csv', index=False)
```
- This line exports the DataFrame tweets1 to a CSV file named 'tweets1.csv', excluding the index column.
### Dependencies
- Ensure you have the following dependencies installed:
pandas (version 1.3.0 or later)
psycopg2 (version 2.9.0 or later)
numpy (version 1.21.0 or later)


To install the required dependencies, follow these steps:
Open a command prompt or terminal.
1) Run the following command to install pandas:
```Python
pip install pandas>=1.3.0
```
2) Run the following command to install psycopg2:
```Python
pip install psycopg2>=2.9.0
```
3) Run the following command to install numpy:
```Python
pip install numpy>=1.21.0

```
### Usage
- Follow the instructions below to use the code:
1) Place the input CSV file 'fpl_tweets.csv' in the same directory as the script.
2) If necessary, update the dtypes dictionary in the code to match the column data types in the CSV file.
3) Run the script to extract, transform, and load the data.
4) The processed data will be saved in the 'tweets1.csv' file in the same directory as the script.
### Potential Issues
- Please be aware of the following potential issues while running the code:
1) Ensure that the input CSV file ('fpl_tweets.csv') is in the correct format and located in the same directory as the script.
2) Check for any missing or inconsistent data in the CSV file, as it may lead to errors during data transformation.
3) Make sure to have the required versions of dependencies installed, as incompatible versions can cause compatibility issues.



## CSV Extraction, Transformation, and Loading to .xlsx. (Files : Spotify_Youtube.csv ; Output file: Spotify_Youtube.xlsx)
### Introduction 
- This code takes a CSV file, performs some data manipulation using pandas, and saves the modified data to an Excel file. 
- Here's a breakdown of the steps:
- Import the required modules: openpyxl, pandas, and os.
- Set the path of the input CSV file using csv_file_path.
- Read the CSV file into a pandas DataFrame using pd.read_csv(), and store it in the variable df.
- Retrieve the column names of the DataFrame using df.columns.
- Create a new column called 'Total Plays' in the DataFrame by adding the 'Views' and 'Likes' columns.
- Set the path for the output Excel file using excel_file_path.
- Create the output directory if it doesn't already exist using os.makedirs().
- Create an Excel workbook using openpyxl.Workbook() and get the active worksheet using workbook.active.
- Iterate over the column names of the DataFrame and write them to the first row of the worksheet.
- Iterate over the rows and columns of the DataFrame, writing the values to the corresponding cells in the worksheet.
- Save the workbook to the specified Excel file path using workbook.save().
- Check if the Excel file was created successfully using os.path.isfile() and print the appropriate message.
- Print the absolute path of the created Excel file.
### Extraction 
```Python
import openpyxl
import pandas as pd
import os
```
- The code begins by importing the necessary modules: openpyxl for working with Excel files, pandas for data manipulation, and os for operating system-related functions.

```Python
csv_file_path = 'work/src/Spotify_Youtube.csv/Spotify_Youtube.csv'
```
- This line sets the path of the input CSV file, Spotify_Youtube.csv, which is assumed to be located at 'work/src/Spotify_Youtube.csv/Spotify_Youtube.csv'.

```Python
df = pd.read_csv('Spotify_Youtube.csv/Spotify_Youtube.csv')
```
- Here, the pd.read_csv() function from pandas is used to read the CSV file and store the data in a DataFrame called df.

```Python
df.columns
```
- This line retrieves the column names of the DataFrame df.

```Python
df['Total Plays'] = df['Views'] + df['Likes']
```
- This line creates a new column called 'Total Plays' in the DataFrame df, which is calculated by summing the values of the 'Views' and 'Likes' columns.

```Python
excel_file_path = 'work/output/Spotify_Youtube.xlsx'
```
- This line sets the path for the output Excel file, 'Spotify_Youtube.xlsx', which is assumed to be located at 'work/output/Spotify_Youtube.xlsx'.

```Python
output_directory = "work/output"
os.makedirs(output_directory, exist_ok=True)
```
- These lines create the output directory 'work/output' if it doesn't already exist. os.makedirs() is used with the exist_ok=True parameter to prevent an error if the directory already exists.

```Python
workbook = openpyxl.Workbook()
worksheet = workbook.active
```
- Here, an Excel workbook is created using openpyxl.Workbook(), and the active worksheet is obtained using workbook.active.

```Python
for column_index, column_header in enumerate(df.columns, start=1):
    worksheet.cell(row=1, column=column_index, value=column_header)
```
- This loop iterates over the column names of the DataFrame df and assigns each column header to a cell in the first row of the worksheet.

```Python
for row_index, row_data in df.iterrows():
    for column_index, column_header in enumerate(df.columns, start=1):
        worksheet.cell(row=row_index+2, column=column_index, value=row_data[column_header])
```
- These nested loops iterate over the rows and columns of the DataFrame df. 
- The values from each row of the DataFrame are written to the corresponding cells in the worksheet.

```Python
workbook.save(excel_file_path)
```
- This line saves the workbook to the specified Excel file path.

```Python
if os.path.isfile(excel_file_path):
    print("Excel file created successfully!")
else:
    print("Excel file not found.")
```
- This conditional statement checks if the Excel file was created successfully by verifying its existence using os.path.isfile(). 
- It prints a corresponding success or failure message.

```Python
print("Excel file path:", os.path.abspath(excel_file_path))
```
- Finally, this line prints the absolute path of the created Excel file.
### Potential Issues:
1) File Paths: Ensure that the input CSV file 'Spotify_Youtube.csv' is located at the correct path 'work/src/Spotify_Youtube.csv/Spotify_Youtube.csv', and the  
  output directory 'work/output' exists or can be created.
2) Missing Modules: Make sure that the required modules (openpyxl and pandas) are installed and accessible in the Python environment where the code is executed.
3) DataFrame Columns: Check that the CSV file has the expected column names ('Views', 'Likes'), and they are case-sensitive. Otherwise, the column manipulation a and iteration steps may encounter errors.
4) Excel File Overwrite: Be cautious when running the code multiple times, as it will overwrite the existing Excel file at the specified path without  
   confirmation.
5) Memory Usage: If the input CSV file is extremely large, the code may consume a significant amount of memory, especially during the DataFrame creation and 
   iteration steps. 
   This could potentially lead to memory errors on systems with limited resources. 
   In such cases, consider processing the data in smaller chunks or optimizing memory usage.
6) General Compatibility: Confirm that the code is executed using a compatible Python version and that the required libraries are compatible with the version  
   being used. 
   Additionally, keep in mind that the code may not work correctly if there are significant changes to the library dependencies or if the underlying functionality changes.
   
   
   
   
## Extraction of csv file, Transformation and Loading to .json (Files: meets.csv, meets.py; Output file: meets.json)
### Documentation: The provided code performs the following steps:
- Imports necessary modules: csv, json, os, and pandas.
- Defines the file paths:
- csv_file_path: Path to the input CSV file ('meets.csv').
- json_file_path: Path to the output JSON file ('work/output/meets.json').
- Reads the CSV file into a DataFrame using pd.read_csv().
- Creates a new DataFrame meets to hold the data from the CSV file.
- Initializes an empty list data to store the transformed data.
- Reads and transforms the data from the CSV file using a csv.DictReader object. 
- Each row is transformed into a dictionary and appended to the data list.
- Checks if the JSON file already exists: If the file exists, it loads the existing JSON data into a list called existing_data.
- The transformed data from step 6 is appended to existing_data.
- The updated existing_data is then written back to the JSON file.
- If the file does not exist, it creates a new JSON file and writes the data list to it.
- Checks if the JSON file exists in the specified directory and prints the corresponding message.

### Extraction
```Python
import csv
import json
import os
import pandas as pd
```
- CSV file path
```Python
csv_file_path = 'meets.csv'
```

- Read the CSV file into a DataFrame
```python
df = pd.read_csv('meets.csv')
```

- Create a new DataFrame 'meets' to hold the data
```Python
meets = df
meets.columns
```

- JSON file path
```Python
json_file_path = 'work/output/meets.json'`
```

### Transformation
- List to store the transformed data
```Python
data = []
```

- Read and transform the data from the CSV file
```Python
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
```

### Load
- Check if JSON file exists
```Python
if os.path.isfile(json_file_path):
    # Load existing JSON data
    with open(json_file_path, 'r') as json_file:
        existing_data = json.load(json_file)
 ```   

- Append new data to existing JSON data 
```Python
existing_data.extend(data)
```

- Write updated JSON data back to the file
```Python
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file)
else:
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)
```

- Check if JSON file exists
```Python
directory = 'work/output/'
json_files = [file for file in os.listdir(directory) if file.endswith('.json')]

if len(json_files) > 0:
    print("JSON file exists")
else:
    print("JSON file does not exist")
```
### Potential issues:
- Ensure that the paths to the input CSV file and output JSON file are correct.
- The code assumes that the input CSV file has the specified column names ('MeetID', 'Federation', 'Date', 'MeetCountry', 'MeetState', 'MeetTown', 'MeetName'). 
- Make sure these column names match the actual column names in your CSV file.
- If the input CSV file contains large amounts of data, loading all the data into memory as a DataFrame may consume significant memory resources. 
- Consider processing the data in smaller chunks or using alternative approaches if memory becomes a limitation.
- Make sure the necessary libraries (e.g., pandas) are installed in your environment.
- The code assumes that the output JSON file is in the 'work/output/' directory. 
- Adjust the json_file_path and directory variables if your desired file location is different.








