import art

def add(n1, n2):
 return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  print("\n")
  for symbol in operations:
    print(symbol)
  print("\n")
  
  should_continue = True
  
  while should_continue:
    operator_symbol = input("Pick an operation: ")
    print("\n")
    num2 = float(input("What's the next number?: ")) 
    function = operations[operator_symbol]  
    answer = function(num1,num2)  
    print(f"\n{num1} {operator_symbol} {num2} = {answer}")  
    continue_result = input(f"\nType 'y' to continue caluclating with {answer}, 'n' to start a new calculation, or 'x' to exit: ").lower()
    if continue_result == 'y':
      num1 = answer
    elif continue_result == 'n':
      print("\n")
      should_continue = False
      calculator()
    else:
      should_continue = False

calculator()