a_list = ['a', 'b', 'c']
print(a_list)
a_list.append(['x', 'y'])
print(a_list)
a_list.extend(['o', 'p'])
print(a_list)
print(len(a_list))
a_list.append('a')
print(a_list)
print(a_list.count('a'))
print(a_list.index('o'))
print(a_list)
a_list.remove('a')
print(a_list)
del a_list[0]
print(a_list)
print(a_list.pop())
print(a_list)
print(a_list.pop(1))
print(a_list)
a_list.insert(1, 'x')
print(a_list)
print('x' in a_list)
