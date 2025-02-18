def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates

# Example usage
my_list = [10, 20, 30, 40, 20, 50, 60, 30, 70, 80, 10]
duplicates = find_duplicates(my_list)
print("Duplicate values:", duplicates)
