class MovieLibrary:
    # Class attribute
    available_movies = []
    
    def __init__(self, member_name):
        # Instance attributes
        self.member_name = member_name
        self.borrowed_movies = []
    
    def borrow_movie(self, movie):
        """Method to borrow a movie from the library."""
        if movie in MovieLibrary.available_movies:
            self.borrowed_movies.append(movie)
            MovieLibrary.available_movies.remove(movie)
            print(f"{self.member_name} borrowed '{movie}'.")
        else:
            print("Movie not available.")
    
    def return_movie(self, movie):
        """Method to return a movie to the library."""
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"{self.member_name} returned '{movie}'.")
        else:
            print("This movie was not borrowed by you.")
    
    def view_borrowed_movies(self):
        """Method to view movies borrowed by the member."""
        print(f"Movies borrowed by {self.member_name}: {self.borrowed_movies}")

# Example usage
MovieLibrary.available_movies = ["Inception", "Titanic", "Interstellar", "The Matrix"]

# Creating a library member
member1 = MovieLibrary("John")
member1.borrow_movie("Inception")
member1.view_borrowed_movies()
member1.return_movie("Inception")
member1.view_borrowed_movies()