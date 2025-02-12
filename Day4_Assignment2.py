Q2)Python Program to Find the Largest Among Three Numbers ?
=>

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number
largest = find_largest(num1, num2, num3)

# Displaying result
print(f"The largest number is: {largest}")



OUTPUT :
    #three numbers taken by me (60,40 ,80)
Enter first number: 60
Enter second number: 40
Enter third number: 80
The largest number is: 80.0

#80 Is the Largest Number.
