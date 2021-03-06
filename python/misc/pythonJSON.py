#!/usr/bin/env python

# # lynda.com - Up and Running with Python
# examples of accessing URLs

import urllib2
import json

def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    count = theJSON["metadata"]["count"];
    print str(count) + " events recorded."
    
#    for i in theJSON["features"]:
#        print i["properties"]["place"]

#    for i in theJSON["features"]:
#        if i["properties"]["mag"] >= 5.0:
#            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
 
    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"
 
        
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"    
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print "Received an error from server, cannot retrieve results." + str(webUrl.getcode)
        
if __name__=="__main__":
    main()
    

'''
    #open a connection to a URL using urllib2
    webUrl = urllib2.urlopen("http://joemarini.com")

    #get the result and print it
    print "result code: " + str(webUrl.getcode())
    data1 = webUrl.read()
    print data1
'''
