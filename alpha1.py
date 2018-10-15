#!/usr/bin/python

from PIL import Image

img = Image.open('alpha1.bmp')
img = img.convert('L')
content = img.load()
y = 310

string = []
for i in range(2800):
    if content[i, y] == 0:
        string.append(str(1))
    else:
        string.append(str(0))
print(hex(int(''.join(string), 2))[2:-1].decode('hex').decode('base64'))

img.close()

