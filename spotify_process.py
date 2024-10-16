import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import whisper

def get_show(my_id, my_secret, show_id):
    ccm = SpotifyClientCredentials(my_id, my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm, language='ja')


    results = spotify.show_episodes(show_id, limit=10, market="JP")
    episodes = results['items']
    while results['next']:
        results = spotify.next(results)
        episodes.extend(results['items'])
    print(len(episodes),"番組取得した")
    #print(episodes)
    return episodes

def get_episode(my_id, my_secret, episode_id):
    ccm = SpotifyClientCredentials(my_id, my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm, language='ja')

    episode = spotify.episode(episode_id, market='us')
    return episode

def process_mp3(url):
    """Process mps and generate a description."""
    model = whisper.load_model("small") #モデル指定
    result = model.transcribe(url, verbose=True, fp16=False, language="en") #ファイル指定
    #print(result['text'])
    return result['text']