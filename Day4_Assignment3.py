Q3)Python Program to Check if a Number is Positive, Negative or zero ?
=>

# Function to check the number
def check_number(num):
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

# Input from user
num = float(input("Enter a number: "))

# Checking the number
check_number(num)


OUTPUT :
#Enter the Number an check where it is postitve or negative

Enter a number: 50
The number is Positive.

Enter a number: 0
The number is Zero.

Enter a number: -50
The number is Negative.
