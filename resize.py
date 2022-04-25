from PIL import Image
from os import listdir, mkdir
from os.path import exists


target = (256, 256)
dir = 'testdata/yebi'
for fname in listdir(dir):
    img = Image.open(dir + '/' + fname)
    img = img.resize(target, Image.ANTIALIAS)
    if not exists(dir + '_resized/'):
        mkdir(dir + '_resized/')
    img.save(dir + '_resized/' + fname)
