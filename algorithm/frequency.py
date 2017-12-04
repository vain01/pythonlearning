listArray = [1, 3, 5, 2, 6, 4, 5, 6, 6, 69]

map = {}
for i in listArray:
    if map.get(i):
        map[i] += 1
    else:
        map[i] = 1

print(map)
