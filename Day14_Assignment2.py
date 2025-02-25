Q2)Write a Python program that prompts the user to input an integer and
raises a ValueError exception if the input is not a valid integer

=>

def get_integer():
    try:
        num = input("Enter an integer: ")
        if not num.isdigit() and not (num.startswith('-') and num[1:].isdigit()):
            raise ValueError("Invalid input. Please enter a valid integer.")
        print(f"You entered: {int(num)}")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
get_integer()


OUTPUT :
    #Here the output is :
Enter an integer: 20
You entered: 20
