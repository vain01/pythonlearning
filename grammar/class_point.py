class Point:
    pass


point = Point()
point.x = 2
point.y = 3

print(point.x)

print(hasattr(point, 'x'))

print(hasattr(point, 'z'))
point.z = 4
print(hasattr(point, 'z'))

