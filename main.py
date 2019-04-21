import googlemaps
import getPlaces
import getDirections

def main():
    keyFile = open('googlemapsKey.txt', 'r')
    key = keyFile.read()
    keyFile.close()

    gmaps = googlemaps.Client(key=key)
    # place = input("Please input your destination: ")
    # start = input("Please input your starting time: ")
    place = "7707 Aldea Ave, Van Nuys, CA"
    # start = "10:00"
    # time = start.split(':') # time[0] = hr; time[1] = min

    placeDict = {}
    placeNames = [] # needed to keep order of destinations

    initialPlace = getPlaces.getInitialPlace(gmaps, place)
    placeDict[initialPlace[0]] = initialPlace[2]
    placeNames.append(initialPlace[0])
    print(initialPlace)

    nextPlace = initialPlace

    for i in range(5):
        if i == 1 or i == 4:
            keyword = 'food'
            type = 'restaurant'
        else:
            keyword = 'tourist attractions'
            type = None

        nextPlace = getPlaces.getNearPlace(gmaps, nextPlace[2], keyword, type, placeNames)
        placeDict[nextPlace[0]] = nextPlace[2]
        placeNames.append(nextPlace[0])
        print(nextPlace)

    for i in range(len(placeNames) - 1):
        matrix = getDirections.getDistanceMatrix(gmaps, placeDict[placeNames[i]], placeDict[placeNames[i+1]])
        strVal = "From: {} ({})\nTo: {} ({})\n{} ({})\n".format(placeNames[i], matrix['origin_addresses'][0],
                                                              placeNames[i+1], matrix['destination_addresses'][0],
                                                              matrix['rows'][0]['elements'][0]['duration']['text'],
                                                              matrix['rows'][0]['elements'][0]['distance']['text'])
        print(strVal)

        directions = getDirections.getDirections(gmaps, placeDict[placeNames[i]], placeDict[placeNames[i+1]])
        # print(directions[0]['legs'][0].keys())
        for direction in directions[0]['legs'][0]['steps']:
            dirString = "{}\n{}".format(direction['html_instructions'], direction['distance']['text'])
            print(dirString)
        print()

    print('Map data ©2019 Google')


if __name__ == "__main__":
    main()


