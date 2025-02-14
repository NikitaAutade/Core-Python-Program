Q2)Write a python program to check whether a number is palindrome or not? 
=>
# Function to check if a number is a palindrome
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        rev = (rev * 10) + digit  # Append the digit to the reversed number
        n = n // 10  # Remove the last digit
    return original == rev  # Check if the original and reversed numbers are the same

# Input from user
num = int(input("Enter a number: "))

# Handling negative numbers (Negative numbers are not palindromes)
if num < 0:
    print(f"{num} is not a palindrome")
else:
    if is_palindrome(num):
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")


OUTPUT : 
  #first number enter  is 250
Enter a number: 250
250 is not a palindrome

#second number enter is 2
Enter a number: 2
2 is a palindrome
