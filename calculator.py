
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: division by 0 is not allowed"
    else:
        return a / b
    
def main():
    print("Hi there! Welcome to the Simple Calculator!")
    print("This program will help you perform basic arithmetic operations.")
    
    while True: 
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5": 
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            try: 
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == "1":
                print(f"Result: {add(num1, num2)}")

            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")

        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()