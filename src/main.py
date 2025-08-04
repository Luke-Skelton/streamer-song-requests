# src/main.py

from src.data_loader import load_song_requests
from src.spotify_client import SpotifyAPI
import config

def run_process():
    """
    Main function to run the entire song request processing workflow.
    """
    print("--- Starting Twitch Song Request Processor ---")
    
    # 1. Load song data from the CSV file
    song_requests_df = load_song_requests()
    
    if song_requests_df is None:
        print("--- Process stopped due to data loading error. ---")
        return

    # 2. Initialize the Spotify API client
    spotify = SpotifyAPI()
    if not spotify.sp:
        print("--- Process stopped due to Spotify authentication error. ---")
        return

    # 3. Find Spotify IDs for each song
    print("\n--- Searching for songs on Spotify... ---")
    track_ids_to_add = []
    for index, row in song_requests_df.iterrows():
        # Make sure data is a string and remove leading/trailing whitespace
        song_name = str(row['Song Name']).strip()
        artist = str(row['Artist']).strip()
        album = str(row['Album']).strip()
        
        track_id = spotify.find_song_id(song_name, artist, album)
        if track_id:
            track_ids_to_add.append(track_id)
    
    # Remove duplicates that might have been requested multiple times
    unique_track_ids = list(set(track_ids_to_add))
    print(f"\nFound {len(unique_track_ids)} unique tracks to add.")

    # 4. Add the found songs to the review playlist
    if not unique_track_ids:
        print("--- No new songs to add to the playlist. Process finished. ---")
        return
        
    print(f"\n--- Adding songs to playlist ID: {config.PLAYLIST_ID} ---")
    spotify.add_songs_to_playlist(unique_track_ids)
    
    print("\n--- Process completed successfully! ---")


if __name__ == '__main__':
    run_process()
