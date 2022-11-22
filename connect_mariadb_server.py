import mariadb
import sys
# Connect to MariaDB Platform
table_name = 'bigData'
try:
    conn = mariadb.connect(
        user="root",
        password="Yeg.1995",
        host="ngn.am",
        port=3306,
        database="pythontest",
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

#Get list of existing tables
cur.execute("show tables;")
list_of_existing_tables = []
for x in cur:
    list_of_existing_tables.append(x[0])

#function to check if 'bigData' table exist in databas
check_result = int
def return_table_name(list_of_existing_tables):
    global table_name
    global check_result
    if table_name in list_of_existing_tables:
        print(f"You have table with name {table_name},it will be replaced by a new one")
    else:
        print(f"You dont have table with name {table_name}")
        check_result = 0

return_table_name(list_of_existing_tables)
