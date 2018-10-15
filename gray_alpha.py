#!/usr/bin/python

from PIL import Image

img = Image.open('gray.bmp')
content = img.load()
y = 310
size = img.size[0]

g_string = []
for i in range(size):
    if content[i, y][0] == 0:
        g_string.append(str(1))
    else:
        g_string.append(str(0))

g_channel = ''.join(g_string)
img.close()

img = Image.open('alpha.bmp')
content = img.load()
y = 310
size = img.size[0]

a_string = []
for i in range(size):
    if content[i, y][0] == 0:
        a_string.append(str(1))
    else:
        a_string.append(str(0))

al_channel = ''.join(a_string)
img.close()

img = Image.open('alpha1.bmp')
content = img.load()
y = 310
size = img.size[0]
a_1_string = []
for i in range(size):
    if content[i, y][0] == 0:
        a_1_string.append(str(1))
    else:
        a_1_string.append(str(0))

al_1_channel = ''.join(a_1_string)
img.close()

res = []
for x in range(len(g_channel)):
    color = int(al_channel[x]) | int(al_1_channel[x]) ^ int(g_channel[x])
    res.append(str(color))

print hex(int(''.join(res), 2))[2:-1].decode('hex')
