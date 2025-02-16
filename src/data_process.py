import os
import glob
import shutil
import pandas as pd
from config import DOWNLOAD_PATH, OUTPUT_PATH

def load_data():
    """Loads the first CSV file from the Kaggle dataset directory."""
    kaggle_csv = glob.glob(os.path.join(DOWNLOAD_PATH, "*.csv"))
    if not kaggle_csv:
        raise FileNotFoundError("No CSV file found in the dataset directory.")
    return pd.read_csv(kaggle_csv[0])

def preprocess(df):
    print("Before pre-processing shape: ", df.shape)
    # drop duplicate ids
    df = df.drop_duplicates(subset=['id'])
    # remove oct 2nd data
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    df = df[df.created_utc >= "2024-10-03"]
    # remove empty string texts
    df = df[df.text != ""]
    # remove duplicate texts
    df = df[~df.text.duplicated()]
    # remove nans from text
    df = df.dropna(subset=['text'])
    # remove user profile posts
    df = df[~df.subreddit.str.startswith('u_')]
    # reset index
    df.reset_index(inplace=True)
    
    print("Post pre-processing shape: ", df.shape)
    return df

def save_preprocessed_data(df):
    """Saves the preprocessed data to a CSV file."""
    if os.path.exists(OUTPUT_PATH):
        # Remove all existing files in the directory
        shutil.rmtree(OUTPUT_PATH)
    os.makedirs(OUTPUT_PATH)
    df.to_csv(os.path.join(OUTPUT_PATH, "processed.csv"), index=False)
    print(f"Preprocessed data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    df = load_data()
    df_preprocessed = preprocess(df)
    save_preprocessed_data(df_preprocessed)
