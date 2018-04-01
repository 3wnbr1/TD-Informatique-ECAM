def factorial(n):
    """returns factorial of integrer"""
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def exponential(x,prec):
    """returns exponential of x with prescision"""
    from math import exp
    ex = 0
    i = 0
    while abs(ex-exp(x))>prec:
        ex += x**i/factorial(i)
        i+=1
    return ex

print(exponential(12,0.0001))
