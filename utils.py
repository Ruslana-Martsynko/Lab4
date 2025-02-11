def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


