Q3) Write a python program finding the factorial of a given number
    using a while loop ?
=>
# Function to calculate factorial using a while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 1:
        result *= n  # Multiply result by the current number
        n -= 1  # Decrease the number by 1
    return result

# Input from user
num = int(input("Enter a number: "))

# Output the factorial
print(f"Factorial of {num} is {factorial(num)}")



OUTPUT :
    
    #First number 3
Enter a number: 3
Factorial of 3 is 6

  #second number -3
Enter a number: -3
Factorial of -3 is Factorial is not defined for negative numbers
