import pandas as pd
import pyodbc

# 1️⃣ Load CSV
df = pd.read_csv('cleaned_car_data.csv')

# 2️⃣ SQL Server connection details
server = r"SY_MOIZ\SYMOIZ"     # Your SQL Server instance
database = 'pakwheel'
username = 'sa'
password = '1218'

# 🔥 Correct connection string using SQL Server Authentication
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# 3️⃣ Create table
create_table_query = """
IF OBJECT_ID('dbo.Cars', 'U') IS NOT NULL
    DROP TABLE dbo.Cars;

CREATE TABLE dbo.Cars (
    title NVARCHAR(255),
    price FLOAT,
    year INT,
    mileage FLOAT,
    fuel NVARCHAR(50),
    engine FLOAT,
    transmission NVARCHAR(50)
);
"""
cursor.execute(create_table_query)
conn.commit()

# 4️⃣ Insert data into table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO dbo.Cars (title, price, year, mileage, fuel, engine, transmission)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    row['title'], row['price'], row['year'], row['mileage'], row['fuel'], row['engine'], row['transmission'])

conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into SQL Server!")
