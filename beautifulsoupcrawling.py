import requests
from bs4 import BeautifulSoup
url = "https://open.spotify.com/playlist/1f6Gmqsc2ny8BeeVml77G1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}
res = requests.get(url, headers=headers)
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

songs = soup.find_all("span", attrs = {"class": "track-name"})

song_titles = ""
for song in songs:
    song_title = song.get_text()    
    song_titles += song_title + "\n"

with open("songs.txt", "w", encoding="utf8") as f:
    f.write(song_titles)
