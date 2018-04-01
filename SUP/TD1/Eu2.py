def fib(n):
    ls = [1,1]
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        ls.append(a+b)
    return ls

print(fib(4000000))
