def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):  # fixed typo from mulitply
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

def main():
    print("Welcome to the Command Line Calculator!\n")

    while True:
        try:
            x_input = input("Please enter your first number or type 'q' to quit:\n ")
            if x_input.lower() == 'q':
                print("Exiting Command Line Calculator. See you next time.\n")
                break
            x = float(x_input)
        except ValueError:
            print("Invalid input. Try again.\n")
            continue

        operator = input("Enter operator (+, -, *, /): ")

        try:
            y = float(input("Please enter your second number: \n"))
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        if operator == "+":
            result = add(x, y)
        elif operator == "-":
            result = subtract(x, y)
        elif operator == "*":
            result = multiply(x, y)
        elif operator == "/":
            result = divide(x, y)
        else:
            result = "Invalid operator"

        print(f"Result: {result}\n")

# Call main once
main()

    
                
              
                
  
  

