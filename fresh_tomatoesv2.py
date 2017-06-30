import mediav3
import webbrowser
import os
import re

# Styles and scripting for the page
# This version of fresh_tomatoes was retrieved from web written by James Childs-Maidment (thisbejim)
# Made changes to it to account for my new classe defintions, instances and variables.

main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Video Highlights</title>
    <link rel="icon" href="assets/favicon.ico">
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animate.css">
    <link rel="stylesheet" href="css/font-awesome/css/font-awesome.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?modestbranding=1;autohide=1&amp;showinfo=0&amp;controls=0;autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            // Add movie / series information to the modal
            var title = $(this).attr('data-title')
            var lead_act_1 = $(this).attr('data-lead1')
            var lead_act_2 = $(this).attr('data-lead2')
            var lead_act_3 = $(this).attr('data-lead3')
            var director = $(this).attr('data-director')
            var this_rating = $(this).attr('data-rate')
            $("#actor-info").empty().append($("<div> Director / Producer: "+director+".</p><p>Cast: "+lead_act_1+", "+lead_act_2+", "+lead_act_3+".</p>"+"</div>"));
            $("#this_title").empty().append($("<h2>"+title+"</h2>"));
            $("#logo-info").empty().append($('<img />').attr('src', 'assets/lookout.svg').attr('height', '50px'));
            // Add rating to the the modal
            $("#rating").empty();
            var i;
            for (i = 0; i < this_rating; i++) {
            $("#rating").append($("<i class='fa fa-star'></i>"));
            }
            t = 5 - this_rating;
            for (i = 0; i < t; i++) {
            $("#rating").append($("<i class='fa fa-star-o'></i>"));
            }
            $("i").animate({opacity: 0}, 100).first().animate({opacity: 1}, 600, function showNext() {
            $(this).next("i").animate({opacity:1}, 600, showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog animated fadeIn">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true"><img src="assets/exit.svg" height=25 width=25></a>
                <div class="row">
                    <div class="col-md-11" id="this_title"></div>
                    <div class="col-md-11" id="actor-info"></div>
                    <div class="col-md-11" id="rating"></div>
                </div>
                <div class="scale-media" id="trailer-video-container"></div>
            </div>
        </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Favorite Video Trailers</a>
          </div>
            <a class="navbar-text navbar-right">Select Video Poster for Preview</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center animated bounceInRight" data-trailer-youtube-id="{trailer_youtube_id}"
data-lead1="{lead_1}" data-lead2="{lead_2}" data-lead3="{lead_3}" data-director="{director}" data-rate="{rating}" data-title="{movie_title}"
data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="176" height="223">
    <h2>{movie_title}</h2>
    <p>{storyline}</p>
</div>
'''
# A single movie entry html template
movie_tile_content2 = '''
<div class="col-md-6 col-lg-4 movie-tile text-center animated bounceInRight" data-trailer-youtube-id="{trailer_youtube_id}"
data-lead1="{main_character}" data-lead2="{series_duration}" data-lead3="{series_creator}" data-director="{series_producer}" data-title="{movie_title}"
data-rate="{series_duration}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="176" height="223">
    <h2>{movie_title}</h2>
    <p>{series_episode}</p>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        # Append the tile for the movie with its content filled in
        if (isinstance(movie, mediav3.Movie)):
            content += movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                lead_1=movie.lead_1,
                lead_2=movie.lead_2,
                lead_3=movie.lead_3,
                director=movie.director,
                rating=movie.rating,
                storyline=movie.storyline
            )
    return content

def create_movie_tiles_content2(series):
    # The HTML content for this section of the page
    content = ''
    for movie in series:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        # Append the tile with TV Series data with its content filled in
        if (isinstance(movie, mediav3.Series)):
            content += movie_tile_content2.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                main_character=movie.series_mainchar,
                series_duration=movie.series_duration,
                series_creator=movie.series_creator,
                series_episode=movie.series_episode,
                series_producer=movie.series_producer
            )
    return content

def open_movies_page(movies,series):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')
  # Replace the placeholder for the video tiles with the actual dynamically generated content
  # "Render content for Movie Instance."
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
  # "Render content for Series Instance."
  rendered_content += main_page_content.format(movie_tiles=create_movie_tiles_content2(series))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
