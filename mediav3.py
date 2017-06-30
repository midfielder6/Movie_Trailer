import webbrowser


class Video():
    """ This class is the parent class object and stores common video data
        used by both child classes Movie and Series (title, poster image file
        and youtube url).

        The built-in method __init__ known as constructor - initializes
        new instances and creates memory space for the instance. The 1st
        argument of the init method is called 'self'; 'self' represents the
        instance of the object itself.

        Note: The name 'self' has no special meaning to Python but is used as a
        common naming convention. Not following this convention may make your
        code less readable to other Python programmers.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # def show_trailer(self):
        # webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """ This class is a child of the parent class Video and stores detailed
        movie data. It inherits the parent class attributes (title, poster, and
        youtube url) and defines the unique instance varibles for
        class(Movie) - lead_1, lead_2 and lead_3 (cast member leads), movie
        director, film rating (G, PG, R, etc.) and a brief plot summary or
        storyline).
    """

    def __init__(self, movie_title, poster_image, trailer_youtube,
                 lead_1, lead_2, lead_3, director, rating, storyline):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.lead_1 = lead_1
        self.lead_2 = lead_2
        self.lead_3 = lead_3
        self.director = director
        self.rating = rating
        self.storyline = storyline


class Series(Video):
    """ This class is a child of the parent class Video and stores TV Series
        information. It inherits parent class attributes (movie, poster,
        trailer) and defines unique instance varibles for class(Series); series
        main character, duration (years in production), creator (writers),
        last three season episode production dates, the network producer.

        The class also includes an instance method show_episode_summ() which
        leverages Google to access TV Series web pages
    """

    def __init__(self, movie_title, poster_image, trailer_youtube, mainchar,
                 duration, creator, episode, producer):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.series_mainchar = mainchar
        self.series_duration = duration
        self.series_creator = creator
        self.series_episode = episode
        self.series_producer = producer

    def show_episode_summ(self):
        google = raw_input('Episode Summary which Series to Google Search:')
        # print "See webpage: " + self.title + " " + self.series_producer
        webbrowser.open_new_tab(
            'http://www.google.com/search?btnG=1&q=%s' % google)
