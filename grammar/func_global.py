x = 50


def func():
    global x

    print('global x is', x)
    x = 2
    print('internal x is', x)


func()
print('x is', x)
