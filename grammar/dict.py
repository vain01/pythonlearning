ab = {
    'aabo': 'aabo@163.com',
    'haoliang': 'haolaing@myqifa.com',
    'hl': 'haoliang@ifurion.com'
}

print("aabo's mail is", ab['aabo'])
print(ab)

# 删除一项
del ab['hl']
print('Someone is deleted from ab, new ab is', ab)
print('new ab length is', len(ab))

# 查看所有的字典中条目
for name, mail in ab.items():
    print(name, mail)

# 添加一项
ab['yufeng'] = 'chenyufeng@ifurion.com'
print(ab['yufeng'])
print(ab.get('yufeng'))

if 'xx' not in ab:
    ab['xx'] = 'xx@ifurion.com'
print(ab.get('xx'))

# 查看所有的字典中的key
for name in ab.keys():
    print(name)

print()

for key in ab:
    print(key)

# 查看所有的字典中的值
for mail in ab.values():
    print(mail)

# 查看字典中是否存在某个key
if 'aabo' in ab:
    print(ab['aabo'])

# 返回元组列表
print(ab.items())

# 生产简单字典
simple_dict = dict(zip('abc', range(3)))
print(simple_dict)

# 使用元组做为dict的键很常见
last = 'hao'
first = 'liang'
mobile = '13482892312'
directory = {}
directory[last, first] = mobile
last = 'hao'
first = 'li'
mobile = '13482892319'
directory[last, first] = mobile
print(directory)  # {('hao', 'liang'): '13482892312'}
for last, first in directory:
    print(last, first, directory[last, first])
