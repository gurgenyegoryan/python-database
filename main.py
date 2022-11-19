import mariadb
import connect_mariadb_server
import get_csv_data

cur = connect_mariadb_server.conn.cursor()
create_table = connect_mariadb_server.create_table
column_names = get_csv_data.columns_name
values_type = get_csv_data.list_elements_type
database_name = 'data1_big'
# Create database if not exist
j = 0
while j < 2:
    if create_table is None:
        s = f"create table {database_name} ({column_names[0]} {values_type[0]});"
        cur.execute(s)
        create_table = f'{database_name}'
    else:
        for i in range(1, len(column_names)):
            try:
                s = f"alter table {database_name} add ({column_names[i]} {values_type[i]});"
                cur.execute(s)
            except mariadb.Error as e:
                print(f"You have column with this name: {e}")
    j += 1
# Add data in file

reader_obj = get_csv_data.csv_data
column_names_final = ''

# for i in column_names:
#     column_names_final = column_names_final + i + ','

values_count = 49 * '?,'
values_count = values_count.rstrip(values_count[-1])
cur.execute(f"SHOW COLUMNS FROM {database_name}")
for i in cur:
    column_names_final = column_names_final + i[0] + ','

column_names_final = column_names_final.rstrip(column_names_final[-1])
k = 0
for row in reader_obj:
    # print(row[0])
    # print(type(row[0]))
    # for i in row:
    #     print(i)
    #     print(type(i))
    #     break
    #     if type(i) == str:
    #         i = '\"' + i + '\"'
    #     roww = roww + i + ','
    # break
    # roww = roww.rstrip(roww[-1])
    # print(type(roww))
    # break
    # sql = f"insert into data1_big ({heading}) values ({roww});"

    try:
        cur.execute(f"INSERT INTO {database_name} ({column_names_final}) VALUES ({values_count})", (row))
        # cur.execute(f"INSERT INTO data1_big ({column_names_final}) VALUES ({roww});")
        print('row set: ')
    except mariadb.Error as e:
        print(f"Error: {e}")

    #cur.commit()
cur.close()
    #cur.execute(f"INSERT INTO data1_big ({column_names_final}) VALUES ({roww});")
    # conn.commit()
    #
    # print("Row inserted")
