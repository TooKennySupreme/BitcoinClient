import shodan
import time
import requests
import json

GOOGLEMAPS_API_KEY = "AIzaSyCvdA9pmAodt1JknfuvTYoIuf9K5IUxwQo"

GOOGLEMAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&key={2}"

SHODAN_API_KEY = "pL2Xta897UmrCxHByAlkB08Xp5PjHM8h"

api = shodan.Shodan(SHODAN_API_KEY)

ipFile = open("ip.txt","r")

IpInfoFile = open("ipInfo.txt","w")

UniversitiesFIle = open("UniversitiesAddresses.txt","r")

for line in ipFile:

	# Lookup the host
	host = api.host(line)

	if(host['latitude'] == None or host['longitude'] == None):
		continue
	else:
		#TEST FUNDAO
		response = requests.get(GOOGLEMAPS_API_URL.format("-22.8596589","-43.2303241",GOOGLEMAPS_API_KEY))
		#REAL GET
#		response = requests.get(GOOGLEMAPS_API_URL.format(host['latitude'],host['longitude'],GOOGLEMAPS_API_KEY))
		json_data = json.loads(response.text)
		# print formatted address for debug
		for addressComponent in json_data['results']:
			print(addressComponent['formatted_address'])
		# Print general info
		print ("IP: {0}\ncountry: {1}\ncity: {2}\nlongitude: {3}\nlatitude: {4}".format(host['ip_str'], host['country_code'],host['city'], host['latitude'], host['longitude']))


		IpInfoFile.write("IP: {0}\tcountry: {1}\tcity: {2}\tlongitude: {3}\tlatitude: {4}\n".format(host['ip_str'], host['country_code'],host['city'], host['latitude'], host['longitude']))
		IpInfoFile.flush()
	time.sleep(2)