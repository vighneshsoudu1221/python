"""def outer():
    x=10
    def inner():
        return x
    return inner()
of=outer()
print(of)"""
"""
def outer():
    x=10
    def inner():
        return x
    return inner
of = outer()
print(of())
"""
#Create outer() with a variable x = 50. Inside it, create inner() that returns x. Return inner,
#store the returned function in f, and print the result of calling f().
"""
def outer():
    x=50
    def inner():
        return x
    return inner
f=outer()
print(f())
"""
#Create outer(start) with an inner function that adds 10 to start and returns the result.
#Return the inner function. Then create f = outer(5) and print f().
"""def outer(start):
    def inner():
        result=start+10
        return result
    return inner
of=outer(5)
print(of())"""
# counter 
"""
def counter():
    count=0
    def inner():
        nonlocal count
        count=count+1
        return count
    return inner
oc=counter()
print(oc())
print(oc())
print(oc())"""

#Can you write a function called multiply that takes two numbers and returns their product?
#Just write the function yourself.
"""def multiply(a,b):
    result=a*b
    return result
def calculate(func):
    return func(3, 5)
res=calculate(multiply)
print(res)"""

def rat(fun):
   def loppar():
       print("*"*20)
       fun()
       print("*"*20)
   return loppar 
@rat   
def let():
    print("cat")
let()  
