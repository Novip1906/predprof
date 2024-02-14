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

a = get_data()

def data_sort(arr: list):
    """
    This function is used for sorting songs
    :param arr: array of songs and artists
    :return:
    """
    start_date = datetime.strptime('01.01.1900', '%d.%m.%Y')
    for i in range(len(arr)):
        d = datetime.strptime(a[i][-1], '%d.%m.%Y')
        arr[i].append((d - start_date).days)
    for i in range(len(arr) - 1):
        mx = 0
        mxi = 0
        for j in range(i, len(arr)):
            if arr[j][-1] > mx:
                mx = arr[j][-1]
                mxi = j
        arr[i], arr[mxi] = arr[mxi], arr[i]
    arr.reverse()
    return arr
a = data_sort(a)
for i in range(5):
    print(f'{i + 1} {a[i][2]}, {a[i][1]}, {a[i][3]}')
