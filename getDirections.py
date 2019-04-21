def getDistanceMatrix(gmaps: 'googlemaps Client', origin: 'latLong', destination: 'latLong'):
    matrix = gmaps.distance_matrix(origins = origin,
                                   destinations = destination,
                                   mode = 'driving',
                                   units = 'imperial')

    return matrix

def getDirections(gmaps: 'googlemaps Client', origin: 'latLong', destination: 'latLong'):
    directions = gmaps.directions(origin = origin,
                                  destination = destination,
                                  mode = 'driving',
                                  units = 'imperial')
    return directions