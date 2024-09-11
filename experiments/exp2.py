import csv

with open("../files/weather.txt", "r") as file:
    data = list(csv.reader(file))
print(data)

city = input("Enter city to check the temperature: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
