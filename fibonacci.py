"""Fibonacci module — three functions to fix, and one to extend.

Read each docstring carefully. Then run main.py to see what values
the functions should return.
"""


def fib(n):
    """Return the nth Fibonacci number.

    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)  for n >= 2

    Examples:
        fib(0)  -> 0
        fib(1)  -> 1
        fib(2)  -> 1
        fib(7)  -> 13
        fib(10) -> 55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def fib_sequence(n):
    """Return the first n Fibonacci numbers as a list.

    Examples:
        fib_sequence(0) -> []
        fib_sequence(1) -> [0]
        fib_sequence(5) -> [0, 1, 1, 2, 3]
        fib_sequence(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-1])
    return seq


def golden_ratio_approx(n):
    """Approximate the golden ratio using consecutive Fibonacci numbers.

    The ratio F(n+1) / F(n) converges to phi (the golden ratio):
        phi = (1 + sqrt(5)) / 2  ~=  1.6180339887...

    Larger n gives a better approximation.

    Examples:
        golden_ratio_approx(20) ~= 1.6180339
        golden_ratio_approx(30) ~= 1.6180339887
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    return fib(n) / fib(n + 1)
