#!/usr/bin/python

from PIL import Image

img = Image.open('gray.bmp')
content = img.load()
y = 310
size = img.size[0]

gr_string = []
for i in range(size):
    if content[i, y][0] == 0:
        gr_string.append(str(1))
    else:
        gr_string.append(str(0))

gr_channel = ''.join(gr_string)[::-1]
img.close()

print(gr_channel)
# print hex(int(''.join(gr_channel), 2))[2:-1].decode('hex')
