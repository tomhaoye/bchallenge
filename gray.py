#!/usr/bin/python

from PIL import Image

img = Image.open('gray.bmp')
img = img.convert('L')
content = img.load()
y = 310
size = img.size[0]

string = []
for i in range(size):
    if content[i, y] == 0:
        string.append(str(1))
    else:
        string.append(str(0))
print(hex(int(''.join(string), 2))[2:-1])
img.close()
