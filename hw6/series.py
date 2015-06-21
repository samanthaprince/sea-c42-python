def fibonacci(n):
    """Loop n-1 times and return n unless n=0 or n=1."""
    if n == 0:
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
