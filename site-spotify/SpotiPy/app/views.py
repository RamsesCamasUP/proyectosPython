from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config


# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(config('CLIENT_ID'),config('CLIENT_SECRET'),))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:10]
        return render(request,'base.html',{"results":final_result})
    else:
      return render(request,'base.html',)