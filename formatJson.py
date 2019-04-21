def formatJSON(json: dict):
    outputString = \
"""{
 'legs':
        ["""
    for i in range(len(json['legs'])):
        current = json['legs'][i]
        addString = \
"""{{'start' : {{ 'name' : {}, 'address': {} }},
          'end'    : {{ 'name' : {}, 'address': {} }},
          'trip_duration' : {},
          'trip_distance' : {},
          'steps': {}
         }},
         """
        newStr = addString.format(current['start']['name'], current['start']['address'],
                                  current['end']['name'], current['end']['address'],
                                  current['trip_duration'],
                                  current['trip_distance'],
                                  str(current['steps']))
        outputString += newStr
    endAdd = \
"""],
 'copyrights' : 'Map data ©2019 Google'
}
"""
    outputString += endAdd

    return outputString
    return outputString