# 函数返回两个值--使用元组
def get_error_detail():
    return (2, "error_detail")


err_num, err_detail = get_error_detail()
print(err_num)
print(err_detail)

# 第一传给第一个参数，后面其他传给第二个参数--使用列表
a, *b = [1, 3, 4, 5]
print(a)
print(b)

# 最快方式交换两个变量值
a = 5
b = 8
a, b = b, a
print(a)
print(b)

# 链式比较操作
# https://foofish.net/idiomatic_part2.html
age = 18
if 10 < age < 30:
    print('Young man.')

# 单语句块
flag = True
if flag: print('Yes')

# 三元运算符
male = False
sex = '男' if male else '女'
print(sex)
gender = 'male'
text = '男' if gender == 'male' else '女'
print(text)


