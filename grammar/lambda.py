def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)
print(twice('Hao'))
print(twice(2))

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
print(points)
# points.sort(lambda a, b: cmp(a['x'], b['x']))
