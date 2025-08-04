# src/data_loader.py

import pandas as pd
import config
import os

def load_song_requests():
    """
    Loads song requests from the CSV file specified in the config.

    Returns:
        A pandas DataFrame with the song requests, or None if the file is not found.
    """
    file_path = config.DATA_FILE_PATH
    if not os.path.exists(file_path):
        print(f"Error: Data file not found at '{file_path}'")
        print("Please export your Google Form data to CSV and place it there.")
        return None

    try:
        # We now require 'Song Name', 'Artist', and 'Album' columns.
        # Adjust the column names here if your form uses different ones.
        required_cols = {'Song Name', 'Artist', 'Album'}
        df = pd.read_csv(file_path)

        if not required_cols.issubset(df.columns):
            print(f"Error: CSV file must contain the columns: {', '.join(required_cols)}")
            return None
        
        # Fill any empty 'Album' cells with an empty string so the script doesn't fail.
        df['Album'] = df['Album'].fillna('')

        print(f"Successfully loaded {len(df)} song requests from '{file_path}'.")
        return df

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None
