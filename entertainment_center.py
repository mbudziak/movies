## This file instantiates Movie objects, creates a list of the objects
##  and sends the list to the fresh_tomatos.open_movies_page method
## Import media for the Movie class
## Import fresh_tomatos for the open_movies_page class
import media
import fresh_tomatos

back_to_the_future = media.Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
                                 "http://www.movieposter.com/posters/archive/main/50/MPW-25074",
                                 "https://www.youtube.com/watch?v=yosuvf7Unmg")


weekend_at_bernies = media.Movie("Weekend At Bernie's",
                                 "A pair of losers try to pretend that their murdered employer is really alive, but the murderer is out to \"finish him off\".",
                                 "http://images.moviepostershop.com/weekend-at-bernies-movie-poster-1989-1020297739.jpg",
                                 "https://www.youtube.com/watch?v=YCTgcZ6ImsQ")

indiana_jones = media.Movie("Raiders of the Lost Arc",
                            "Archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
                            "https://knoji.com/images/user/raidersoflostarkonesheet.jpg",
                            "https://www.youtube.com/watch?v=0ZOcoxjeUYo")

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "A high school wise guy is determined to have a day off from school, despite what the principal thinks of that.",
                             "http://images.moviepostershop.com/ferris-buellers-day-off-movie-poster-1986-1010244206.jpg",
                             "https://www.youtube.com/watch?v=R-P6p86px6U")

hunger_games = media.Movie("The Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
                           "http://www.hungergamesdwtc.net/wp-content/uploads/2014/02/The-Hunger-Games-Poster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

revenge_of_the_electric_car = media.Movie("Revenge of the Electric Car",
                                          "Director Chris Paine takes his film crew behind the closed doors of Nissan, GM, and the Silicon Valley start-up Tesla Motors to chronicle the story of the global resurgence of electric cars.",
                                          "https://is5-ssl.mzstatic.com/image/thumb/Video/v4/10/4b/a0/104ba02f-edcf-1605-f54d-1b62ee0baf13/source/800x1200sr.jpg",
                                          "https://www.youtube.com/watch?v=po1XA6l19Mk")

# Create list of Movie objects to send to the fresh_tomatos.open_movies_page method
movies = [back_to_the_future, weekend_at_bernies, indiana_jones, ferris_bueller, hunger_games, revenge_of_the_electric_car]

# Create webpage by sending list of Movie objects to the fresh_tomotos.open_movie_page method
fresh_tomatos.open_movies_page(movies)
