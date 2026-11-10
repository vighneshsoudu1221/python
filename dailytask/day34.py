#1 Write a Python program using a closure where the outer function takes a number n and the inner function takes
#another number x and returns n + x.
#Input: n = 10 x = 5
#Output: 15
"""
def bigger(n):
    def inner(x):
      return n+x
    return inner
res=bigger(10)
print(res(6))
"""
#2 Create a closure counter() that maintains a count. Every time the inner function is called,
#it should increase the count by 1 and return the updated count.
#Input: c = counter() print(c()) print(c()) print(c())
#Output: 1 2 3
"""def cat():
    c=0
    def loppala():
        nonlocal c
        c=c+1
        return c
    return loppala
ci=cat()
print(ci())
print(ci())
print(ci())"""
#3 Write a closure that stores a number and provides an inner function to increase the stored number by a given value.
#Input: c = create_counter(10) print(c(5)) print(c(3)) print(c(7))
#Output: 15 18 25
"""def add(n):
    def loppala(x):
        nonlocal n
        n=n+x
        return n
        
    return loppala
ci=add(10)
print(ci(5))
print(ci(3))
print(ci(7))"""
#4 Write a function calculator(n) that returns three inner functions: add(x) → adds x to n sub(x)
#→ subtracts x from n mul(x) → multiplies n by x All three functions must access the same variable n from
#the outer function.
#Input: add, sub, mul = calculator(1
def calculator(n):
    def add(x):
        return n+x
    def sub(b):
        return n-b
    def mul(y):
        return n-y
    return{"add":add,"sub":sub,"mul":mul}
res=calculator(10)
print(res["add"](5))
print(res["sub"](5))
print(res["mul"](5))
