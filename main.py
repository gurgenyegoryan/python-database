import mariadb
import sys
import csv
import connect_mariadb_server
import get_csv_data

cur = connect_mariadb_server.conn.cursor()
create_table = connect_mariadb_server.create_table
column_names = get_csv_data.columns_name
values_type = get_csv_data.list_elements_type

# Create database if not exist
j = 0
while j < 2:
    if create_table is None:
        s = f"create table data1_big ({column_names[0]} {values_type[0]});"
        cur.execute(s)
        create_table = 'data1_big'
    else:
        for i in range(1, len(column_names)):
            try:
                s = f"alter table data1_big add ({column_names[i]} {values_type[i]});"
                cur.execute(s)
            except mariadb.Error as e:
                print(f"You have column with this name: {e}")
    j += 1
# Add data in file

reader_obj = get_csv_data.csv_data
column_names_final = ''

# for i in column_names:
#     column_names_final = column_names_final + i + ','
roww = ()
cur.execute("SHOW COLUMNS FROM data1_big")
for i in cur:
    column_names_final = column_names_final + i[0] + ','

column_names_final = column_names_final.rstrip(column_names_final[-1])
k = 0
for row in reader_obj:
    for i in row:
        if str(i):
            i = '\'' + i + '\''
        append_roww = roww + i
        roww = append_roww

        # roww = roww.rstrip(roww[-1])
    print(roww)
    break
    # sql = f"insert into data1_big ({heading}) values ({roww});"
    cur.execute(f"INSERT INTO data1_big ({column_names_final}) VALUES ({roww});")
    # conn.commit()
    #
    # print("Row inserted")
