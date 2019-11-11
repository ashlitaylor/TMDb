import http.client
import json
#import time
import sys
#import collections
import urllib
import urllib.request
from urllib.request import urlopen
import csv
from collections import defaultdict
import threading
import urllib.parse
#from itertools import combinations
API_KEY = input()

drama_genre_query = {}
drama_list_pages = list()
#Using the API to search for movies in the ‘Drama’ genre released in the year 2004 or later. 
#The 350 most popular movies in this genre are retrieved, sorted from most popular to least popular.
q1b_url = 'https://api.themoviedb.org/3/discover/movie?api_key=' + API_KEY + '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_date.gte=2004-01-01&with_genres=18'
pages = list(range(1,19))
#Query for 18 pages
for i in pages:
    page_url_append = '&page=' + str(i)
    drama_page = json.load(urllib.request.urlopen(q1b_url+page_url_append))
    drama_results = drama_page['results']
    drama_list_pages.append(drama_results)

#Creating a dictionary containing movie-ID and Title key:value pairs with top 350 movies   
for page in range(0, (len(drama_list_pages))):
    for movie in range(0, (len(drama_list_pages[page]))):
        movie_id = drama_list_pages[page][movie]['id']
        movie_name = drama_list_pages[page][movie]['title']
        if len(drama_genre_query) < 350:
            drama_genre_query.update({movie_id: movie_name})

#Writing movies to CSV file
csv_file = 'movie_ID_name.csv'
with open(csv_file, 'w', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)    
    writer.writerows(drama_genre_query.items())
   
#Step 1: SImilar movie retrieval
urlfront = 'https://api.themoviedb.org/3/movie/'
urlend = '/similar?api_key=' + API_KEY + '&language=en-US&page=1'
similar_movie_list = list()

#Function to request at most 5 similar movies
def similarrequest(queryurl):
    similar_movie_query = json.load(urllib.request.urlopen(queryurl))
    similar_movies = similar_movie_query['results']
    if len(similar_movies) > 5:
        similar_movies = similar_movies[0:5]
    for target in range(0, len(similar_movies)):
        target_movie_id = similar_movies[target]['id']
        similar_pair = source, target_movie_id
        similar_movie_list.append(similar_pair)  

for source in drama_genre_query:
    queryurl = urlfront + str(source) + urlend
    requesttimer = threading.Timer(0.25, similarrequest(queryurl))
    requesttimer.start()    
    requesttimer.cancel()

#Step 2: Deduplication
paircount = defaultdict(int)
test_list = similar_movie_list.copy()
for source, target in test_list:
    pair = (min(source, target), max(source, target))
    paircount[pair] += 1

paircount = defaultdict(int)
update_list = similar_movie_list.copy()
for source, target in update_list:
    pair = (min(source, target), max(source, target))
    paircount[pair] += 1
for source, target in paircount:
    pair = source, target
    if(paircount[pair]) >= 2:
        pair_remove = target, source
        update_list.remove(pair_remove)
similar_dict = dict(update_list)

#Writing to CSV file
csv_file = 'movie_ID_sim_movie.csv'
with open(csv_file, 'w', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(similar_dict.items())