from bs4 import BeautifulSoup
import requests
import json


def scrape_movie_genres(input, output_path):
    
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
