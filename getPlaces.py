# getPlaces.py
# Makes use of the Places API within the Googlemaps API.
# Functions in this module handle locating places located near specified addresses.

def getInitialPlace(gmaps: 'gmapsClient', readableAddress: str):
    """Returns an initial place of interest located near a specified location

    :param gmaps: The googlemaps client object, necessary to call any of the googlemaps API functions
    :type gmaps: googlemaps.Client

    :param readableAddress: The human-readable version of an address, i.e. "123 Bottle Street, Irvine, CA"
    :type readableAddress: str

    :return: list of necessary information for the chosen place
    """
    geocode = gmaps.geocode(address=readableAddress)
    latLong = str(geocode[0]["geometry"]["location"]["lat"]) + "," + str(geocode[0]["geometry"]["location"]["lng"])
    places = gmaps.places(query = "tourist attractions",
                          location = latLong,
                          radius = 32186 # 20 miles
                          )['results']

    i = 0
    isSuitableRating = False
    while not isSuitableRating:
        if places[i]["rating"] >= 4.0:
            place = places[i]
            isSuitableRating = True
        else:
            i += 1

    placeLatLong = str(place["geometry"]["location"]["lat"]) + "," + str(place["geometry"]["location"]["lng"])
    # neLatLong = str(place["geometry"]["viewport"]["northeast"]["lat"]) + "," + str(place["geometry"]["viewport"]["northeast"]["lng"])
    # swLatLong = str(place["geometry"]["viewport"]["southwest"]["lat"]) + "," + str(place["geometry"]["viewport"]["southwest"]["lng"])
    return [place["name"], placeLatLong] #, neLatLong, swLatLong, place["types"]]


def getNearPlace(gmaps: 'gmapsClient', location: 'latLng',  keyword: str, type: 'googlemaps type', placeNames: list):
    """Returns a place near the previous location within a smaller radius

    :param gmaps: The googlemaps client object, necessary to call any of the googlemaps API functions
    :type gmaps: googlemaps.Client

    :param location: The latitude+longitude location of the previous location
    :type location: str

    :param keyword: A word to query for the next location
    :type keyword: str

    :param type: Restricts results to places of a specific type; to use in call to places_nearby
    :type type: str

    :param placeNames: A list containing the previously chosen places
    :type placeNames: list

    :return: list of necessary information for the chosen place
    """
    places = gmaps.places_nearby(location = location,
                                    # radius = 4828, # 2 miles
                                    keyword = keyword,
                                    type = type,
                                    rank_by = 'distance' # remove if we want to rank by prominence
                                    )['results']
    i = 0
    isSatisfactory = False

    while not isSatisfactory:
        if places[i]["name"] in placeNames or places[i]["rating"] < 4.0:
            i += 1
        else:
            nextPlace = places[i]
            isSatisfactory = True

    placeLatLong = str(nextPlace["geometry"]["location"]["lat"]) + "," + str(nextPlace["geometry"]["location"]["lng"])
    # neLatLong = str(nextPlace["geometry"]["viewport"]["northeast"]["lat"]) + "," + str(nextPlace["geometry"]["viewport"]["northeast"]["lng"])
    # swLatLong = str(nextPlace["geometry"]["viewport"]["southwest"]["lat"]) + "," + str(nextPlace["geometry"]["viewport"]["southwest"]["lng"])
    return [nextPlace["name"], placeLatLong] #, neLatLong, swLatLong, nextPlace["types"]]




