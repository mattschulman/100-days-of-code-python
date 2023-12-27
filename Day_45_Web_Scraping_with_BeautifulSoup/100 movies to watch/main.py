import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
#print(soup.prettify())

#The movies are in H3 elements with a class of "title"
all_movies = soup.find_all(name="h3", class_="title")

#Extract the text of the H3 element and put in a list called all_movies
movie_titles = [movie.getText() for movie in all_movies]
#print(movie_titles[::-1])

with open("movies.txt", "w") as file:
    #Reverse the order of the list using slicing [::-1]
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")

