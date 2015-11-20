# -*- coding: utf-8 -*-
# Developer: Andres Anies <andres_anies@hotmail.com>

from fresh_tomatoes import open_movies_page
from media import Movie

# List of movies for Fresh Tomatoes Movie Trailer
MOVIES = [
    Movie(title='PIXELS',
          trailer='https://www.youtube.com/watch?v=eIOcWZOQL5M',
          art='http://ia.media-imdb.com/images/M/MV5BMTYxMzM4N'
              'DY5N15BMl5BanBnXkFtZTgwNzg1NTI3MzE@._V1_SX640_SY720_.jpg',
          director='Chris Columbus',
          writers=['Tim Herlihy', 'Timothy Dowling'],
          stars=['Adam Sandler', 'Kevin James', 'Michelle Monaghan']),
    Movie(title='The Dark Knight Rises',
          trailer='https://www.youtube.com/watch?v=GokKUqLcvD8',
          art='http://ia.media-imdb.com/images/M/MV5BMTk4ODQzN'
              'DY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX640_SY720_.jpg',
          director='Christopher Nolan',
          writers=['Jonathan Nolan', 'Christopher Nolan'],
          stars=['Christian Bale', 'Tom Hardy', 'Anne Hathaway']),
    Movie(title='Avatar',
          trailer='https://www.youtube.com/watch?v=5PSNL1qE6VY',
          art='http://ia.media-imdb.com/images/M/MV5BMTYwOTEwN'
              'jAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg',
          director='James Cameron',
          writers=['James Cameron'],
          stars=['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver']),
    Movie(title='Paper Towns',
          trailer='https://www.youtube.com/watch?v=w4olpTxktM4',
          art='http://ia.media-imdb.com/images/M/MV5BMjE2ODQxO'
              'DMwOF5BMl5BanBnXkFtZTgwNDY5NjY3NDE@._V1_SX640_SY720_.jpg',
          director='Jake Schreier',
          writers=['John Green', 'Scott Neustadter'],
          stars=['Nat Wolff', 'Cara Delevingne', 'Austin Abrams']),
    Movie(title='Begin Again',
          trailer='https://www.youtube.com/watch?v=uTRCxOE7Xzc',
          art='http://ia.media-imdb.com/images/M/MV5BNjAxMTI4M'
              'TgzMV5BMl5BanBnXkFtZTgwOTAwODEwMjE@._V1_SX214_AL_.jpg',
          director='John Carney',
          writers='John Carney',
          stars=['Keira Knightley', 'Mark Ruffalo', 'Adam Levine']),
    Movie(title='The Hangover',
          trailer='https://www.youtube.com/watch?v=KLAkxSjs8ZY',
          art='http://ia.media-imdb.com/images/M/MV5BMTA0NjE1M'
              'zMzODheQTJeQWpwZ15BbWU3MDY4MTQ3Mzk@._V1_SX214_AL_.jpg',
          director='Todd Phillips',
          writers=['Jon Lucas', 'Scott Moore'],
          stars=['Zach Galifianakis', 'Bradley Cooper', 'Justin Bartha']),
]

# Render the web page with the movies
open_movies_page(MOVIES)
