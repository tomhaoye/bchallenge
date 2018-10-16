#!/usr/bin/python

from PIL import Image

img = Image.open('challenge.png')
content = img.load()
y = 310
size = img.size[0]

g_string = []
for i in range(size):
    g_string.append(str(bin(content[i, y][0])[-1]))
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

res = []
for x in range(len(g_channel)):
    color = int(g_channel[x]) ^ int(al_channel[x])
    res.append(str(color))

print hex(int(''.join(res), 2))[2:-1].decode('hex')
