import csv
from math import log
import pandas as pd
from matplotlib import pyplot as plt

csvfile = 'coordinates1.csv'
with open(csvfile,'w',newline='') as fobj:
    fields = ['X_coord','Y_coord']
    csvwriter = csv.writer(fobj)
    csvwriter.writerow(fields)
    for i in range(1,101):
        y = pow(i,2) + log(i/2)
        coord=[i,y]
        csvwriter.writerow(coord)
data = pd.read_csv(csvfile)
plt.plot(data.X_coord,data.Y_coord)
plt.show()