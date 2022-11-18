import mariadb
import sys
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Yeg.1995",
        host="176.32.195.85",
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

create_table = 'data1_big'

#function to check if 'data1_big' table exist in databas
def return_table_name(list_of_existing_tables):
    global create_table
    if create_table in list_of_existing_tables:
        return create_table
    else:
        create_table = None
        print("No database")
return_table_name(list_of_existing_tables)