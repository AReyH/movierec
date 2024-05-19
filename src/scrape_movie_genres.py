from bs4 import BeautifulSoup
import requests
import json


def scrape_movie_genres(input, output_path):
    """
    Scrapes movie genres for a given list of movie links and saves them to a JSON file.

    Parameters
    ----------
    input : dict
        A dictionary containing movie titles as keys and their corresponding URLs as values.
    output_path : str
        The path where the JSON file containing scraped movie genres will be saved.

    Returns
    -------
    None

    Notes
    -----
    This function scrapes movie genres from the provided list of movie links and saves them to a JSON file.
    It searches for genre information within the JSON-LD script tag of each movie webpage.
    """
    
    movies_genre = {}
    counter = 0
    for key,value in movies_link.items():
        if counter%10 == 0:
            print(counter + 1)
        url = value
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        json_ld_script = soup.find('script', type='application/ld+json')

        # Extract genre information
        if json_ld_script:
            movie_data = json.loads(json_ld_script.string)
            genre = movie_data.get('genre', [])
            movies_genre[key] = genre
        else:
            print("JSON-LD script not found.")
            movies_genre[key] = 'NA'
        
        counter += 1

    with open(output_path, "w") as json_file:
        json.dump(movies_genre, json_file, indent=4)
    
    print(f'Output generated at: {output_path}')


if __name__ == '__main__':

    with open('outputs/links.json', "r") as json_file:
        movies_link = json.load(json_file)

    output_path = 'genres.json'

    scrape_movie_genres(input=movies_link, output_path=output_path)
