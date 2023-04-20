import csv
import time

result = time.gmtime(time.time())
day = 10-10

with open('birthdays.csv', 'r') as f:
    reader = csv.reader(f)

    for line in reader:
            print(line[1])
