# src/spotify_client.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import config

class SpotifyAPI:
    def __init__(self):
        """
        Initializes the Spotify client using credentials from .env and config.
        """
        load_dotenv() # Load environment variables from .env file
        
        try:
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                scope=config.SPOTIFY_SCOPE,
                username=config.SPOTIFY_USERNAME
            ))
            self.sp.current_user() 
            print("Successfully authenticated with Spotify.")
        except Exception as e:
            print(f"Error authenticating with Spotify: {e}")
            print("Please check your .env and config.py settings.")
            self.sp = None

    def find_song_id(self, track_name: str, artist_name: str, album_name: str) -> str | None:
        """
        Searches for a song on Spotify and returns its ID. It first tries a precise
        search with the album, then falls back to a broader search if needed.

        Args:
            track_name: The name of the song.
            artist_name: The name of the artist.
            album_name: The name of the album (can be empty).

        Returns:
            The Spotify track ID as a string, or None if not found.
        """
        if not self.sp:
            return None
            
        try:
            # First, try a precise search including the album if it's provided.
            if album_name:
                query = f"track:{track_name} artist:{artist_name} album:{album_name}"
                results = self.sp.search(q=query, type='track', limit=1)
                items = results['tracks']['items']
                if items:
                    track_id = items[0]['id']
                    found_name = items[0]['name']
                    found_artist = items[0]['artists'][0]['name']
                    print(f"  -> Found via precise search: '{found_name}' by '{found_artist}' [ID: {track_id}]")
                    return track_id

            # If the precise search fails or album wasn't provided, fall back to track and artist.
            query = f"track:{track_name} artist:{artist_name}"
            results = self.sp.search(q=query, type='track', limit=1)
            
            items = results['tracks']['items']
            if not items:
                print(f"  -> Could not find '{track_name}' by '{artist_name}' on Spotify.")
                return None
            
            track_id = items[0]['id']
            found_name = items[0]['name']
            found_artist = items[0]['artists'][0]['name']
            print(f"  -> Found via general search: '{found_name}' by '{found_artist}' [ID: {track_id}]")
            return track_id
            
        except Exception as e:
            print(f"An error occurred while searching for song: {e}")
            return None

    def add_songs_to_playlist(self, track_ids: list[str]):
        """
        Adds a list of songs to the review playlist specified in the config.

        Args:
            track_ids: A list of Spotify track IDs.
        """
        if not self.sp or not track_ids:
            return

        try:
            # Spotify API can only add 100 tracks at a time.
            chunk_size = 100
            for i in range(0, len(track_ids), chunk_size):
                chunk = track_ids[i:i + chunk_size]
                self.sp.playlist_add_items(config.PLAYLIST_ID, chunk)
                print(f"Successfully added a batch of {len(chunk)} songs to the review playlist.")

        except Exception as e:
            print(f"An error occurred while adding songs to the playlist: {e}")
