def fibonacci(n):
    """Loop n-1 times and return n unless n=0 or n=1."""
    if n < 0:
        print("Not in scope of assignment, please provide positive number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

# Enter n in function call
fibonacci()


def lucas(x):
    """Loop x-1 times and return x unless x < 0."""
    if x < 0:
        print("Not in scope of assignment, please provide positive number.")
    else:
        c, d = 2, 1
        for i in range(x - 1):
            c, d = d, c + d
        return c

# Enter x in function call
lucas()


def sum_series(y, e=0, f=1):
    """Loop y-1 times with default parameters e, f."""
    if y < 0:
        print("Not in scope of assignment, please provide positive number.")
    elif y == 0:
        return 0
    elif y == 1:
        return 1
    else:
        for i in range(y - 1):
            e, f = f, e + f
    return e

# Enter y, e, f in function call.
sum_series()


if __name__ == 'fibonacci':
    # The 3rd number of fibonacci = 1
    assert fibonacci(3) == 1

if __name__ == 'lucas':
    # The 4th number of lucas = 5
    assert lucas(4) == 5

if __name__ == 'sum_series':
    # The 4th number of sum_series with parameters 2,3 = 8
    assert sum_series(4, 2, 3) == 8
