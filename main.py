import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h3", class_="title")
title_names = []

with open("movies.txt", "w", encoding="utf-8") as file:
    for i, data in enumerate(titles, 1):
        name = ' '.join(data.text.split()[1:])
        file.write(f"{i}) {name} \n")


