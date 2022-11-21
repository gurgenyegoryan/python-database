import csv

# import pandas as pd
csv_file = "Individual_Incident_2004.csv"
with open(csv_file) as file_obj:
    # Get columns name
    csv_data = csv.reader(open(csv_file))
    columns_name = next(csv_data)
    # Create reader object by passing the file
    # object to reader method
    # Iterate over each row in the csv file
    # using reader object
    list_elements_type = []
    for row in next(csv_data):
        try:
            int(row)
        except ValueError:
            list_elements_type.append('longtext')
        else:
            list_elements_type.append('int')
