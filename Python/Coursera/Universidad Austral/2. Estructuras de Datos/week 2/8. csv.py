import csv

# Leer un archivo csv
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/9. csv_file.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, quotechar="||")
    for row in reader:
        print(', '.join(row))

