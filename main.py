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
    start = "10:00"
    time = start.split(':') # time[0] = hr; time[1] = min

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

    getDirections.getDistanceMatrix(gmaps, placeNames, placeDict)


if __name__ == "__main__":
    main()
