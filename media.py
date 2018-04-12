import webbrowser


class Movie():

    """
    This is the Movie class file.
    It stores movie information
    for the user's selected movies
    """

    def __init__(self,
                 title,
                 tagline,
                 poster_image_url,
                 trailer_youtube_url,
                 imdb_link):
        """
        Constructor to initialize:
        title as string
        tagline as string
        poster_image_url as string
        trailer_youtube_url as string
        imdb_link as string
        """
        self.title = title
        self.tagline = tagline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_link = imdb_link
        print("Added: " + self.title)

    def show_trailer(self):
        """
        Opens the trailer url
        """
        webbrowser.open(self.trailer_youtube_url)
