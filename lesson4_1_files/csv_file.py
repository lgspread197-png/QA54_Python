import csv
from os import write

with open("user_csv.csv","w",encoding="utf-8",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name","email","role"])
    writer.writerow(["Lev", "lev@gm.com", "QA"])
    writer.writerow(["Ivan", "ivan@gm.com", "dev"])

with open("user_csv.csv") as file:
    reader = csv.reader(file)
    print(type(reader))
    for row in reader:
        print(row)

print("____")

        #emil = row[1]
with open("user_csv.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["name"],"-",row["role"])