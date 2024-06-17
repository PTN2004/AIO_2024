def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def sin(x, n):
    result = x
    for i in range(1, n+1):
        result += (-1)**i * ((x**(2*i + 1)) / factorial(2*i + 1))
    return result


def cos(x, n):
    result = 1
    for i in range(1, n+1):
        result += (-1)**i * ((x**(2 * i)) / factorial(2 * i))
    return result


def sinh(x, n):
    result = x
    for i in range(1, n+1):
        result += (x**(2 * i + 1)) / factorial(2 * i + 1)
    return result


def cosh(x, n):
    result = 1
    for i in range(1, n+1):
        result += (x**(2 * i)) / factorial(2 * i)
    return result


print(sin(3.14, 10))
print(cos(3.14, 10))
print(sinh(3.14, 10))
print(cosh(3.14, 10))
