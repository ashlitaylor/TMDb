-------------------------------------------------------
# Scraping and Visualizing data from The Movie Database
-------------------------------------------------------
This python code was completed as part of an assignment for my Data and Visual Analytics course at The Georgia Insitute of Technology. 

### Introduction
The Movie Database [TMDb]("https://www.themoviedb.org/") is a popular, user editable database for movies and TV shows. The Python code script.py accesses the API to scrape and parse data for 350 movies that have been released in the 'Drama' genre since 2004 and pairs a movie that is similar. 
I removed all duplicate movie pairs. That is, if both the pairs A,B and B,A are present, I only keep A,B where the value of title A is less than thevalue of title B.
After removing duplicate pairs, I request five similar movies and output the data to a CSV file. I used the data from the CSV file to generate a similar movie network graph using [Gephi]("https://gephi.org/") to visualize movie similarity. This code output two CSV files:
*movie_ID_name.csv - a CSV file containing 350 of the most popular Drama movies since 2004
*movie_ID_sim_movie.csv - a CSV file containing the five most similar movies to the most popular Drama movies. Please visit this [notebook](https://github.com/ashlitaylor/TMDb/blob/master/TMDb.ipynb) to see a step by step guide to each section of the code. 

### Prerequisites
This code requires ##Python 3.X** and requires a TMDb API code to be input to run. To get a TMDb account and API Code:
1. Get a [TMDb account](https://www.themoviedb.org/account/signup)
2. Request an [API key](https://docs.google.com/document/d/e/2PACX-1vQkWjHiLS1Xu2HZNQ7Egv08l_DdPnugoxUOZ0ugqBNHWY529xWB417QoSS0MbIih6PS9gu1Y1D-NFDT/pub)
3. Follow TMDb API [Documentation](https://developers.themoviedb.org/3/getting-started/introduction)

### Run
In the terminal or command window, navigate to the folder where the script is located, and input the following command, substituting your API key:

```python3 script.py <API_KEY>```

This will run the 'script.py' file and execute the code, generating the two aforementioned CSV files. 
