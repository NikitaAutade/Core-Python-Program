Q1)Write a Python program to handle a ZeroDivisionError exception
when dividing a number by zero

=>

def safe_division(a, b):
    try:
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Example usage
a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))
print(safe_division(a, b))



OUTPUT :
    
Enter numerator: 56
Enter denominator: 12
Result: 4.666666666666667


Enter numerator: 20
Enter denominator: 30
Result: 0.6666666666666666

