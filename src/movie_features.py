import pandas as pd
import json

def create_movie_features(movies_genre, output_path):
    """
    Creates a movie features DataFrame based on the provided movie genres dictionary and saves it to a CSV file.

    Parameters
    ----------
    movies_genre : dict
        A dictionary containing movie titles as keys and their corresponding genres as values.
    output_path : str
        The path where the CSV file containing movie features will be saved.

    Returns
    -------
    None

    Notes
    -----
    This function creates a DataFrame where each row represents a movie and each column represents a genre.
    The value of each cell indicates whether the movie belongs to the corresponding genre (1) or not (0).
    The genres are derived from the provided dictionary of movie genres.
    """

    # Get the unique movie genres
    unique_genres = []
    for val in movies_genre.values():
        for v in val:
            if v not in unique_genres:
                unique_genres.append(v)

    # Create empty movie features df
    movie_features = pd.DataFrame(columns=unique_genres,index=list(movies_genre.keys()))

    # Populate movie features df
    for col in movie_features.columns:
        for key,value in movies_genre.items():
            if col in value:
                movie_features.loc[key,col] = 1
            else:
                movie_features.loc[key,col] = 0

    movie_features.to_csv(output_path)


if __name__ == '__main__':
    with open('outputs/genres.json', "r") as json_file:
        movies_genre = json.load(json_file)

    output_path = 'movie_features.csv'

    create_movie_features(movies_genre=movies_genre, output_path=output_path)