import media
import fresh_tomatoes

caddyshack = media.Movie("Caddyshack",
                         "A story of a groundskeeper and his "
                         "nemesis, the gopher",
                         "https://images-na.ssl-images-amaz"
                         "on.com/images/I/71pY%2BIj78GL."
                         "_SY679_.jpg",
                         "https://www.youtube.com/"
                         "watch?v=x9Nl39uWEYk",
                         "http://www.imdb.com/"
                         "title/tt0080487/")

dodgeball = media.Movie("Dodgeball",
                        "If you can dodge a wrench, you "
                        "can dodge a ball",
                        "https://images2.vudu.com"
                        "/poster2/8549-338",
                        "https://www.youtube.com"
                        "/watch?v=ztLcDpRJl9o",
                        "http://www.imdb.com/title"
                        "/tt0364725/?ref_=fn_al_tt_1")

super_mario_bros = media.Movie("Super Mario Bros.",
                               "Hollywood's first attempt"
                               "at a video game movie.",
                               "https://i.pinimg.com/"
                               "originals/37/df/16/37df"
                               "1636942888220ce3de103ea0"
                               "add2.jpg",
                               "https://www.youtube.com"
                               "/watch?v=wtMZKYnLg5c",
                               "http://www.imdb.com/ti"
                               "tle/tt0108255"
                               "/?ref_=fn_al_tt_1")

oscar = media.Movie("Oscar",
                    "Stallone, as a funny guy",
                    "https://upload.wikimedia."
                    "org/wikipedia/en/thumb/3/31/"
                    "Oscar1991poster.jpg/"
                    "220px-Oscar1991poster.jpg",
                    "www.youtube.com/watch?v="
                    "CMMtpC7t4s4",
                    "http://www.imdb.com/title"
                    "/tt0102603/?ref_=fn_al_tt_1")

superman = media.Movie("Superman",
                       "Not quite as good as Batman...",
                       "https://static.fnac-static.com/"
                       "multimedia/FR/images_produits"
                       "/FR/Fnac.com/ZoomPE/4/3/1/"
                       "7321950010134/tsp20130828194753"
                       "/Superman.jpg",
                       "https://www.youtube.com"
                       "/watch?v=grO4OcJ6cgY",
                       "http://www.imdb.com"
                       "/title/tt0078346/?ref_=nv_sr_2")

who_framed_roger_rabbit = media.Movie("Who Framed Roger Rabbit",
                                      "The only time you will "
                                      "see Mickey and Bugs "
                                      "together...",
                                      "https://i.pinimg.com/"
                                      "originals/db/87/3c/db87"
                                      "3c381c960d42c9fd5ea4"
                                      "fffc3fe7.jpg",
                                      "https://www.youtube."
                                      "com/watch?v=OFCIaMyMORg",
                                      "http://www.imdb.com/"
                                      "title/tt0096438/?ref"
                                      "_=nv_sr_1")

movies = [caddyshack, dodgeball, super_mario_bros,
          oscar, superman, who_framed_roger_rabbit]

fresh_tomatoes.open_movies_page(movies)
