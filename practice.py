import math 

def add(x,y):
  return x + y

def subtract(x,y):
  return x - y

def mulitply(x,y):
  return x * y

def divide(x,y):
  if y == 0:
    return "Error: cant divide by zero"
  else:
    return x/y

def modulo(x,y):
  return x & y

def int_divide(x,y):
   if y == 0:
    return "Error: cant divide by zero"
  else:
    return x//y

def exponent(x,y):
  return x ** y


def sq_root(x):
  if x < 0:
    return "Error: cant square root a neg number"
  else math.sqrt(x)

def main():
  history = []
  last_result = None
  print("Welcome to your personal calculator")

  while True:
    print("Menu: ")
    print("option 1: Do some calculations. ")
    print("option 2: Show calculation history. ")
    print("option 3: Exit ")
    choice = input(print("Choose one of the options above: "))

    if choice == "1":
      x_input = input("Enter your first number or('ans' to use your last result):")
      if x_input.lower == 'ans':
        if last_result is None:
          print(" There is no previous answer.")
        continue
        x = last_result
      else:
        try:
          x = float(x_input)
        except ValueError:
          print("invalid input try again.")
          continue

      operator = input("Enter an operator ( +, -, *, **, %, /, //, sq_root): ")

      # for sqrt we only need 1 number 
      if operator == "sqrt":
        result = sq_root(x)
        history.append(f"√{x} = {result}")
        print(f"(result = {result}")
        last_result = result
        continue 

      y_input = input("Enter your second number or('ans' to use your last result):")
      if y_input.lower == 'ans':
        if last_result is None:
          print(" There is no previous answer.")
        continue
        y = last_result
      else:
        try:
          y = float(x_input)
        except ValueError:
          print("invalid input try again.")
          continue

      if operator == "+":
        result = add(x,y)
      elif operator == "-":
        result = subtract(x,y)
      elif operator == "/":
        result = divide(x,y)
      elif operator == "*":
        result = multiply(x,y)
      elif operator == "**":
        result = exponent(x,y)
      elif operator == "//":
        result = int_divide(x,y)
      elif operator == "%":
        result = modulo(x,y)
      else:
        print("invalid input please try again. ")
        continue
      history.append(f"{x} {operator} {y} = {result} ")
      last_result = result
      print(f"Result = {result}")
     
      elif choice == "2":
        if not history:
          print("theres no history yet")
        else:
          print("Calculation History: ")
          for item in history:
            print(item)
          print()

      elif choice == "3":
        print("Exiting the Calculator application. See you soon. ")
        break
        else:
          print("Invalid choice pleasse try again.")

main()


          
      
          
          


      


    
        
          
        
          
          


