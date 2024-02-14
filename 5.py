import csv

a = []

table = {}
with open('songs.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    for s in reader.reader:
        a.append(s)
    del a[0]
used_songs = []
for s in a:
    name, song = s[1], s[2]
    if song in used_songs:
        continue
    used_songs.append(song)
    if name in table.keys():
        table[name] += 1
    else:
        table[name] = 1
res = []
for t in table:
    res.append([t, table[t]])
res.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    print(f'{res[i][0]} выпустил {res[i][1]} песен.')