from bs4 import BeautifulSoup
import requests
import json

def scrape_movie_links(url, output_path):

    """
    Scrapes movie links from a given URL and saves them to a JSON file.

    Parameters
    ----------
    url : str
        The URL of the webpage containing movie links.
    output_path : str
        The path where the JSON file containing scraped movie links will be saved.

    Returns
    -------
    None

    Notes
    -----
    This function scrapes movie links from the specified webpage and saves them to a JSON file.
    It searches for HTML elements with class 'details' to extract movie titles and URLs.
    """
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    details = soup.find_all(class_='detail')

    details_list = soup.find_all('span', class_='details')

    movies_link = {}

    for details in details_list:
        title_element = details.find('a', class_='title')
        title = title_element.text
        url = title_element['href']

        year = details.find('span', class_='year').text.strip('()')

        movies_link[title] = url

    
    with open(output_path, "w") as json_file:
        json.dump(movies_link, json_file, indent=4)
    
    print(f'Output generated at: {output_path}')



if __name__ == '__main__':

    url = 'https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/'
    output_path = 'links.json'

    scrape_movie_links(url, output_path)