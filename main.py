import googlemaps
import getPlaces

def main():
    gmaps = googlemaps.Client(key='AIzaSyA4j2DBPo0Lkk0q1p8zIjGF4PFdTImfCFI')
    # place = input("Please input your destination: ")
    # start = input("Please input your starting time: ")
    place = "7707 Aldea Ave, Van Nuys, CA"
    start = "10:00"
    time = start.split(':') # time[0] = hr; time[1] = min

    placeDict = {}

    initialPlace = getPlaces.getInitialPlace(gmaps, place)
    placeDict[initialPlace[0]] = initialPlace[2]
    print(initialPlace)

    nextPlace = initialPlace

    for i in range(5):
        if i == 1 or i == 4:
            keyword = 'food'
            type = 'restaurant'
        else:
            keyword = 'tourist attractions'
            type = None

        nextPlace = getPlaces.getNearPlace(gmaps, nextPlace[2], keyword, type, placeDict)
        placeDict[nextPlace[0]] = nextPlace[2]
        print(nextPlace)


if __name__ == "__main__":
    main()
