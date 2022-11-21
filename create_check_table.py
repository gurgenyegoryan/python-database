import connect_mariadb_server
import get_csv_data
import mariadb

table_name = connect_mariadb_server.table_name
column_names = get_csv_data.columns_name
check_result = connect_mariadb_server.check_result
cur = connect_mariadb_server.conn.cursor()
values_type = get_csv_data.list_elements_type

j = 0
while j < 1:
    try:
        if check_result == 0:
            for i in range(0, len(column_names)):
                s = f"create table {table_name} ({column_names[0]} {values_type[0]});"
                cur.execute(s)
    except:
        for i in range(1, len(column_names)):
            try:
                s = f"alter table {table_name} add ({column_names[i]} {values_type[i]});"
                cur.execute(s)
            except mariadb.Error as e:
                print(f"You have column with this name: {e}")
            else:
                print(f"Column \"{column_names[i]}\" created.")
    j += 1
