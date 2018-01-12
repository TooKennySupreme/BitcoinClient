import shodan
import time
import requests
import json

from geopy.distance import great_circle

#GOOGLEMAPS_API_KEY = "AIzaSyCvdA9pmAodt1JknfuvTYoIuf9K5IUxwQo"

#GOOGLEMAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&key={2}"

SHODAN_API_KEY = "pL2Xta897UmrCxHByAlkB08Xp5PjHM8h"

api = shodan.Shodan(SHODAN_API_KEY)

ipFile = open("ip.txt","r")

IpInfoFile = open("ipInfo.txt","w")

UniversitiesFile = open("UniversitiesAddresses.txt","r")

statsFile =  open("stats.txt","w")

universitiesLatLong = []

for line in UniversitiesFile:
	split = line.replace("\n","").split(",")
	universitiesLatLong.append([float(split[0]), float(split[1])])

ipCount = {}
CountryCount = {}

for line in ipFile:
	try:
	
		ip = line.split("\t")[0].split(":")[0]

		host = api.host(ip)

		if ip in ipCount:
			ipCount[ip] += 1
		else:
			ipCount[ip] = 1

		if host['country_code'] in CountryCount:
			CountryCount[host['country_code']] += 1
		else:
			CountryCount[host['country_code']] = 1

		if(host['latitude'] == None or host['longitude'] == None):
			continue
		else:
			ipLatLong = (host['latitude'],host['longitude'])
			for UniversityLatLong in universitiesLatLong:
				distance = great_circle((UniversityLatLong[0],UniversityLatLong[1]),ipLatLong).miles
				if(distance < 0.12):
					print("Possible positive: {0}".format(ip))
	except Exception as e:
		print("Unknow error :{0}".format(e))
	time.sleep(5)
statsFile.write(json.dumps(ipCount) + "\n")
statsFile.write(json.dumps(CountryCount) + "\n")
statsFile.flush()