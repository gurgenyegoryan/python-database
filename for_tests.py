import csv
import mariadb
import sys
import get_csv_column

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

csv_file = "Individual_Incident_2004.csv"


csv_data = csv.reader(open(csv_file))
header = next(csv_data)
#print(header)



with open('Individual_Incident_2004.csv') as file_obj:
    # Skips the heading
    # Using next() method
    heading = next(file_obj)

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv file
    # using reader object
    roww = ''
    for row in reader_obj:
        # print(heading)
        # break
        # #print(row)

        for i in row:
            print(i)
            roww = roww + i + ','
        roww = roww.rstrip(roww[-1])

        sql = f"insert into data1_big ({heading}) values ({roww});"
        cur.execute(f"insert into data1_big ({heading}) values ({roww});")
        conn.commit()

        print("Row inserted")





