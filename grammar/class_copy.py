import copy


class Point:
    pass


class Rectangle:
    pass


rect = Rectangle()
rect.width = 50
rect.height = 100
rect.corner = Point()
rect.corner.x = 0
rect.corner.y = 0

box = copy.copy(rect)
print(box is rect)
print(box == rect)
print(box.corner is rect.corner)

box_deep_copy = copy.deepcopy(rect)
print(box_deep_copy is rect)
print(box_deep_copy == rect)
print(box_deep_copy.corner is rect.corner)
