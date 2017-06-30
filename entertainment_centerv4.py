'''
This program file defines the instances defined in mediav3 for the child
classes Movie and Series.

The instances for class name Movie are ronin, casablanca and vinny.
The instances for class name Series are homeland, mash and frasier.

Each of the instances below define the data to be stored in each of the
instance variables (see mediav3).

Google's URL Shortener (https://goo.gl/) used for a few poster URLs
to meet PEP8 format standards.
'''

import mediav3
import fresh_tomatoesv2

ronin = mediav3.Movie(
                "RONIN",
                "https://goo.gl/SDAJws",
                "https://www.youtube.com/watch?v=EkJq5RPu-EY",
                "Robert DeNiro",
                "Jean Reno",
                "Natascha McElhone",
                "John Frankenheimer",
                "R",
                "A group of international freelancers assemble for one mission \
                 track down a mysterios package")

casablanca = mediav3.Movie(
                "Casablanca",
                "https://goo.gl/sYfksW",
                "https://www.youtube.com/watch?v=jQTWfGOv1JY",
                "Humphrey Bogart",
                "Ingrid Bergman",
                "Paul Heireid",
                "Michael Curtiz",
                "PG",
                "Casablanca, Rick who owns a nightclub in Casablanca during \
                 WWII is faced with life changing decsions.")

vinny = mediav3.Movie(
                "My Cousin Vinny",
                "https://goo.gl/cPZ3X4",
                "https://www.youtube.com/watch?v=SL4HdaZXuOw",
                "Marissa Tomei",
                "Joe Pesci",
                "Fred Gwynne",
                "Jonathan Lynn",
                "R",
                "NYC lawyer Vinny has never won a case. When his cousin is \
                 accused of murder, Vinny must take the case.")

homeland = mediav3.Series(
                "Homeland",
                "https://i.ytimg.com/vi/YtxejzHA8vo/hqdefault.jpg",
                "https://www.youtube.com/watch?v=vuZtSIAocgE",
                "CIA Officer Carrie Mathison",
                "Years - 2011 through 2017",
                "Created by Gideon Raff",
                "Season/Episodes<br>4 - 12 ...Oct 5,2014 - Dec 21,2014<br>5 - \
                 12 ...Oct 4, 2015 - Dec 20,2015<br>6  - 12 ...Jan 15, 2017 \
                 - Apr 9,2017",
                "Showtime")

mash = mediav3.Series(
                "M*A*S*H",
                "https://cordcutting.com/wp-content/uploads/2015/06/MASH.jpg",
                "https://www.youtube.com/watch?v=1xlvJQXRtvM",
                "Captain Hawkeye Pearce",
                "Years - 1972 through 1983",
                "Created by Larry Gelbart & Gene Reynolds",
                "Season/Episodes<br>9	- 20 ...Nov 1980 - May 1981<br>10 - \
                 22 ...Oct 1981 - Apr 1982<br>11  -  16 ...Oct 1982 - \
                 Feb 1983",
                "CBS")

frasier = mediav3.Series(
                "Frasier",
                "https://goo.gl/omkt8j",
                "https://www.youtube.com/watch?v=mNJlNJ6XfGA",
                "Doctor Frasier Crane",
                "Years - 1993 through 2004",
                "Created by David Angell, Peter Casey & David Lee ",
                "Season/Episodes<br>9  - 24 ... Sep 2001 - May 2002<br>10 - \
                 24...Sep 2002 - May 2003<br>11  -  24 ...Sep 2003 - May 2004",
                "NBC")

# python lists passed to fresh_tomatoesv2.py
movies = [ronin, casablanca, vinny]
series = [homeland, mash, frasier]
# Output to console the application's Class documentation
print "Video" + mediav3.Video.__doc__ + "\nMovie" + mediav3.Movie.__doc__ + \
 "\nSeries" + mediav3.Series.__doc__
# Build Movie Trailer Webpage using fresh_tomatoesv2.py
fresh_tomatoesv2.open_movies_page(movies, series)
