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
# 查看所有的字典中的key
for name in ab.keys():
    print(name)
# 查看所有的字典中的值
for mail in ab.values():
    print(mail)
# 查看字典中是否存在某个key
if 'aabo' in ab:
    print(ab['aabo'])

