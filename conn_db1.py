
# import pyodbc

# # Database connection string
# conn_str = (
#     "Driver={PostgreSQL Unicode};"
#     "Server=localhost;"
#     "Port=5432;"
#     "Database=leapstart;"
#     "Uid=postgres;"
#     "Pwd=@2333103080@;"
# )

# try:
#     # Connect to PostgreSQL
#     conn = pyodbc.connect(conn_str)

#     print("Database connected successfully!")

#     # Create cursor
#     cursor = conn.cursor()

#     # Execute query
#     cursor.execute("SELECT version();")

#     # Fetch result
#     result = cursor.fetchone()

#     print("PostgreSQL Version:", result[0])

# except pyodbc.Error as e:
#     print("Connection Error:", e)

# finally:
#     if 'cursor' in locals():
#         cursor.close()

#     if 'conn' in locals():
#         conn.close()

#     print("Connection closed.")



# import pyodbc

# # Database connection string
# conn_str = (
#     "Driver={PostgreSQL Unicode};"
#     "Server=localhost;"
#     "Port=5432;"
#     "Database=leapstart;"
#     "Uid=postgres;"
#     "Pwd=@2333103080@;"
# )

# try:
#     # Connect to PostgreSQL
#     conn = pyodbc.connect(conn_str)

#     print("Database connected successfully!")

#     cursor = conn.cursor()

#     # Check PostgreSQL version
#     cursor.execute("SELECT version();")
#     result = cursor.fetchone()

#     print("\nPostgreSQL Version:")
#     print(result[0])

#     # Display all student records
#     print("\n========== STUDENT RECORDS ==========")

#     cursor.execute("SELECT * FROM students;")

#     # Fetch column names
#     columns = [column[0] for column in cursor.description]
#     print(" | ".join(columns))

#     print("-" * 90)

#     # Fetch all rows
#     rows = cursor.fetchall()

#     for row in rows:
#         print(" | ".join(str(value) for value in row))

#     print("-" * 90)
#     print("Total Records:", len(rows))

# except pyodbc.Error as e:
#     print("Connection Error:", e)

# finally:
#     if 'cursor' in locals():
#         cursor.close()

#     if 'conn' in locals():
#         conn.close()

#     print("\nConnection closed.")


import pyodbc

conn = pyodbc.connect(
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=leapstart;"
    "Uid=postgres;"
    "Pwd=@2333103080@;"
)

#connection to database

# cn = pyodbc.connect(conn)

#initializing the cursor
cursor = conn.cursor()

#handleing the queries

cursor.execute("SELECT * FROM students")

#handeling the data

data = cursor.fetchall();
print(f"connected sucessfully")
print(data);

#closing the cursor and data connection

cursor.close();
conn.close();


