import json
import urllib.request

def Results(url):
    #Open the URL, and load the string data into dictionary
    data=urllib.request.urlopen(url)
    earthquake_json=json.load(data)

    #Title
    print(earthquake_json['metadata']['title'])

    #Output the number of events 
    print(str(earthquake_json['metadata']['count']) + " events recorded")
    print("------------\n")

    #Print the events events in oceanic regions (Tsunami)
    print('The events in oceanic regions (Tsunami):')
    for i in earthquake_json['features']:
        if i['properties']['tsunami']==1:
            print("%2.1f" % i['properties']['mag'],i['properties']['place'])
    print("------------\n")

    #Print the events having magnitude greater than 6.0
    #Ignore the events having null data of magnitude ("mag":null)    
    print('The events having magnitude greater than 6.0:')
    for i in earthquake_json["features"]:
        if i['properties']['mag']!=None and i['properties']['mag']>=6.0:
            print("%2.1f" % i['properties']['mag'], i['properties']['place'])
    
#The feeds includes all the earthquakes of past 30 days
Results("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    
    

    

    
