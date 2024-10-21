from math import sqrt
print("$$$$$$ WELCOME TO THE  CALCULATOR FOR TWO NUMBER $$$$$$")
print()
try:
    def add(a, b):
        print(f"The sum of {a} and {b} is ", a + b)

    def subtract(a, b):
        print(f"The subtraction between {a} and {b} is ", a - b)

    def multipication(a, b):
        print(f"The multiplication of {a} and {b} is ", a * b)

    def division(a, b):
        print(f"The divison betwwen {a} and {b} is ", float(a / b))

    def power(a, b):
        print(f" {a} ^ {b} = {a**b}")

    def remainder(a, b):
        print(f"The remainder betwwen {a} and {b} is ", float(a % b))

    def square(a):
        print(f"The square of {a} is ", sqrt(a) )

   
    operation=input("Enter the operation you want to do like ( + ,-,/,*,power,square,%): ")
    print()
    if(operation == "square"):
        num = int(input("Enter  number:"))
    else :
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
   
    print()
    if (operation == "+"):
        add(a, b)
    elif (operation == "-"):
        subtract(a, b)
    elif (operation == "*"):
        multipication(a, b)
    elif (operation == "/"):
        division(a, b)
    elif (operation == "power"):
        power(a, b)
    elif (operation == "%"):
        remainder(a, b)
    elif (operation == "square"):
        square(num)
    else:
        print("Invalid operation")

except:
    print("Invalid Input")

print("Program finished.")
input("Press Enter to exit...")
