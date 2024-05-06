import csv

test_data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angels'],
]

with open('mydata.csv', 'w') as file:
    writer = csv.writer(file)
    for row in test_data:
        writer.writerow(row)