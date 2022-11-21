import mariadb
import connect_mariadb_server
import get_csv_data
import create_check_table
import time
import datetime

# Get variables
csv_file = get_csv_data.csv_file
cur = connect_mariadb_server.conn.cursor()
table_name = connect_mariadb_server.table_name
column_names = get_csv_data.columns_name
values_type = get_csv_data.list_elements_type
csv_data = get_csv_data.csv_data

#Get values count that be set
values_count = len(column_names) * '?,'
values_count = values_count.rstrip(values_count[-1])

# Translate column names to the desired form in maria db
column_names_final = ''
for i in column_names:
    column_names_final = column_names_final + i + ','
column_names_final = column_names_final.rstrip(column_names_final[-1])

try:
    current = datetime.datetime.now()
    print(f"Process started {current}")
    start = time.time()
    cur.execute(f"LOAD DATA INFILE '{csv_file}' INTO TABLE {table_name} \
                fields terminated BY ',';")

except mariadb.Error as e:
    print(f"Error: {e}")

current = datetime.datetime.now()
print(f"Process ended {current}")
time.sleep(5)
end = time.time()
timer = end - start
print(f"Process to last {timer/60} minutes")
# Set rows in table
# row_final = []
# for row in csv_data:
#     for i in row:
#         if i == '':
#             i = 0
#         try:
#             int(i)
#         except ValueError:
#             row_final.append(i)
#         else:
#             row_final.append(int(i))
#     row_final = tuple(row_final)
#     print(row_final)
#     try:
#         cur.execute(f"INSERT INTO {table_name} ({column_names_final}) VALUES ({values_count})", row_final)
#     except mariadb.Error as e:
#         print(f"Error: {e}")
#     else:
#         print('row set: ')
#
# cur.close()
