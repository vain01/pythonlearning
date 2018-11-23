def factorial(natural_num):
    if natural_num <= 1:
        return 1
    return natural_num * factorial(natural_num - 1)


print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
