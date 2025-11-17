import csv

def read_as_dict(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        result = {}
        for row in reader:
            result[row["name"]] = row["country"]
            print(result)
            
read_as_dict("people.csv")
