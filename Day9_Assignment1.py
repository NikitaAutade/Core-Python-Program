1. Write a Python program to Count all letters, digits,
and special symbols from the given 
string Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3 ?
=>

def count_chars_digits_symbols(s):
    char_count = sum(c.isalpha() for c in s)
    digit_count = sum(c.isdigit() for c in s)
    symbol_count = len(s) - (char_count + digit_count)
    
    print(f"Chars = {char_count}")
    print(f"Digits = {digit_count}")
    print(f"Symbol = {symbol_count}")

# Given input
input_str = "P@#yn26at^&i5ve"
count_chars_digits_symbols(input_str)


OUTPUT :

Chars = 8
Digits = 3
Symbol = 4
