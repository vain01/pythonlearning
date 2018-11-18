number = 23
guess = int(input("Enter your number:"))
if guess == number:
    print('你猜中了')
elif guess < number:
    print('你猜的小了')
else:
    print('你猜的打了')
print('结束')
