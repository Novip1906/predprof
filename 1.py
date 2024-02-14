import csv
from datetime import datetime
a = []
d0 = '01.01.2002'
with open('songs.csv') as file:
    #print(file.read())
    reader = csv.DictReader(file, delimiter=';')
    for s in reader.reader:
        a.append(s)
    del a[0]
for i in range(len(a)):
    if a[i][0] == '0':
        d1 = datetime.strptime(d0, '%d.%m.%Y')
        d2 = datetime.strptime(a[i][3], '%d.%m.%Y')
        dl = (d1 - d2).days
        a[i][0] = str(abs(dl // (len(a[i][1]) + len(a[i][2]))) * 10000)
with open('songs_new.csv', 'w') as file:
    fieldnames=['streams',	'artist_name', 'track_name', 'date']
    rs = 'streams;artist_name;track_name;date\n'
    for s in a:
        rs += ';'.join(s) + '\n'
    file.write(rs)