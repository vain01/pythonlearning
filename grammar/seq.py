# 序列
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'haoliang'
print(shoplist)
print(name)

# 索引
print('Item 0 is', shoplist[0])
print('Item 0 is', shoplist[1])
print('Item 0 is', shoplist[2])
print('Item 0 is', shoplist[3])
print('Item 0 is', shoplist[-1])
print('Item 0 is', shoplist[-2])
print('Item 0 is', shoplist[-3])
print('Item 0 is', shoplist[-4])
print('Character 0 is', name[0])

# 切片列表
print('Item 1 to 3 is', shoplist[1:3])  # 包含初值，不包含终值
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# print('Item start to end is', shoplist[0: len(shoplist)])  #这行和上行是一样的输出

# 切片字符串
print('Character 1 to 3 is', name[1:3])  # 包含初值，不包含终值
print('Character 2 to end is', name[2:])
print('Character 1 to -1 is', name[1:-1])
print('Character start to end is', name[:])

# 切片步长
print(name[::1])
print(name[::2])
print(name[::-1])
