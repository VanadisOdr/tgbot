import csv

from datetime import timedelta, datetime

today = datetime.now()
date_start = (today + timedelta(days=5)).strftime("%m-%d")

print(date_start)

with open('birthdays.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if date_start in row:
            print(row[3])