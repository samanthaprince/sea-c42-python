def fibonacci(n):
    """Loop n times and return n unless n=0 or n=1."""
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
