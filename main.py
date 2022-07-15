from art import logo

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
  "/": divide,
}

#turns whole action into its own function
def calculator():
  print(logo)
  #set as float to allow decimals
  num1 = float(input("What's the first number?: "))
  #prints all key options in dictionary
  for symbol in operations:
    print(symbol)
  #flag for while loop. sets continue to true
  should_continue = True

  #starts the loop back here so long as continue is true
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    #transfers operations and above functions all into one function so no need for crazy if statements I tried...
    calculation_function = operations[operation_symbol]
    
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.") == "y":
      #sets num1 to answer variable so can continue loop
      num1 = answer
    else:
      #ends loop. VERY IMPORTANT BEFORE NEXT STEP otherwise endless loop
      should_continue = False
      #called recursion. recalls the whole function from beginning so can start over
      calculator()

#original actual call of function
calculator()