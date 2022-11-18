import mariadb
import sys
import get_csv_column
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

#Get csv file columns and its format!
list_elements_type = get_csv_column.list_elements_type
list_elements = get_csv_column.list_of_column_names
print(list_elements[1])

#Delete if table exist
#cur.execute('DROP TABLE IF EXISTS data1_big;')
#Create or alter table
j = 0
while j < 2:
    if create_table is None:
        s = f"create table data1_big ({list_elements[0]} {list_elements_type[0]});"
        cur.execute(s)
        create_table = 'data1_big'
    else:
        for i in range(1, len(list_elements)):
            try:
                    s = f"alter table data1_big add ({list_elements[i]} {list_elements_type[i]});"
                    cur.execute(s)
            except mariadb.Error as e:
                print(f"You have column with this name: {e}")
    j += 1

#Load csv file
# s = "LOAD DATA INFILE '/usr/local/mysql/var/Individual_Incident_2004.csv' INPUT TABLE data1_big"
#
# cur.execute(s)