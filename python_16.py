# factorial number 
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
    # Print a message indicating that factorial doesn't exist for negative numbers
    print("Factorial does not exist for negative numbers ")

elif num == 0:
    # Print a message stating the factorial of 0 is 1
    print("Facorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")