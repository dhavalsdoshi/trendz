import httplib
import csv
from xml.dom import minidom                                          

xmldoc = minidom.parse('countries.xml')  
csvWriter = csv.writer(open('countries.csv', 'wb'), delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
csvWriter.writerow(['country', 'woeid','clatitude','clongitude'])
places = xmldoc.getElementsByTagName('place')
for place in xmldoc.getElementsByTagName("place"):
	woeid = place.getElementsByTagName("woeid")[0].firstChild.data
	name = place.getElementsByTagName("name")[0].firstChild.data
	print name
	
	conn = httplib.HTTPConnection("where.yahooapis.com")
	conn.request("GET", "/v1/place/"+woeid+"?appid=3jqX4VbV34FfP82R7MppZARRfxaAFHjuTmtKCpB7Uab47s_1ECohhR3vcjAWkOYjxaP1")
	r1 = conn.getresponse()
	print r1.status, r1.reason
	data1 = r1.read()
	xmldoc2 = minidom.parseString(data1)
	centroid = xmldoc2.getElementsByTagName('centroid')[0]
	latitude=centroid.getElementsByTagName('latitude')[0].firstChild.data
	longitude=centroid.getElementsByTagName('longitude')[0].firstChild.data
	csvWriter.writerow([name,woeid,latitude,longitude])
