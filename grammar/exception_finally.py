import time

try:
    f = open('poem.txt', 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(1)
except KeyboardInterrupt:
    print('You canelled the reading from the file')
except:
    print('Something error')
finally:
    f.close()
    print('file was closed')
