import csv

with open('birthdays.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if '10-10' in row:
            print(row[3])
