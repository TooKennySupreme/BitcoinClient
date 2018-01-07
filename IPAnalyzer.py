import shodan
import time

SHODAN_API_KEY = "pL2Xta897UmrCxHByAlkB08Xp5PjHM8h"

api = shodan.Shodan(SHODAN_API_KEY)

ipFile = open("ip.txt","r")

IpInfoFile = open("ipInfo.txt","w")

for line in ipFile:

	# Lookup the host
	host = api.host(line)

	# Print general info
	print ("IP: {0}\ncountry: {1}\ncity: {2}\nlongitude: {3}\nlatitude: {4}".format(host['ip_str'], host['country_code'],host['city'], host['latitude'], host['longitude']))
	IpInfoFile.write("IP: {0}\tcountry: {1}\tcity: {2}\tlongitude: {3}\tlatitude: {4}\n".format(host['ip_str'], host['country_code'],host['city'], host['latitude'], host['longitude']))
	IpInfoFile.flush()
	time.sleep(2)


# Print all banners
# for item in host['data']:
#         print ("""
#                 Port: %s
#                 Banner: %s
#        """ % (item['port'], item['data']))