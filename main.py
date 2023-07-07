word = 'hello'
steps = 3
code = ''
for i in word:
    if (ord(i) + steps) >= 123:
        code += chr(ord(i) + steps - 26)
    else:
        code += chr(ord(i) + steps)

print(code)
1.13