import pyodbc

# conn = pyodbc.connect(
#     "Driver={PostgreSQL Unicode};"
#     "Server=localhost;"
#     "Port=5432;"
#     "Database=leapstart;"
#     "Uid=postgres;"
#     "Pwd=@2333103080@;"
# )
# #initializing the cursor
# cursor=conn.cursor();
# #running the direct query
# qry="insert into students values('arun',55,57,88,87,99)"
# # handeling the queries
# cursor.execute(qry)

# #commits saves into the table
# cursor.commit();

# #closing the cursor and data connection
# cursor.close();
# conn.close();

# print ("record insert sucessfully")

#insert using the tuple
conn = pyodbc.connect(
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=leapstart;"
    "Uid=postgres;"
    "Pwd=@2333103080@;"
)
cursor=conn.cursor();
#creating a pratical qry
qry= "insert into students values (?,?,?,?,?,?)"
#define a tuple with multiple records
data = [("Ajay",77,56,56,56,99),("narsima",77,56,56,56,99),("yash",77,56,56,56,99),("omer",77,56,56,56,99)];
cursor.executemany(qry, data);
conn.commit();
cursor.close;
conn.close;

print ("record insert sucessfully")

