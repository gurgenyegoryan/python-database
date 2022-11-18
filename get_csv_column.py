import csv
csv_file = "Individual_Incident_2004.csv"
with open(csv_file) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    list_of_column_names_tmp = []
    list_of_column_names = []
    list_of_column_names_2 = []
    i = 0
    for row in csv_reader:
        if i == 0:
            list_of_column_names_tmp.append(row)
        else:
            list_of_column_names_2.append(row)
            break
        i += 1

list_elements_type = []
for i in range(0,len(list_of_column_names_2[0])):
    try:
        type(int(list_of_column_names_2[0][i]))
        list_elements_type.append('int NOT NULL')
    except:
        type(list_of_column_names_2[0][i])
        list_elements_type.append('longtext')
for i in range(0,len(list_of_column_names_tmp[0])):
    list_of_column_names.append(list_of_column_names_tmp[0][i])

#print(list_elements_type)
#print(len(list_of_column_names))
var = ''
for i in list_elements_type:
    var = var + i + ','
#print(var)
