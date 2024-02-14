import csv
from datetime import datetime
a = []
d0 = '01.01.2002'
d = '12.05.2023'
with open('songs.csv') as file:
    #print(file.read())
    reader = csv.DictReader(file, delimiter=';')
    for s in reader.reader:
        a.append(s)
    del a[0]
res = []
for i in range(len(a)):
    d1 = datetime.strptime(d, '%d.%m.%Y')
    d00 = datetime.strptime(d0, '%d.%m.%Y')
    d2 = datetime.strptime(a[i][3], '%d.%m.%Y')
    if a[i][0] == '0':
        dl = (d1 - d2).days
        a[i][0] = str(abs(dl // (len(a[i][1]) + len(a[i][2]))) * 10000)
        if d2 > d00:
            continue
    res.append(a[i])

with open('songs_new.csv', 'w') as file:
    rs = 'streams;artist_name;track_name;date\n'
    for s in res:
        rs += ';'.join(s) + '\n'
    file.write(rs)