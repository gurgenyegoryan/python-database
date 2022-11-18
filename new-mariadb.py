import mariadb
import sys
import get_csv_data
import connect_mariadb_server

le

#Get csv file columns and its format!
list_elements_type = get_csv_data.list_elements_type
#list_elements = get_csv_column.
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