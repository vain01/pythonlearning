running = True
while running:
    s = input('输入字符串:')
    if s == 'exit':
        running = False
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('输入的长度足够')
else:
    print('循环结束')
print('结束')
