import googlemaps
import getPlaces # getPlaces.py
import getDirections # getDirections.py
# import formatJson

def generatePlan(area: str):
    # keyFile = open('googlemapsKey.txt', 'r')
    # key = keyFile.read()
    # keyFile.close()

    gmaps = googlemaps.Client(key='AIzaSyA4j2DBPo0Lkk0q1p8zIjGF4PFdTImfCFI')

    place = area

    returnDict = {}
    returnDict['legs'] = []

    placeDict = {}
    placeNames = [] # needed to keep order of destinations

    initialPlace = getPlaces.getInitialPlace(gmaps, place)
    placeDict[initialPlace[0]] = initialPlace[1]
    placeNames.append(initialPlace[0])
    print("hi1")
    # print(initialPlace)

    nextPlace = initialPlace

    for i in range(5):
        if i == 1 or i == 4:
            keyword = 'food'
            type = 'restaurant'
        else:
            keyword = 'tourist attractions'
            type = None

        nextPlace = getPlaces.getNearPlace(gmaps, nextPlace[1], keyword, type, placeNames)
        placeDict[nextPlace[0]] = nextPlace[1]
        placeNames.append(nextPlace[0])
        # print(nextPlace)
        print("hi2")

    for i in range(len(placeNames) - 1):
        matrix = getDirections.getDistanceMatrix(gmaps, placeDict[placeNames[i]], placeDict[placeNames[i+1]])
        # strVal = "From: {} ({})\nTo: {} ({})\n\t<small>{} ({})</small>\n".format(
        #     placeNames[i], matrix['origin_addresses'][0],
        #     placeNames[i+1], matrix['destination_addresses'][0],
        #     matrix['rows'][0]['elements'][0]['duration']['text'],
        #     matrix['rows'][0]['elements'][0]['distance']['text'])
        # # print(strVal)
        addDict = {}
        addDict['start'] = {}
        start = addDict['start']
        start['name'] = placeNames[i]
        start['address'] = matrix['origin_addresses'][0]
        start['latLong'] = placeDict[placeNames[i]]
        addDict['end'] = {}
        end = addDict['end']
        end['name'] = placeNames[i+1]
        end['address'] = matrix['destination_addresses'][0]
        end['latLong'] = placeDict[placeNames[i+1]]
        addDict['trip_duration'] = matrix['rows'][0]['elements'][0]['duration']['text']
        addDict['trip_distance'] = matrix['rows'][0]['elements'][0]['distance']['text']
        print("hi3")

        directions = getDirections.getDirections(gmaps, placeDict[placeNames[i]], placeDict[placeNames[i+1]])
        addDict['steps'] = []
        for direction in directions[0]['legs'][0]['steps']:
            dirString = "{} ({})".format(direction['html_instructions'], direction['distance']['text'])
            # print(dirString)
            addDict['steps'].append(dirString)
        # print()

        returnDict['legs'].append(addDict)

    # print('Map data ©2019 Google')
    returnDict['copyrights'] = 'Map data ©2019 Google'
    # print(formatJson.formatJSON(returnDict))
    print(returnDict)
    return [returnDict]

if __name__ == "__main__":
    generatePlan('')



