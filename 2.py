import csv
from datetime import datetime
a = []
start_date = datetime.strptime('01.01.1900', '%d.%m.%Y')
with open('songs.csv') as file:
    #print(file.read())
    reader = csv.DictReader(file, delimiter=';')
    for s in reader.reader:
        a.append(s)
    del a[0]
for i in range(len(a)):
    d = datetime.strptime(a[i][-1], '%d.%m.%Y')
    a[i].append((d - start_date).days)
for i in range(len(a) - 1):
    mx = 0
    mxi = 0
    for j in range(i, len(a)):
        if a[j][-1] > mx:
            mx = a[j][-1]
            mxi = j
    a[i], a[mxi] = a[mxi], a[i]
a.reverse()
for i in range(5):
    print(f'{i + 1} {a[i][2]}, {a[i][1]}, {a[i][3]}')
