import json
with open('stations.json', 'r') as json_file:
    data = json.load(json_file)
    longtitude = []
    stationlijst = []
    for each in data["payload"]:
        station = each['namen']['lang']
        stationlijst.append(station)
        code = each['code']
        type = each['stationType']
        print('{:23} {}  {:5}  {} {}'.format(station,'-',code,':',type))
        longtitude2 = each['lng']
        longtitude.append(longtitude2)
    index = longtitude.index(max(longtitude))
    print('\nHet meest oostelijk gelegen station is', stationlijst[index])


