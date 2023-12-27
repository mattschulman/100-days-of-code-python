from bs4 import BeautifulSoup
import requests
answer = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_url = f"https://billboard.com/charts/hot-100/{answer}"

billboard_response = requests.get(billboard_url)

hot_100_html = billboard_response.text

soup = BeautifulSoup(hot_100_html, "html.parser")

song_names_data = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_data]
print(song_names)