# ETL
## Extraction of csv file, Transformation and Loading to PostGreSQL - amazon_sale_report.csv
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




