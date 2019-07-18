import copy


class Point(object):
    """
    2-D point
    """


class Rectangle():
    """

    """


def grow_rectangle(rect, width, height):
    rect.width += width
    rect.height += height


def find_center(rect):
    center = Point()
    center.x = rect.corner.x + rect.width / 2
    center.y = rect.corner.y + rect.height / 2
    return center


def print_point(p):
    print('(%d,%g)' % (p.x, p.y))


r = Rectangle()
r.width = 8
r.height = 10
r.corner = Point()
r.corner.x = 0
r.corner.y = 0

c = find_center(r)
print_point(c)

grow_rectangle(r, 50, 100)
c = find_center(r)
print_point(c)

print('############  copy/deepcopy  ############')
box = Rectangle()
box.width = 10
box.height = 20
box.corner = Point()
box.corner.x = 0
box.corner.y = 0

box_copied = copy.copy(box)
print(box is box_copied)
print(box.corner is box_copied.corner)

box_deep_copied = copy.deepcopy(box)
print(box is box_deep_copied)
print(box.corner is box_deep_copied.corner)

