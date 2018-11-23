def gcd(p, q):
    if q == 0:
        return p
    remainder = p % q
    return gcd(q, remainder)


print(gcd(8, 0))
print(gcd(0, 8))
print(gcd(8, 8))
print(gcd(8, 4))
print(gcd(5, 3))
