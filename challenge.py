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


print hex(int(g_channel, 2))[2:-1].decode('hex')
