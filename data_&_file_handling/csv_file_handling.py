# CSV - represent tables - rows and columns

# Write a CSV file

#------------------------------------------------------------

import csv
from pathlib import Path

path = Path("data/students.csv")

rows = [
    ["id", "name", "score"],
    [1, "John", 88],
    [2, "Alex", 67],
    [3, "Joe", 3]
]

rows_2 = [
    [5, "John", 88],
    [2, "Alex", 67],
    [1, "Joe", 3]
]
# newline -> tells python "Do not automatically add extra blank 
# lines when writing to this file"
with path.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with path.open("a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows_2)
    
# Read CSV normally

with path.open("r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read CSV as dictionaries

with path.open("r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(row)
        print(row["id"], row["name"], row["score"])