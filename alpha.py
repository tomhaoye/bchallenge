#!/usr/bin/python

from PIL import Image

img = Image.open('alpha.bmp')
content = img.load()
y = 310
size = img.size[0]

string = []
for i in range(size):
    if content[i, y][0] == 0:
        string.append(str(1))
    else:
        string.append(str(0))
channel = ''.join(string)

print(hex(int(channel, 2))[2:-1].decode('hex'))

img.close()
