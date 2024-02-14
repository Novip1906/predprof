import csv
from datetime import datetime

def get_data():
    """
    This function is used for getting data from songs.csv file
    :return:
    """
    a = []
    with open('songs.csv') as file:
        # print(file.read())
        reader = csv.DictReader(file, delimiter=';')
        for s in reader.reader:
            a.append(s)
        del a[0]
    return a

def process_songs():
    """
    This function is used for process data like in условие
    :return:
    """
    a = get_data()
    d0 = '01.01.2002'
    d = '12.05.2023'
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
    return res

with open('songs_new.csv', 'w') as file:
    rs = 'streams;artist_name;track_name;date\n'
    for s in process_songs():
        rs += ';'.join(s) + '\n'
    file.write(rs)