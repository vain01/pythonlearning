def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


ta = tuple('1abc')
tb = list('abcde')
print(has_match(ta, tb))