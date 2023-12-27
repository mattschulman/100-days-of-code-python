## ********Day 54 Start**********
## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(multiply, 2, 3)
# print(result)

# #should be 6

# result = calculate(add, 2, 3)
# print(result)

# #should be 5

# ## Functions can be nested in other functions.  nested_function() is not callable outside of  outer_function()

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()

# outer_function()

# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# inner_function = outer_function()
# inner_function()


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

# #With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

say_bye()

# #Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

