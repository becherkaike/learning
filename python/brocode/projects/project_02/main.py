# Python calculator with basic operators ( +, -, *, /)

num1 = float(input("Insert the first number of the operation: "))
operation = input("Select the operation that you wanna execute (+, -, *, /): ")
num2 = float(input("Insert the second number of the operation: "))

result = None

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 == 0:
        print("You cannot divide a number by 0!")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please enter one of the operations above!")

if result is not None:
    print(f"The result is: {round(result, 2)}")

# made a print function in every if statement at first, but tried to improve by making a print only at the end
# consulted AI because of a traceback of result not being defined if divided by 0
# learn about declaring as None and conditioning to print only if result is not None 
# initialy the last if was "if result:"
# but there was no print if the result was 0, like 5 - 5 as an example