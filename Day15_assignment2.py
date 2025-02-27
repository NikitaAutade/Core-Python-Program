Q2)Write a function in Python to count and
display the total number of words in a text file “ABC.txt”

=>
def count_words_in_file():
    try:
        with open("ABC.txt", "r") as file:  # Open the file in read mode
            content = file.read()  # Read the entire file content
            words = content.split()  # Split the content into words
            word_count = len(words)  # Count the number of words
            print(f"Total number of words in 'ABC.txt': {word_count}")
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")

# Call the function
count_words_in_file()


OUTPUT :


    #Here the data we have : "Hello I am Nikita Autade
    #From Dr Dy patil ACS College Pimpri
    #PuneCurrently Doing MSC Computer Science"

Total number of words in 'ABC.txt': 18
