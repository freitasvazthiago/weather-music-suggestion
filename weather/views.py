import requests
import spotipy
import spotipy.util as util
import configparser
import spotipy.oauth2 as oauth2

from django.http import HttpResponse, JsonResponse
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Weather
from django.core.serializers import serialize
from .serializers import WeatherSerializer
from rest_framework import generics

config = configparser.ConfigParser()


class MusicView(generics.GenericAPIView):
    def get(self, request, city_name):
        config.read('config.cfg')

        if request.method == 'GET':
            params = {
                'q': city_name,
                'lan': 'pt_br',
                'units': 'metric',
                'appid': config.get('WEATHER', 'WEATHER_APPID')
            }

            r = requests.get(config.get('WEATHER', 'WEATHER_ENDPOINT'), params).json()

        
        if r['cod'] != 200:
            return JsonResponse(r, safe=False)

        current_temperature = r['main']['temp']
        musics = []

        if current_temperature > 25:
            musics.append(getSpotifyPlaylistSongs(config.get('PLAYLIST', 'POP_PLAYLIST')))
        elif current_temperature >= 10 and current_temperature <= 25:
            musics.append(getSpotifyPlaylistSongs(config.get('PLAYLIST', 'ROCK_PLAYLIST')))
        else:
            musics.append(getSpotifyPlaylistSongs(config.get('PLAYLIST', 'CLASSIC_PLAYLIST')))

        addStatistic(r['id'], r['name'])

        return JsonResponse(
            {
                'data': {
                    'city_name': r['name'],
                    'temperature': current_temperature
                },
                'suggested_songs' : musics.pop(),
                'input': {
                    'city_name': city_name
                }
            }
        )

def getSpotifyPlaylistSongs(playlist):

    spotify = getSpotifyToken()
    results = spotify.playlist_tracks(playlist, fields='items(track(name))')

    return results

def getSpotifyToken():

    config.read('config.cfg')

    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')

    auth = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    token = auth.get_access_token()
    spotify = spotipy.Spotify(auth=token)

    return spotify


def addStatistic(city_id, city_name):
    
    w = Weather(city_id = city_id, city_name = city_name)
    w.save()
    
class StatisticView(generics.GenericAPIView):
    def get(self, request):
        serializer = WeatherSerializer(Weather.objects.all(), many=True)
        content = serializer.data

        return JsonResponse(
            {
                'data': {
                    'citys': content
                }
            }
        )