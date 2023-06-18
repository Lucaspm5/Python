def fibonacci(k):
    n = [0, 1]
    for i in range(2, k+1):
        n.append(n[i-1] + n[i-2])
    return n
cases = int(input())
for _ in range(cases):
    k = int(input())
    fib = fibonacci(k)
    print(f'Fib({k}) = {fib[k]}')