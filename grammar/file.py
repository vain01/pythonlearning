poem = '''
I am Haoliang.
I am finding ...
'''

file = open('poem.txt', 'w')
file.write(poem)
file.close()
file = open('poem.txt', 'r')
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end='')
file.close()
