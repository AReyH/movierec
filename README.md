# **Movie Recommendation System**

This project is a movie recommendation system that scrapes movie from the web, and creates a ratings matrix based on user preferences and movie genres.

## **Getting Started**

To get started with this project, follow these steps:

Clone the repository:

```bash

git clone https://github.com/AReyH/movierec.git
``` 
### **Install the required dependencies:**

Navigate to the project directory:

```bash
cd movierec
```

Create a conda environment from the provided environment.yml file:

```bash
conda env create -f environment.yml
```
Activate the conda environment:

```bash
conda activate movierec
```
Run the main scripts to generate movie features and ratings matrix:

```bash
python scrape_movie_links.py
python scrape_movie_genres.py
python create_movie_features.py
python ratings_matrix.py
```

## **Project Structure**

The project consists of the following main components:

* `scrape_movie_links.py`: Scrapes movie links from a given URL and saves them to a JSON file.
* `scrape_movie_genres.py`: Scrapes movie genres for a list of movie links and saves them to a JSON file.
* `create_movie_features.py`: Creates a movie features DataFrame based on movie genres and saves it to a CSV file.
* `ratings_matrix.py`: Generates a ratings matrix based on movie genres and user preferences and saves it to a CSV file.

## **Usage**

Each script can be run independently with appropriate input data. Ensure that the required input files are available before running the scripts.

## **License**

This project is licensed under the MIT License - see [the license file](LICENSE) file for details.
