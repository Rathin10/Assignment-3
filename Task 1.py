def factorial(x) :
    if x<2 :
        return 1
    else :
        return x*factorial(x-1)
n = int(input('Enter a number:'))
result = factorial(n)
print('Factorial of',n,'is:',result)