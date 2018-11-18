listArray = [1, 3, 5, 2, 6, 4, 5, 6, 6, 69]

result = {}
for i in listArray:
    if result.get(i):
        result[i] += 1
    else:
        result[i] = 1

print(result)
