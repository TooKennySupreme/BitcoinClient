import time
import requests
import json

LATEST_BLOCK_API = "https://blockchain.info/pt/q/latesthash"

BLOCK_INFO = "https://blockchain.info/pt/rawblock/{0}"

lastBlockHash = ""

ipFile = open("ip.txt","w")

delay = 10

analyzerError = open("blockError.txt", "w")

while True:
	try:
		print("Getting latest block hash. . .\n")
		response = requests.get(LATEST_BLOCK_API)
		if response == None or response == "":
			print("Empty response on latest block hash! Trying again!\n")
			pass
		else:
			latestBlockHash = response.text
			#Check if its the same ip viewed at last time to minimize duplicate
			if lastBlockHash != latestBlockHash:
				print("Getting latest block info. . .\n")
				response = requests.get(BLOCK_INFO.format(latestBlockHash))
				if response == None or response == "":
					print("Empty response on latest block info! Trying again!\n")
					pass
				else:
					json_data = json.loads(response.text)
					ipFile.write(json_data["relayed_by"]+"\n")
					ipFile.flush()
					#update viewd block
					lastBlockHash = latestBlockHash
			else:
				print("Block recent viewd!\n")
				pass
	except Exception as e:
		print("Unknow error :{0}".format(e))
		analyzerError.write("Error:{0} \t response: {1}\n".format(e,response.text))
		analyzerError.flush()
	print("Waiting {0} seconds. . .\n".format(delay))
	time.sleep(delay)