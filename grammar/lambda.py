def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)
print(twice('Hao'))
print(twice(2))


def cmp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


nums = [3, 4, 5, 6, 9, 1]
nums.sort()
print(nums)
# nums.sort(key=cmp, reverse=False)
# print(nums)

# points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}, {'x': 3, 'y': 5}]
# print(points)
# points.sort(lambda a, b: a['x'] - b['x'])

# persons = [{'name': 'zhang3', 'age': 15}, {'name': 'li4', 'age': 12}]
# print(persons)
# persons.sort(lambda a, b: a['age'] - b['age'])
# print(persons)
