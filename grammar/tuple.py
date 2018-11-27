# 元组
zoo = ('python', 'elephant', 'penguin')
# zoo = 'python', 'elephant', 'penguin' #元组声明并赋值时，这个语句和上句一样
print('Number of animals of the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('All animals in the new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo) + len(zoo) - 1)

# 空元组
empty_tuple = ()
# 一个元素的元组,注意逗号以区分修改运算优先级的括号
one_tuple = (2,)

name = 'ab'
name2 = ('ab',)
name3 = 'ab',
print(name)
print(name2)
print(name3)
print(name[0])
print(name2[0])
print(name3[0])
# 下面是输出
# ab
# ('ab',)
# ('ab',)
# a
# ab
# ab


# 元组的比较:第一个相同,比较第二个一次类推
print((0, 1, 2) < (0, 3, 4))  # True
print((0, 1, 20000) < (0, 3, 4))  # True
