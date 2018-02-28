x = 50


def func(x):
    print('global x is', x)
    x = 2
    print('local x is', x)


func(x)
print('global x is still', x)
