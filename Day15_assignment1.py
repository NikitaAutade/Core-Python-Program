Q1)Write a function in python to read the content from a text file "ABC.txt" line by line
and display the same on screen. 

=>
def read_file_line_by_line():
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line, end='')  # end='' to avoid extra new lines
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")

# Call the function
read_file_line_by_line()




OUTPUT :
    #Here The Data from my txt file (ABC.txt)
Hello
I am Nikita Autade
From Dr Dy patil ACS College Pimpri Pune
Currently Doing MSC Computer Science
