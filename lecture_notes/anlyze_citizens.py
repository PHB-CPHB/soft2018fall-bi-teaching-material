import csv
import numpy as np

file_name = 'befkbhalderstatkode.csv'
path_to_file = 'befkbhalderstatkode.csv'

# with open(file_name) as fp:
#    reader = csv.reader(fp)
#    header_row = next(reader)
#    rows = [row for row in reader]
# print(rows)

data = np.genfromtxt(path_to_file, delimiter=',', dtype=np.uint)
data = data[1:]

print(data[:,3])
print("---------------------------------------")
print(np.sum(data[:,-1]))
print("---------------------------------------")
print((data[:,0] == 2015) & data([:,3] == 5134))
print("---------------------------------------")
print(np.sumdata([(data[:,0] == 2015) & (data([:,3] == 5134))][:,-1]))