from bs4 import BeautifulSoup
from PyMovieDb import IMDB
import json
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
imdb = IMDB()

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []


# res = imdb.get_by_name('The Shawshank Redemption')

# json_object = json.loads(res)
# print(json_object["type"])
# print(res[1][0])

# arquivo = open("texto.json", "a")
# arquivo.write(res)
