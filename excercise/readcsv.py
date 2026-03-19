import csv
with open("data.csv","r") as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        count+=1
    print(count)