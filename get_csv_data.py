import csv

# Open file
csv_file = "Individual_Incident_2004.csv"
with open(csv_file) as file_obj:
    # Skips the heading
    # Using next() method


    csv_data = csv.reader(open(csv_file))
    columns_name = next(csv_data)
    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    reader_obj_transfer = reader_obj
    # Iterate over each row in the csv file
    # using reader object
    list_elements_type = []

    for row in reader_obj:
        for element in row:
            try:
                type(int(element))
                list_elements_type.append('int NOT NULL')
            except:
                type(element)
                list_elements_type.append('longtext')
        break

print(len(columns_name))
print(len(list_elements_type))