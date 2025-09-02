import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import random
import webbrowser

def play_music():
    """opens a random song from a chosen spotify playlist in browser
    """
    #gets key from .env
    load_dotenv()
    client_id = os.getenv("SPOTIFY_ID")
    client_secret = os.getenv("SPOTIFY_SECRET")

    #authenticate spotify account
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://127.0.0.1:5000/redirect",
        scope="playlist-read-private")
    )

    #get list of tracks from linked playlist
    playlist_id = os.getenv("SPOTIFY_PLAYLIST")
    playlist_data = sp.playlist_tracks(playlist_id)
    tracks = playlist_data["items"]

    #pick a random track and open url in browser
    track = random.choice(tracks)["track"]
    url = track["external_urls"]["spotify"]
    webbrowser.open(url)