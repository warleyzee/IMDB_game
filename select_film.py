from soupsieve import select
from filter_movies import Filter_Movies
from PyMovieDb import IMDB
from pprint import pprint
import random
import json


class Select_Film():

    def movies(self, ):

        movie = Filter_Movies().filter_movies()

        self.random_film = random.choice(movie)
        self.list_film = random.sample(movie, k=7)
        self.list_film.append(self.random_film)
        self.mix = sorted(self.list_film)

        return(self.mix)
    
    def select_film(self, ):

        mix = Select_Film().movies()
        select_film = random.choice(mix)

        imdb = IMDB()
        # res = imdb.get_by_name('Ben-Hur')
        res = imdb.get_by_name(select_film)
        # print(res)
        self.json_object = json.loads(res)

        return(self.json_object)

    def salve_film(self, ):

        self.film = Select_Film().select_film()
        pprint(self.film)
        input()

        self.name = self.film['name']
        self.duration = self.film['duration']
        self.actor = self.film['actor']
        self.creator = self.film["creator"]
        self.keywords = self.film['keywords']
        self.review = self.film["review"]['dateCreated']
        self.datePublished = self.film["datePublished"]
        self.description = self.film["description"]
        self.genre = self.film['genre']
        self.director = self.film['director']
        self.data_film = {"Name"        :self.film['name'],
                          "Duration"    :self.film['duration'],
                          "Actor"       :self.film['actor'],
                          "Creator"     :self.film["creator"],
                          "Keywords"    :self.film['keywords'],
                          "Date Created":self.film["review"]['dateCreated'],
                          "Data Publish":self.film["datePublished"],
                          "Description" :self.film["description"],
                          "Genre"       :self.film['genre'],                   
                          "Director"    :self.film['director'],
                        }
        
        return(self.data_film)

test2 = Select_Film().salve_film()
pprint(test2)

