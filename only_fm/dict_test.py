d = dict()
d['hao'] = 3
d['liang'] = 4
d['qi'] = 5

print(d)
poped = d.pop('liang')
print(poped)
print(d)
print(d['hao'])
print(d.get('haoNotExist', 8))

print(lambda d: d[0])
print(d)
print(type(d))

print("##################A##################")
A = sorted(d.items(), key=lambda d: d[1], reverse=False)
print(A)
print(type(A))
d = dict(A)
print(d)
print("##################B##################")
B = sorted(d.values(), reverse=True)
print(B)
print(type(B))
print(B[:10])
