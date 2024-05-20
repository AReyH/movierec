import pandas as pd
import numpy as np
import json


def build_user_profiles(ratings_df, features_df, output_path_X, output_path_y):
    user_profiles_X = {}
    user_profiles_y = {}

    for user in ratings_df.index:
        X = []
        y = []
        for col in ratings_df.columns:
            if pd.notna(ratings_df.loc[user,col]):
                X.append(features_df.loc[col].values)

                y.append(ratings_df.loc[user,col])
        
        new_X = np.vstack(X)
        user_profiles_X[user] = new_X.tolist()
        user_profiles_y[user] = y

    with open(output_path_X, "w") as json_file:
        json.dump(user_profiles_X, json_file, indent=4)

    with open(output_path_y, "w") as json_file:
        json.dump(user_profiles_y, json_file, indent=4)
    
    print(f'Output generated at: {output_path_X}')
    
    print(f'Output generated at: {output_path_y}')



if __name__ == '__main__':
    ratings_df = pd.read_csv('outputs/ratings_matrix.csv',index_col=0)
    features_df = pd.read_csv('outputs/movie_features.csv',index_col=0)

    output_path_X = 'user_profiles_X.json'
    output_path_y = 'user_profiles_y.json'

    build_user_profiles(ratings_df=ratings_df,
                        features_df=features_df,
                        output_path_X=output_path_X,
                        output_path_y=output_path_y)