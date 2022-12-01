import spacy

class Movie:
    def __init__(self, title, description):
        self.title = title
        self.description = description

def file_read():
    try:
        with open('movies.txt', 'r', encoding='utf-8') as file_information:
            data = file_information.read()
        data = data.strip()
        data = data.split("\n")
        for movie_details in data:
            movie_details = movie_details.split(":")
            movie_details[0] = movie_details[0].strip()
            movie = Movie(movie_details[0], movie_details[1])
            movie_list.append(movie)
        return True
    except FileNotFoundError:
        print("Sorry, 'movies.txt' appears to be missing.")

def file_comparison(movie_comparison):
    score_to_beat = 0
    best_match = None
    for movie in movie_list:
        description = nlp(movie.description)
        comparison = nlp(movie_comparison)
        score = description.similarity(comparison) * 100
        if score > score_to_beat:
            score_to_beat = score
            best_match = movie
    print(f'''The best movie for you to watch is {best_match.title} with a {score_to_beat:.2f}% match.
description: {best_match.description}''')

nlp = spacy.load('en_core_web_md')

movie_list = []
comparison = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk landed on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

file_exists = file_read()
if file_exists:
    file_comparison(comparison)