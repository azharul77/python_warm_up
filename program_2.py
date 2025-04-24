# Addition
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# Division 

num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))

if num4 == 0:
    print("Error: Division by zero is not allowed")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")