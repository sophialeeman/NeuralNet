import numpy as np
import csv
file = open("trainingdata.csv")
filereader = csv.reader(file)
rows = []
for row in filereader:
    rows.append(row)
file.close()