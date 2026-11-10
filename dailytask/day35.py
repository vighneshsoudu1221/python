#1 Write a Python program using a decorator to display a message before and after executing the function.
#Input: hello batch 89
#Output: Function Started hello batch 89 Function Ended
"""
def dec(fun):
    def inner():
        print("function started",end="")
        fun()
        print("function ended",)
    return inner()
@dec
def display():
    print("hello batch 89")
"""    

#2 Write a Python program using a decorator to count the number of times a function is called.
#Input: hello() hello() hello()
#Output: Call 1: hello Call 2: hello Call 3: hello
"""def out(fun):
    def inner():
        print("call")
        fun()

    return inner()
@out
def display():
    print("hello")
display()
display()
display()"""
#3 Write a Python program using a decorator to display a message before adding two numbers.
#Input: n1 = 10 n2 = 20
#Output: Adding 10 and 20 Sum = 30

