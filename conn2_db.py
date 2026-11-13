
import pyodbc

# conn = pyodbc.connect(
#     "Driver={PostgreSQL Unicode};"
#     "Server=localhost;"
#     "Port=5432;"
#     "Database=leapstart;"
#     "Uid=postgres;"
#     "Pwd=@2333103080@;"
# )

# #connection to database

# # cn = pyodbc.connect(conn)

# # print(pyodbc.drivers()):

# #initializing the cursor
# cursor = conn.cursor()

# #handleing the queries

# cursor.execute("SELECT * FROM persons")

# #handeling the data

# data = cursor.fetchall();
# print(f"connected sucessfully")
# print(data);

# #closing the cursor and data connection

# cursor.close();
# conn.close();

conn = pyodbc.connect(
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=leapstart;"
    "Uid=postgres;"
    "Pwd=@2333103080@;"
)
#initializing the cursor
cursor=conn.cursor();
#running the direct query
qry = "INSERT INTO persons VALUES (104, 'faizan', 19, 'hyderabad', 'telangana', 999)"
# handeling the queries
cursor.execute(qry)

#commits saves into the table
cursor.commit();

#closing the cursor and data connection
cursor.close();
conn.close();

print ("record insert sucessfully")