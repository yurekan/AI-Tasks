import csv
import pandas as pd
from matplotlib import pyplot as plt

csvfile = 'coordinates.csv'
with open(csvfile,'w',newline='') as fobj:
    fields = ['X_coord','Y_coord']
    csvwriter = csv.writer(fobj)
    csvwriter.writerow(fields)
    choice = int(input("Enter the no of coordinates : "))
    for i in range(choice):
        x = int(input("Enter the x co-ordinate : "))
        y = int(input("Enter the y co-ordinate : "))
        coord = [x,y]
        csvwriter.writerow(coord)
data = pd.read_csv(csvfile)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(data.X_coord,data.Y_coord)
plt.show()

