import csv

with open('/Projects/Temps/Python/grades.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)
