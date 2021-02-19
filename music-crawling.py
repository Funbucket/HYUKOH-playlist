import requests
from bs4 import BeautifulSoup


def get_musics_list(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        songs = soup.find_all("span", attrs = {"class": "track-name"})

        musics = ""
        for song in songs:
            music = song.get_text()
            musics += music + "\n"
        return musics


def get_text_file(name, list):
    with open(f"{name}.txt", "w", encoding="utf8") as f:
        f.write(list)


nodongyo_url = "https://open.spotify.com/playlist/1f6Gmqsc2ny8BeeVml77G1"
stream_of_consciousness_url = "https://open.spotify.com/playlist/2IhYcOgHy8AWqgEApW2h8I"
rhythm_url = "https://open.spotify.com/playlist/3Je0WlN6XjrGOlf4bQ5Aml"

nodongyo_list = get_musics_list(nodongyo_url)
stream_of_consciousness_list = get_musics_list(stream_of_consciousness_url)
rhythm_list = get_musics_list(rhythm_url)

get_text_file("nodongyo", nodongyo_list)
get_text_file("stream_of_consciousness", stream_of_consciousness_list)
get_text_file("rhythm", rhythm_list)
