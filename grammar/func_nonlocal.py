def func_outer():
    x = 2
    print('outer x is', x)

    def func_inner():
        nonlocal x
        x = 888
        print('inner x is', x)

    func_inner()
    print('outer x is', x)


func_outer()
