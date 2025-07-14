import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: divide by zero"
    return x / y

def exponent(x, y):
    return x ** y

def modulo(x, y):
    return x % y

def int_divide(x, y):
    if y == 0:
        return "Error: divide by zero"
    return x // y

def square_root(x):
    if x < 0:
        return "Error: can't sqrt negative number"
    return math.sqrt(x)

def main():
    history = []
    last_result = None

    print("Welcome to your upgraded command line calculator!\n")

    while True:
        print("Menu:")
        print("1. Perform Calculation")
        print("2. View History")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            x_input = input("Enter first number (or 'ans' to use last result): ")
            if x_input.lower() == "q":
                break
            if x_input.lower() == "ans":
                if last_result is None:
                    print("No previous result available.\n")
                    continue
                x = last_result
            else:
                try:
                    x = float(x_input)
                except ValueError:
                    print("Invalid input. Try again.\n")
                    continue

            operator = input("Enter operator (+, -, *, /, **, %, //, sqrt): ")

            # For sqrt, we only need one input
            if operator == "sqrt":
                result = square_root(x)
                history.append(f"√{x} = {result}")
                print(f"Result: {result}\n")
                last_result = result
                continue

            y_input = input("Enter second number (or 'ans' to use last result): ")
            if y_input.lower() == "ans":
                if last_result is None:
                    print("No previous result available.\n")
                    continue
                y = last_result
            else:
                try:
                    y = float(y_input)
                except ValueError:
                    print("Invalid input. Try again.\n")
                    continue

            if operator == "+":
                result = add(x, y)
            elif operator == "-":
                result = subtract(x, y)
            elif operator == "*":
                result = multiply(x, y)
            elif operator == "/":
                result = divide(x, y)
            elif operator == "**":
                result = exponent(x, y)
            elif operator == "%":
                result = modulo(x, y)
            elif operator == "//":
                result = int_divide(x, y)
            else:
                print("Invalid operator. Try again.\n")
                continue

            history.append(f"{x} {operator} {y} = {result}")
            last_result = result
            print(f"Result: {result}\n")

        elif choice == "2":
            if not history:
                print("No history yet.\n")
            else:
                print("\nCalculation History:")
                for item in history:
                    print(item)
                print()
        elif choice == "3":
            print("Exiting calculator. Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.\n")

main()

    
                
              
                
  
  

