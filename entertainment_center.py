import media
import fresh_tomatoes

"""
Assign movies:
Caddyshack, Dodgeball, Super Mario Bros,
Oscar, Superman, and Who Framed Roger
Rabbit
"""

# Caddyshack Movie - title, tagline, poster, trailer, imdb
caddyshack = media.Movie("Caddyshack",
                         "A story of a groundskeeper and his "
                         "nemesis, the gopher",
                         "https://images-na.ssl-images-amazon.com/images/I/71pY%2BIj78GL._SY679_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=x9Nl39uWEYk",  # NOQA
                         "http://www.imdb.com/title/tt0080487/")  # NOQA

# Dodgeball Movie - title, tagline, poster, trailer, imdb
dodgeball = media.Movie("Dodgeball",
                        "If you can dodge a wrench, you "
                        "can dodge a ball",
                        "https://images2.vudu.com/poster2/8549-338",  # NOQA
                        "https://www.youtube.com/watch?v=ztLcDpRJl9o",  # NOQA
                        "http://www.imdb.com/title/tt0364725/?ref_=fn_al_tt_1")  # NOQA

# SMB Movie - title, tagline, poster, trailer, imdb
super_mario_bros = media.Movie("Super Mario Bros.",
                               "Hollywood's first attempt"
                               "at a video game movie.",
                               "https://i.pinimg.com/originals/37/df/16/37df1636942888220ce3de103ea0add2.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=wtMZKYnLg5c",  # NOQA
                               "http://www.imdb.com/title/tt0108255/?ref_=fn_al_tt_1")  # NOQA

# Oscar Movie - title, tagline, poster, trailer, imdb
oscar = media.Movie("Oscar",
                    "Stallone, as a funny guy",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Oscar1991poster.jpg/220px-Oscar1991poster.jpg",  # NOQA
                    "www.youtube.com/watch?v=CMMtpC7t4s4",  # NOQA
                    "http://www.imdb.com/title/tt0102603/?ref_=fn_al_tt_1")  # NOQA

# Superman Movie - title, tagline, poster, trailer, imdb
superman = media.Movie("Superman",
                       "Not quite as good as Batman...",
                       "https://static.fnac-static.com/multimedia/FR/images_produits/FR/Fnac.com/ZoomPE/4/3/1/7321950010134/tsp20130828194753/Superman.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=grO4OcJ6cgY",  # NOQA
                       "http://www.imdb.com/title/tt0078346/?ref_=nv_sr_2")  # NOQA

# Who Framed Roger Rabbit Movie - title, tagline, poster, trailer, imdb
who_framed_roger_rabbit = media.Movie("Who Framed Roger Rabbit",
                                      "The only time you will "
                                      "see Mickey and Bugs "
                                      "together...",
                                      "https://i.pinimg.com/originals/db/87/3c/db873c381c960d42c9fd5ea4fffc3fe7.jpg",  # NOQA
                                      "https://www.youtube.com/watch?v=OFCIaMyMORg",  # NOQA
                                      "http://www.imdb.com/title/tt0096438/?ref_=nv_sr_1")  # NOQA

movies = [caddyshack, dodgeball, super_mario_bros,
          oscar, superman, who_framed_roger_rabbit]

fresh_tomatoes.open_movies_page(movies)
