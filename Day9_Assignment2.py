Q2).Write a Python program to remove duplicate characters of a given string. 

Input = “String and String Function” 

Output: String and Function


=>

def remove_duplicates(s):
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

# Input string
input_str = "String and String Function"
output_str = remove_duplicates(input_str)
print("Output:", output_str)


OUTPUT :
     String adFuco
