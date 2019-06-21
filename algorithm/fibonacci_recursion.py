known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = result
    return result


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
