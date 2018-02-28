def func(initial, *numbers, vegetables):
    count = initial
    for num in numbers:
        count += num
    count += vegetables
    return count


print(func(5, 1, 2, vegetables=2))
# print(func(5, 1, 2, 2))   #这行是语法错误的，keyword only参数必须使用x=xxx样式
