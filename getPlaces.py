def getInitialPlace(gmaps: 'gmapsClient', readableAddress: str):
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
    return [place["name"], place["formatted_address"], placeLatLong, place["rating"]]


def getNearPlace(gmaps: 'gmapsClient', location: 'latLng',  keyword: str, type: 'googlemaps type', placeNames: list):
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
    return [nextPlace["name"], nextPlace["vicinity"], placeLatLong, nextPlace["rating"]]




