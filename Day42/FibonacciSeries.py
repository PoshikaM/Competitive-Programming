def fibonacci_series(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

terms = 10
print(f"Fibonacci series (first {terms} terms): {fibonacci_series(terms)}")