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

def write_to_files(rus: set, foreign: set):
    """
    this functiono is used for writings data to .txt files
    :param rus: russian singers
    :param foreign: foreings singers
    :return:
    """
    with open('russian_artists.txt', 'w') as f:
        f.write('\n'.join(list(rus)))
    with open('foreign_artists.txt', 'w') as f:
        f.write('\n'.join(list(foreign)))


a = get_data()

def russian_or_foreign(arr: list):
    """
    this function is used for singers division
    :param arr: array of singers
    :return:
    """
    ru = 'йцукенгшщзхъфывапролджэячсмитьбю'
    russian_artists, foreign_artists = set(), set()
    for s in arr:
        for l in s[1]:
            if l in ru or l in ru.upper():
                russian_artists.add(s[1])
                break
        else:
            foreign_artists.add(s[1])
    return russian_artists, foreign_artists
russian_artists, foreign_artists = russian_or_foreign(a)

print(f'Количество российских исполнителей: {len(russian_artists)} (https://drive.google.com/file/d/1wK_FbEUID_5Y_tHWNveiqhc7butER22Z/view?usp=drive_link)')
print(f'Количество иностранных исполнителей: {len(foreign_artists)} (https://drive.google.com/file/d/12p4X5JYqaA5rloR4u9mXP0Hl6_CyNAJD/view?usp=drive_link) ')

write_to_files(russian_artists, foreign_artists)