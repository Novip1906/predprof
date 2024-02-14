import csv

a = []
russian_artists, foreign_artists = set(), set()

with open('songs.csv') as file:
    #print(file.read())
    reader = csv.DictReader(file, delimiter=';')
    for s in reader.reader:
        a.append(s)
    del a[0]
ru = 'йцукенгшщзхъфывапролджэячсмитьбю'

for s in a:
    for l in s[1]:
        if l in ru or l in ru.upper():
            russian_artists.add(s[1])
            break
    else:
        foreign_artists.add(s[1])
print(f'Количество российских исполнителей: {len(russian_artists)} (https://drive.google.com/file/d/1wK_FbEUID_5Y_tHWNveiqhc7butER22Z/view?usp=drive_link)')
print(f'Количество иностранных исполнителей: {len(foreign_artists)} (https://drive.google.com/file/d/12p4X5JYqaA5rloR4u9mXP0Hl6_CyNAJD/view?usp=drive_link) ')
with open('russian_artists.txt', 'w') as f:
    f.write('\n'.join(list(russian_artists)))
with open('foreign_artists.txt', 'w') as f:
    f.write('\n'.join(list(foreign_artists)))