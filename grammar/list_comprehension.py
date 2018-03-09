# 从一个列表中导出变换的另外一个数组
list_one = [2, 3, 8]
print(list_one)
list_two = [2 * i for i in list_one if i > 2]
print(list_two)
