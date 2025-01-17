print("Hi there! Welcome to the Simple Calculator!")
print("This program will help you perform basic arithmetic operations.")

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