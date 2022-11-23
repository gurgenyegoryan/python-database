import sys
import mariadb
import csv
import get_csv_data

#username = os.environ.get("username")
#password = os.environ.get("password")

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

cursor = conn.cursor()
csv_file = "Individual_Incident_2004.csv"
with open(csv_file) as file_obj:
    # Get columns name
    csv_data = csv.reader(open(csv_file))
columns_name = get_csv_data.columns_name
def add_data(csvv):
    global columns_name
    try:
        statement = f"INSERT INTO bigData ({columns_name}) VALUES ({csvv})"
        data = csv_data
        cursor.execute(statement)
        cursor.commit()
        print("Successfully added entry to database")
    except mariadb.Error as e:
        print(f"Error adding entry to database: {e}")




row_final = []
j = 0
for row in csv_data:
    csvv = tuple(row)
    #print(csvv)
    add_data(csvv)
    # for i in row:
    #     if i == '':
    #         i = 0
    #     try:
    #         int(i)
    #     except ValueError:
    #         row_final.append(i)
    #     else:
    #         row_final.append(int(i))
    # row_final = tuple(row_final)
    # print(row_final)


