# import os

# folder_path = "landingfolder"

# for file in os.listdir(folder_path):
#     if file.endswith(".json"):
#         print(os.path.join(folder_path, file))



# import os
# import pandas as pd
# import pyodbc
# from datetime import date

# folder_path = os.path.expanduser("~/Documents/Python_learning/landingfolder")

# today = date.today().strftime("%Y%m%d")



# for file in os.listdir(folder_path):
#     if today in file:
#         fname=file

#         df = pd.read_json("landingfolder/"+fname)
#         print(df)




import os
import pandas as pd
import pyodbc
from datetime import date

folder_path = os.path.expanduser("~/Documents/python_learning/landingfolder")

today = date.today().strftime("%Y%m%d")

con = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=myapplication;"
    "UID=postgres;"
    "PWD=@2333103080@;"
)

cursor = con.cursor()

# Reading today's JSON file
for file in os.listdir(folder_path):
    if today in file and file.endswith(".json"):
        fname = file

        df = pd.read_json(os.path.join(folder_path, fname))
        print(df)
        break
else:
    print("Today's JSON file not found!")
    cursor.close()
    con.close()
    exit()

# Insert query
query = """
    INSERT INTO students
    (idno, name, age, course, fees, joindate,
     inserted_on, updated_on)
    VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
"""

# Inserting data into PostgreSQL
for index, row in df.iterrows():

    cursor.execute(
        query,
        row["idno"],
        row["sname"],
        row["age"],
        row["course"],
        row["fees"],
        row["joindate"]
    )

    con.commit()

    print(row["sname"], "Inserted successfully!")

cursor.close()
con.close()

print("ETL process completed successfully!")
