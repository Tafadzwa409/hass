 # defining functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by Zero"
    return x / y

# main program
while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        else:
            result = divide(num1, num2)

        print("Result: ", result)

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option. Please try again")