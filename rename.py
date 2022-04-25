from os import listdir, rename
# from random import randint

dirs = ('testcut/original/',)
for dir in dirs:
    i = 0
    for f in listdir(dir):
        rename(dir + f, f'{dir}{i:>02}.jpg')
        i += 1

