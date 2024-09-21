# string formatting in python

name= "Saugat"
age = 22
normalText="My name is {} and I am {} years old"
text = f"My name is {name} and I am {age} years old"
price = 33.9902
print(text)

print(normalText.format(name,age))
print(f"the price of apple is {price: .2f}")
print(f"{3*3}")
print(type(f"{3*3}"))

# Doc strings
'''
Doc strings are the string literals that appear right after the defination of a function method, class or module
'''

def add(a,b):
    '''
    takes two number and perform their addition
    '''
    print(a+b)
add(5,4)
print(add.__doc__)

#Recursion oin python
#It is simply a function inside a function 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))
print(factorial(6))
print(factorial(4))

#fibonacci number using Recursion method

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))
print(fibonacci(10))
print(fibonacci(11))