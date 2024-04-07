import csv

with open("cardekhoDataset.csv" , "r") as data:
    csv = csv.reader(data, delimiter=",")
    for row in csv:
        print(row)