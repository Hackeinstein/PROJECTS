import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# get songs at time of choice
date = input("What year do you want to travel to? (Format YYYY-MM-DD): ")
url = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
website = url.text

soup = BeautifulSoup(website, "html.parser")
h3 = soup.select("li ul li h3")
songlist = [individs.getText().strip("\n\t") for individs in h3]

# authenticate spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="*******",
                                               client_secret="***********",
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="************"))

user_id = sp.current_user()["id"]
year = date.split("-")
songurl = []
# get song url
for song in songlist:
    try:
        track = sp.search(type="track", q=f'track:{song} year:{year[0]}', limit=1)
        songurl.append(track['tracks']['items'][0]['uri'])
    except Exception as ex:
        print(f"The song {song} is not avaliable")
# #print(track)
# print(songurl)

# add songs to playlist
# try:
#     playlist = sp.user_playlist_create(user=user_id, name="API SHIT", public=False, description="epic shit anyways")
# except Exception as ex:
#     print(ex)

playlist_id="************"


try:
   sp.playlist_add_items(playlist_id=playlist_id, items=songurl)
except Exception as ex:
        print(ex)

