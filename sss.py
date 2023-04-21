from datetime import datetime, timedelta
import csv


today = datetime.now()
date_start = (today + timedelta(days=5)).strftime("%m-%d")


with open('birthdays.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if date_start in row:
            print(row[3])
