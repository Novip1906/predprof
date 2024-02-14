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
a = get_data()

inp = input('Введите имя артиста: ')
while len(inp) > 0 and inp != '0':
    for s in a:
        if inp.strip() in s[1].split()[0] or inp.strip() == s[1]:
            print(f'У {s[1]} найдена песня: {s[2]}')
            break
    else:
        print('К сожалению, ничего не удалось найти')
    inp = input('Введите имя артиста: ')



