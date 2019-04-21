#mapwriter.py
import webbrowser
import os

"""
Script to rewrite html display when user enters a location to view. 
"""

##############################################################################

# <meta http-equiv="refresh" content="5">
# add this under metas for manual refresh

def newScript(x,y) -> str:
    ''' Rewrites new html script given latitude and longitude coords '''
    html_script = '''<!DOCTYPE html>
<html>
  <head>
    <title>Dont Trip! | Display</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/custom.css">
    <script src="js/mapfunctions.js"></script>
    <script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyA4j2DBPo0Lkk0q1p8zIjGF4PFdTImfCFI&callback=initMap" ></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
  </head>
  <body>
    <div class = "wrap">
        <div id="map">
        <script>
            var x ='''+ str(x) + ''';
            var y ='''+ str(y) + ''';
            var map = initMap(x,y);
            var markerArray = [];
            document.write('hello');
        </script>
        </div>
        <div id="right">
            <div id="title">
                <h1>Don't Trip, We Gotchu!</h1>
            </div>
        <p>Where we droppin?</p>
        <div class = "container">
            <select id="dropdown" onchange="deleteMarkers(map, markerArray);addMarker(map, markerArray)">
                <option>Choose a City</option>
            </select>
            <script>
                dropDownList();
            </script>
        </div>
        </div>
    </div>
  </body>
</html>
'''
    return html_script

def writeToFile(text, filename):
    ''' Writes contents to an html file '''
    f = open(filename, "w")
    f.write(text)
    f.close();
    return

def openHTMLInBrowser(filename):
    webbrowser.open('file://' + os.path.realpath(filename), new=0)
    

if __name__ == "__main__":
    lat = input('Enter lat: ')
    long = input('Enter long: ')
    result = newScript(lat, long)
    writeToFile(result, "travel.html")
    openHTMLInBrowser("travel.html")

    
    
