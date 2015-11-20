# -*- coding: utf-8 -*-
# Developer: Andres Anies <andres_anies@hotmail.com>


class Movie(object):
    """
    Movie that has a title an ad, a trailer and little more...
    """
    def __init__(self, title=None, trailer=None, art=None,
                 director=None, writers=None, stars=None):
        """
        Constructor that initialize a movie
        with the minimal required data
        :param title: The name of the movie
        :param trailer: URL of youtube video for watch the trailer
        :param art: URL of an advertising image
        """
        self.trailer_youtube_url = trailer
        self.title = title
        self.poster_image_url = art
        self.director = director
        self._writers_list = writers
        self._stars_list = stars

    @property
    def writers(self):
        """
        Movie writers
        :return: List of movie writers in a user friendly format
        """
        return ', '.join(self._writers_list)

    @property
    def stars(self):
        """
        Movie stars
        :return: List of movie stars in a user friendly format
        """
        return ', '.join(self._stars_list)

