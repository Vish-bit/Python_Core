# Input: User provides two numbers and selects an operation (addition, subtraction, multiplication, division).

num1 = input("Enter the first number: ")
opt = input("Enter the operation(+,-,*,/): ")
num2 = input("Enter the second number: ")
result = None

if(opt == "+"):
    result = int(num1) + int(num2)
elif(opt == "-"):
    result = int(num1) - int(num2)
elif(opt == "*"):
    result = int(num1) * int(num2)
elif(opt == "/"):
    result = int(num1) / int(num2)

if result is not None:
    print(f"Result: {result}")


# OUTPUT
# Enter the first number: 25
# Enter the operation(+,-,*,/): -
# Enter the second number: 5
# Result: 20
