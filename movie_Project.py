MENU_PROMPT = "\Enter 'a' to add a movie," \
              "'l' to see your movie," \
              "'f' to find the movie by title," \
              " or 'q' to quit:"
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movie(movie):
    print(f'Title: {movie["title"]}')
    print(f'Director: {movie["director"]}')
    print(f'Release year: {movie["year"]}')

def show_movie():
    for movie in enumerate(movies):
        print_movie(movie)


def find_movie():
    search_title = input("Enter the movie title you are loking for: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


user_options = { #Usage of First class Function
    "a":add_movie,
    "l":show_movie,
    "f":find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection!='q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)

menu()
