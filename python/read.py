import csv 
with open("write.csv",'w') as file:
    writer = csv.writer(file)

    writer.writerow(['Name',"Country"])
    writer.writerow(['Nirdesh',"KTM"])

import csv 
with open("write.csv",'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
