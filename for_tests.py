import csv
import mariadb
import sys
import get_csv_column
import connect_mariadb_server

with open('Individual_Incident_2004.csv') as file_obj:
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





