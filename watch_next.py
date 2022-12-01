# we import the spacy and tabulate libraries
import spacy
from tabulate import tabulate

# we create a class called Movie which has two attributes, title and description
class Movie:
    def __init__(self, title, description):
        self.title = title
        self.description = description

# we create a function to open a text file and read from it. We then strip and split this data to create a list. We have validation to make sure that the file exists
def file_read():
    try:
        with open('movies.txt', 'r', encoding='utf-8') as file_information:
            data = file_information.read()
        data = data.strip()
        data = data.split("\n")
        # we work through every entry in the list and split again to get the title and description. We then create a Movie object with these details and add our object to a global list
        for movie_details in data:
            movie_details = movie_details.split(":")
            movie_details[0] = movie_details[0].strip()
            movie = Movie(movie_details[0], movie_details[1])
            movie_list.append(movie)
        # if the file exists we return True which will allow our main menu to load
        return True
    except FileNotFoundError:
        print("Sorry, 'movies.txt' appears to be missing.")

# we create a file called file_comparison which takes a string description as an argument
def file_comparison(movie_comparison):
    # we start with a default score to beat of 0 and create a variable which for now is only initialised
    score_to_beat = 0
    best_match = None
    # we tokenise our movie description and assign it to a variable
    comparison = nlp(movie_comparison)
    # we use a loop to iterate every movie in our list and then tokenise that films description. We then check the similarity with that description with the one passed in as an argument which will give us a score
    for movie in movie_list:
        description = nlp(movie.description)
        score = description.similarity(comparison) * 100
        # we check if this films 'score' is higher than the current score_to_beat. If it is we update the score to beat and assign the film to best match
        if score > score_to_beat:
            score_to_beat = score
            best_match = movie
    # once our loop has finished we print out the best result to the user
    print(f'''\nThe best movie for you to watch is {best_match.title} with a {score_to_beat:.2f}% match.
description: {best_match.description}\n''')

# we load the English language model and assign it to a variable called nlp
nlp = spacy.load('en_core_web_md')

# our movie_list
movie_list = []

# These are the entries which will populate our main menu
menu_choices = [
    ["1", "Use Current Selection"],
    ["2", "Add Your Own Description"],
    ["3", "Exit"]
]

# This string is the description which we will be comparing to our movie list
comparison = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him 
into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk landed on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# we create a main menu for the user and ask then to enter a selection. We have validation to make sure that their selection is valid
file_exists = file_read()
while file_exists:
    print(tabulate([[comparison]], headers=["Current Description"], tablefmt="rounded_grid"))
    print(tabulate(menu_choices, headers=["Option", "Function"], tablefmt="rounded_grid"))
    while True:
        try:
            user_selection = int(input("Please enter your selection: "))
            if user_selection > 0 and user_selection <= len(menu_choices):
                break
            else:
                print("Sorry, that selection is not valid")
        except ValueError:
            print("Sorry, that selection was invalid. Please try again")
    if user_selection == 1:
        file_comparison(comparison)
    if user_selection == 2:
        comparison = input("Please enter the film description: ")
        file_comparison(comparison)
    if user_selection == 3:
        print("Goodbye!")
        exit()