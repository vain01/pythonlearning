def print_max(a, b):
    if a > b:
        print(a, 'is max')
    elif a == b:
        print(a, 'is equal', b)
    else:
        print(b, 'is max')


print_max(3, 4)
print_max(7, 5)
print_max(7, 7)
