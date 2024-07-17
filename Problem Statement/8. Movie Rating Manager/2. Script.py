def display_menu():
    print("\nWelcome to the Movie Rating Manager!")
    print("Please choose an option:")
    print("1. Add a movie and its rating")
    print("2. View all movies and their ratings")
    print("3. Update a movie rating")
    print("4. Calculate the average rating")
    print("5. Find the highest and lowest-rated movies")
    print("6. Search for a movie by title")
    print("7. Exit")

def add_movie(movies):
    title = input("Enter the movie title: ")
    try:
        rating = float(input("Enter the movie rating: "))
        movies.append({"title": title, "rating": rating})
        print("Movie added successfully!")
    except ValueError:
        print("Invalid input! Rating should be a number.")

def view_movies(movies):
    if not movies:
        print("No movies to display.")
    else:
        print("Movie List:")
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. Title: {movie['title']}, Rating: {movie['rating']}")

def update_movie(movies):
    if not movies:
        print("No movies to update.")
        return

    try:
        index = int(input("Enter the index number of the movie to update: "))
        if 1 <= index <= len(movies):
            new_rating = float(input("Enter the new rating: "))
            movies[index - 1]['rating'] = new_rating
            print("Movie rating updated successfully!")
        else:
            print("Invalid index number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_average(movies):
    if not movies:
        print("No movies to calculate average.")
    else:
        average = sum(movie['rating'] for movie in movies) / len(movies)
        print(f"The average rating is: {average:.2f}")

def find_highest_lowest(movies):
    if not movies:
        print("No movies to find highest and lowest.")
    else:
        highest = max(movies, key=lambda x: x['rating'])
        lowest = min(movies, key=lambda x: x['rating'])
        print(f"Highest Rated Movie: Title: {highest['title']}, Rating: {highest['rating']}")
        print(f"Lowest Rated Movie: Title: {lowest['title']}, Rating: {lowest['rating']}")

def search_movies(movies):
    search_term = input("Enter a movie title to search: ").lower()
    results = [movie for movie in movies if search_term in movie['title'].lower()]
    if not results:
        print("No movies found with that title.")
    else:
        print("Search Results:")
        for movie in results:
            print(f"Title: {movie['title']}, Rating: {movie['rating']}")

def main():
    movies = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            view_movies(movies)
        elif choice == '3':
            update_movie(movies)
        elif choice == '4':
            calculate_average(movies)
        elif choice == '5':
            find_highest_lowest(movies)
        elif choice == '6':
            search_movies(movies)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

"""
Explanation:
display_menu(): Prints the menu options to the screen.
add_movie(movies): Prompts the user to enter the movie title and rating, and adds the movie to the movies list. Uses try and except to handle invalid rating inputs.
view_movies(movies): Displays all movies with their index numbers, titles, and ratings. If the list is empty, it informs the user.
update_movie(movies): Prompts the user to enter the index number of the movie to update and the new rating. It updates the rating in the list and handles invalid input.
calculate_average(movies): Calculates and displays the average rating of all movies if the list is not empty.
find_highest_lowest(movies): Finds and displays the movie(s) with the highest and lowest ratings if the list is not empty.
search_movies(movies): Prompts the user to enter a movie title and displays the movies that match the search term using a list comprehension.
main(): Contains the main loop that displays the menu, captures user input, and calls the respective functions based on the user's choice. It continues running until the user chooses to exit.
"""
