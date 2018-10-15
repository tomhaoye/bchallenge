#!/usr/bin/python

string = '511B2033232841053022B0FE52ED0F7A165B52C7E75112F656FC4B'

key = '20181002'
hexadecimal = '0123456789ABCDEF'
answer = ''

for i in range(len(string)):
    string_char = string[i]
    key_char = key[i % len(key)]

    string_index = hexadecimal.index(string_char)
    key_index = hexadecimal.index(key_char)

    new_char_index = (string_index - key_index) % len(hexadecimal)
    answer += hexadecimal[new_char_index]

print(answer)

with open('english.txt') as handle:
    contents = [x.strip() for x in handle.readlines()]
    for j in range(18, 52, 3):
        print(contents[int(answer[j:j + 3], 16) - 1])
