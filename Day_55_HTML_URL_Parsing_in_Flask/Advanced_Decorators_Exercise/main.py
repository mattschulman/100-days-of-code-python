inputs = eval(input())
# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
  def wrapper(*args):
    print(f"Function: {function.__name__}")
    print(f"Args: {args}")
    print(f"Output: {function(args[0], args[1], args[2])} ")
  return wrapper
    

# TODO: Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])

