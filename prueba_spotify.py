import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


artist_url = 'spotify:artist:2ifvIECHAlEgPMBuBOJ0lG'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='3d76710966824eabbb4a734e0b8637f0',client_secret='4ff09a5a98914d5db8f78520d1d796cf',))
results = spotify.artist_top_tracks(artist_url)
for track in results['tracks'][:10]:
     print('track    : ' + track['name'])
     print('audio    : ' + track['preview_url'])
     print('cover art: ' + track['album']['images'][0]['url'])
     print()