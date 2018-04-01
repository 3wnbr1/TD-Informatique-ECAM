def factorial(n):
    """returns factorial of integrer"""
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

file = open('factorials.txt','w')

for i in range(100):
    file.write(str(i)+"! = "+str(factorial(i))+'\n')

file.close()
