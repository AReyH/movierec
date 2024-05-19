import pandas as pd
import numpy as np
import random
import json

def ratings_matrix(movies_genre, output_path, threshold=0.7):
    unique_users = [f'user{str(i).zfill(5)}' for i in range(1000)]

    df = pd.DataFrame(columns=list(movies_genre.keys()),index=unique_users)

    unique_genres = []
    for val in movies_genre.values():
        for v in val:
            if v not in unique_genres:
                unique_genres.append(v)

    user_genres = {}
    for user in unique_users:
        user_genres[user] = random.sample(unique_genres, random.randint(1,4))

    for i in df.index:
        for col in df.columns:
            for genre in movies_genre[col]:
                if random.random() < threshold:
                    if genre in user_genres[i]:
                        df.loc[i,col] = round(5*np.random.beta(a=8,b=2,size=1)[0],1)
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