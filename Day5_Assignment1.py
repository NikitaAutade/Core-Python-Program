Q1)1. Declare a div() function with two parameters.
Then call the function and pass two numbers and display their division ?

=>

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Calling the function and displaying the result
num1 = 10
num2 = 2
result = div(num1, num2)
print("Division result:", result)


OUTPUT : 
Division result: 5.0
