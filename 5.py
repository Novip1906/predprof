import csv

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

def get_songs_counts(arr: list):
    """
    this func is used for get singers songs count
    :param arr: array of songs
    :return: array of singers and their songs counts
    """
    table = {}
    used_songs = []
    for s in arr:
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
    return res

a = get_data()
res = get_songs_counts(a)
for i in range(10):
    print(f'{res[i][0]} выпустил {res[i][1]} песен.')