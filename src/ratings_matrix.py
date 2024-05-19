import pandas as pd
import numpy as np
import random
import json

def ratings_matrix(movies_genre, output_path, threshold=0.7, n_users=1000):
    """
    Generates a ratings matrix based on movie genres and saves it to a CSV file.

    Parameters
    ----------
    movies_genre : dict
        A dictionary containing movie titles as keys and their corresponding genres as values.
    output_path : str
        The path where the CSV file containing the ratings matrix will be saved.
    threshold : float, optional
        The threshold probability for a user to watch a movie (default is 0.7).
    n_users : int, optional
        The number of users for which ratings are generated (default is 1000).

    Returns
    -------
    None

    Notes
    -----
    This function generates a ratings matrix where rows represent users and columns represent movies.
    Ratings are based on user preferences for movie genres and are randomly assigned using a Beta distribution.
    Users have preferences for 1 to 4 movie genres, and their ratings are biased towards those genres.
    """

    # Create n_users
    unique_users = [f'user{str(i).zfill(5)}' for i in range(n_users)]

    df = pd.DataFrame(columns=list(movies_genre.keys()),index=unique_users)

    # Just like in movie_features.py, this creates a list of unique movie genres
    unique_genres = []
    for val in movies_genre.values():
        for v in val:
            if v not in unique_genres:
                unique_genres.append(v)

    # Creates randomly 1 to 4 generated preferences for the users
    # This simulates if the user likes 1 to 4 genres which will be given
    # higher scores in the ratings matrix
    user_genres = {}
    for user in unique_users:
        user_genres[user] = random.sample(unique_genres, random.randint(1,4))

    # Creates ratings matrix
    for i in df.index:
        for col in df.columns:
            for genre in movies_genre[col]:
                # If a randomly generated number is higher than threshold, then
                # the user will have watched that movie
                if random.random() > threshold:
                    # If the genre of the movie is in the user's preferred genres
                    # then the score will be given on a number generated from a Beta distribution
                    # with alpha = 8, and b = 2, this gives it a heavy right tail meaning the score
                    # will most likely be high
                    if genre in user_genres[i]:
                        df.loc[i,col] = round(5*np.random.beta(a=8,b=2,size=1)[0],1)
                    # Otherwise, if the genre of the movie is not in the preferred user's genres,
                    # then the user will most likely give it a low score, the score will be given
                    # based on a number generated from a Beta distribution with alpha = 2 and beta = 2
                    # this gives it a bell shaped distribution where the score will be random, with
                    # high likelihood that the score will be around 2.5
                    else:
                        df.loc[i,col] = round(5*np.random.beta(a=2,b=2,size=1)[0],1)
                else:
                    df.loc[i,col] = 0

    df.to_csv(output_path)


if __name__ == '__main__':
    with open('outputs/genres.json', "r") as json_file:
        movies_genre = json.load(json_file)

    output_path = 'ratings_matrix.csv'
    
    ratings_matrix(movies_genre=movies_genre, output_path=output_path)