def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b==0:
        return "Error: Division by zero"
    return a/b
def exp(a, b):
    return a**b

while True:
    print("\nMenu for calculator operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    choice = input("Enter your choice to perform operation or '0' to exit: ")
    if choice == '0':
        print("Exiting the calculator")
        break
    elif choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", sub(num1, num2))
        elif choice == '3':
            print("Result:", mul(num1, num2))
        elif choice == '4':
            print("Result:", div(num1, num2))
        elif choice == '5':
            print("Result:", exp(num1, num2))
    else:
        print("Invalid choice. Please select a valid operation...")
    

