# config.py

# The unique ID of the playlist you want to add songs to for review.
# Find this in Spotify by clicking ..., Share, Copy Spotify URI.
PLAYLIST_ID = 'https://open.spotify.com/playlist/339oFXljP0d5fKBWMU0lmQ?si=96f94f49b16041c6'

# Your Spotify username (sometimes called user ID).
# Find this on your Spotify account page.
SPOTIFY_USERNAME = 'skellevo24'

# The path to the CSV file exported from your Google Form.
DATA_FILE_PATH = 'data/song_requests.csv'

# Define the permissions our script needs.
# This allows it to modify public and private playlists.
SPOTIFY_SCOPE = 'playlist-modify-public playlist-modify-private'