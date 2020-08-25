import requests
from django.http import HttpResponse, JsonResponse

WEATHER_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
WEATHER_APPID = '931a7af1736cc80e90ef7752a4b5d789'

CLASSIC_PLAYLIST = '7umNJ28Wi1QQwllNMvRORu'
ROCK_PLAYLIST = '6zJYd4fWSqRIR7g1Tp2lam'
POP_PLAYLIST = '27BkrEIPh3FiCGfnaOtnOK'

USER_ID = 'freitasvazthiago'
TOKEN = 'BQBXqmyVOTEbcO-uF1633ReN9YIg1RoYhd2tIUzQhVyIGXaKr0CpifSisLMsPQIQNJel1cAUkH7sXMRFwPbRX9ljrPAPmd9gR5RNzVXXoOYIrLqXUVa7HfRk3-FHJWeJbdfFQDqOOqEvyVfGb6C2JeDP8K3Ew9MODS3D'


def index(request):
    if request.method == 'GET':
        city_name = request.GET['city_name']

        params = {
            'q': city_name,
            'lan': 'pt_br',
            'units': 'metric',
            'appid': WEATHER_APPID
        }

        r = requests.get(WEATHER_ENDPOINT, params).json()

    
    if r['cod'] != 200:
        return JsonResponse(r, safe=False)

    current_temperature = r['main']['temp']
    musics = []

    if current_temperature > 25:
        musics.append(getSpotifyMusicPlaylist(ROCK_PLAYLIST))
    elif current_temperature >= 10 and current_temperature <= 25:
        musics.append(getSpotifyMusicPlaylist(POP_PLAYLIST))
    else:
        musics.append(getSpotifyMusicPlaylist(CLASSIC_PLAYLIST))

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


def getSpotifyMusicPlaylist(playlist):
    url = 'https://api.spotify.com/v1/playlists/'+ playlist + '/tracks?fields=items(track(name))'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer ' + TOKEN
    }

    r = requests.get(url, headers=headers).json()
    
    return r