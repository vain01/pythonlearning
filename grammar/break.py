number = 23
running = True
while running:
    guess = int(input('Enter your number:'))
    if guess == number:
        print('你猜中了')
        break
    elif guess > number:
        print('你猜的大了')
    else:
        print('你猜的小了')
else:
    print('循环结束')
print('结束')
