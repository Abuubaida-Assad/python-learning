import pandas as pd
import pyodbc

df = pd.read_excel("exceltodb.xlsx");

conn = pyodbc.connect(
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=leapstart;"
    "Uid=postgres;"
    "Pwd=@2333103080@;"
)

cursor = conn.cursor();
qry = """
INSERT INTO students1 (id, name, age, marks)
VALUES (?, ?, ?, ?)
"""
data = list(df.itertuples(index=False, name=None))
cursor.executemany(qry, data)
conn.commit()
cursor.close()
conn.close()
print("data added sucessfully")


