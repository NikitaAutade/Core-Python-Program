Q2) Write a Python program to get the largest and
smallest number from a list without built in functions? 
=>

def find_largest_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None  

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage
my_list = [3, 1, 7, 10, 2, 8]
largest, smallest = find_largest_smallest(my_list)
print("Largest number:", largest)
print("Smallest number:", smallest)

OUTPUT :
    #here the largest number is 10 and the smallest number is 1 
Largest number: 10
Smallest number: 1
