Q2)Write a python program to reverse a number using a while loop. 
=>
# Function to reverse a number
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        rev = (rev * 10) + digit  # Append the digit to the reversed number
        n = n // 10  # Remove the last digit
    return rev

# Input from user
num = int(input("Enter a number: "))

# Handling negative numbers
if num < 0:
    reversed_num = -reverse_number(-num)
else:
    reversed_num = reverse_number(num)

print(f"Reversed number: {reversed_num}")


OUTPUT :
    #I have enter the number "12" 
    Enter a number: 12
Reversed number: 21
