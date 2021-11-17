import os

SPOTIFY_CLIENT_ID = "ee9fc515c5f344f9b46b8c4f0dd573cb"
SPOTIFY_CLIENT_SECRET = "1a06ee2411a648ea9dc953a383d64ca6"
SPOTIFY_SCOPE = "user-read-playback-state, user-modify-playback-state"
CACHE_PATH = os.path.join(os.path.dirname(__file__), ".cache")