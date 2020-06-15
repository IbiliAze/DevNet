import requests
import json
import urllib3
from pprint import pprint


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# channelId = 'UCrdM5ZqUwanu9CzuuFBgrcQ'
# def test():
#     url = 'https://www.googleapis.com/youtube/v3/videos'


oauth = 'BQA6I-voWnqTX385ejaYXr_YD50YUodyoEMWki61jlQxb7lX-w1ZwQu7ZWpVEOrj6KHijAQjoVte71ud_YyT0Ctqi6tP92FlffjFa6AYPB82yQ16FSwcKc6fly0K2aHCby06syjBFNLdMGPnVaoOeXQ0u2T-BPoheEY67c4TzZD70e1Ar8qFdhRzMX5Z8G3qi08OTi0ea6yHJzos2f3EDwIS28fwRCrrTRemSpzXvlNsSAIa5ymIBWo_7JCOU3Rz6PLoGzaAKg'
user_playlist = str(input("Enter the Playlist Name: "))
how_many_mixes = int(input("How many Mixes? "))
userId = "1123268507"



def regex(track, artist):
    def lowercase(anysring):
        return anysring.lower()
    song_name_lower_case = lowercase(track)
    artist_name_lower_case = lowercase(artist)
    song_name_lower_case = song_name_lower_case.replace(" ", "+")
    artist_name_lower_case = artist_name_lower_case.replace(" ", "+")
    query = f"{song_name_lower_case}+artist:{artist_name_lower_case}"
    return query



#####SONG SEARCH#####
def search():
    #Takes in the song Name and the Artist as varibales
    song_name = str(input("Enter the Song Name: "))
    artist_name = str(input("Enter the Artist Name: "))
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {oauth}"
    }
    query = regex(track=song_name, artist=artist_name)
    q = query
    type = "track"
    limit = how_many_mixes
    query_string = f"q={q}&type={type}&limit={limit}"
    url = f"https://api.spotify.com/v1/search?{query_string}"
    response = requests.get(url, headers=headers, verify=False).json()
    # print(json.dumps(response, indent=2, sort_keys=True))
    tracks = response['tracks']['items']
    # print(json.dumps(tracks, indent=2, sort_keys=True))
    tracks_list = []
    for track in tracks:
        track_uri = track['uri']
        tracks_list.append(track_uri)
    # print(tracks_list)
    return(tracks_list)
# track_list = search()



#####CREATE PLAYLIST#####
def create_playlist():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {oauth}"
    }
    payload = {
        'name': user_playlist
    }
    url = f"https://api.spotify.com/v1/users/{userId}/playlists"
    get_response = requests.get(url, headers=headers).json()
    # print(json.dumps(get_response, indent=2, sort_keys=True))
    playlists = get_response['items']
    for playlist in playlists:
        if playlist['name'] == user_playlist:
            playlistId = playlist['id']
            return playlistId
        else:
            response = requests.post(url, headers=headers,
                data=json.dumps(payload), verify=False).json()
            # print(json.dumps(response, indent=2, sort_keys=True))
            playlistId = response['id']
            # print(playlistId)
            return playlistId
# playlistId = create_playlist()



#####ADD SONG TO PLAYLIST#####
def add_song():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {oauth}"
    }
    payload = {
        'uris': track_list
    }
    url = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks"
    response = requests.post(url, headers=headers, 
        data=json.dumps(payload), verify=False).json()
    # print(json.dumps(response, indent=2, sort_keys=True))
    snapshotId = response['snapshot_id']
    return snapshotId
# snapshotId = add_song()

def main():
    track_list = search()
    playlistId = create_playlist()
    snapshotId = add_song()
