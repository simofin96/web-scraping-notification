# Source: https://www.geeksforgeeks.org/python-script-to-monitor-website-changes/
# Website to monitor: https://www.idays.it/tickets

import hashlib
import re
import time
import urllib.request


def clean_data(data):
	string_data = data.decode("utf-8")
	cleaned_string_data = re.sub(r"<!--.*?-->", "", string_data) # delete HTML comments
	cleaned_data = cleaned_string_data.encode("utf-8")
	return cleaned_data

# setting the URL you want to monitor
url = "https://store.steampowered.com/?l=italian"

# perform a GET request and load the content of the website
page = urllib.request.urlopen(url)
response = page.read()
response = clean_data(response)

# create the initial hash 
currentHash = hashlib.sha224(response).hexdigest() 

print("running") 
while True: 
	time.sleep(2) # time waited between requests 

	try:
		# perform the get request
		page = urllib.request.urlopen(url)
		response = page.read()
		response = clean_data(response) 

		# create a hash 
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash 
		if newHash == currentHash: 
			print(currentHash)
			continue
		else: 
			# notify 
			print("something changed")
			print(currentHash)
			currentHash = newHash
			continue

	except Exception as e: 
		print("error") 

