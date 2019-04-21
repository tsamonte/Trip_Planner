# getDirections.py
# Makes use of the Directions API and DistanceMatrix API within the googlemaps API
# Functions within this module handle generating directions, travel times, and distances

def getDistanceMatrix(gmaps: 'googlemaps Client', origin: 'latLong', destination: 'latLong'):
    """Returns a distance matrix based on the specified origin and destination

    :param gmaps: The googlemaps client object, necessary to call any of the googlemaps API functions
    :type gmaps: googlemaps.Client

    :param origin: The latitude+longitude location of the starting point
    :type origin: str

    :param destination: The latitude+longitude location of the ending point
    :type destination: str

    :return: a distance matrix
    """
    matrix = gmaps.distance_matrix(origins = origin,
                                   destinations = destination,
                                   mode = 'driving',
                                   units = 'imperial')

    return matrix

def getDirections(gmaps: 'googlemaps Client', origin: 'latLong', destination: 'latLong'):
    """Returns the set of directions from the origin to the destination

    :param gmaps: The googlemaps client object, necessary to call any of the googlemaps API functions
    :type gmaps: googlemaps.Client

    :param origin: The latitude+longitude location of the starting point
    :type origin: str

    :param destination: The latitude+longitude location of the ending point
    :type destination: str

    :return: a directions object
    """
    directions = gmaps.directions(origin = origin,
                                  destination = destination,
                                  mode = 'driving',
                                  units = 'imperial')
    return directions