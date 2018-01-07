import shodan
import time

SHODAN_API_KEY = "pL2Xta897UmrCxHByAlkB08Xp5PjHM8h"

api = shodan.Shodan(SHODAN_API_KEY)

file = open("ip.txt","r")

for line in file:

	# Lookup the host
	host = api.host(line)

	# Print general info
	print ("""
			IP: %s
			Organization: %s
			Operating System: %s
			country: %s
			city: %s
			longitude: %s
			latitude: %s
	""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host['country_code'],host['city'], host['latitude'], host['longitude']))
	time.sleep(2)


# Print all banners
# for item in host['data']:
#         print ("""
#                 Port: %s
#                 Banner: %s
#        """ % (item['port'], item['data']))