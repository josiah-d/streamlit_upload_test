import csv
import sys

import pandas as pd

path = "data/data.csv"

# check pandas size
df = pd.read_csv(path)

print(f"pandas bytes: {sys.getsizeof(df)}")

# check csv size
with open(path, newline="") as f_obj:
    reader = csv.reader(f_obj, delimiter=",")

    data = [",".join(row) for row in reader]

print(f"csv bytes: {sys.getsizeof(data)}")
