import os
from decouple import config
from spotify_client import SpotifyClient
def run():
    #Busca en Spotify por canciones Random
    #Una vez obtenidas agregarlas a nuestra biblioteca
    spotify_client = SpotifyClient(config('SPOTIFY_AUTH_TOKEN'))
    random_tracks = spotify_client.get_random_tracks()
    track_ids = [track['id'] for track in random_tracks]
    was_added = spotify_client.add_tracks_to_library(track_ids)
    if was_added:
        for track in random_tracks:
            print(f"Added {track['name']} to library")

if __name__ == "__main__":
    run()