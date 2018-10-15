#!/usr/bin/python

from PIL import Image

img = Image.open('challenge.png')
content = img.load()
y = 310
size = img.size[0]

c_string = []
for i in range(size):
    c_string.append(str(bin(content[i, y][0])[-1]))

or_channel = ''.join(c_string)[:2800]
img.close()

img = Image.open('alpha1.bmp')
img = img.convert('L')
content = img.load()
y = 310
size = img.size[0]

a_string = []
for i in range(size):
    if content[i, y] == 0:
        a_string.append(str(1))
    else:
        a_string.append(str(0))

al_channel = ''.join(a_string)

img.close()

res = []
for x in range(len(or_channel)):
    new_channel = int(or_channel[x]) ^ int(al_channel[x])
    res.append(str(new_channel))

final = ''.join(res)
final = final.replace('1', '2')
final = final.replace('0', '1')
final = final.replace('2', '0')
print(hex(int(final, 2))[2:-1].decode('hex'))
