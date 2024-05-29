# Source: https://www.geeksforgeeks.org/python-script-to-monitor-website-changes/
# Website to monitor: https://www.idays.it/tickets

import hashlib

# Importing libraries 
import time
import urllib.request

# setting the URL you want to monitor
url = "https://www.geeksforgeeks.org"

# to perform a GET request and load the 
# content of the website and store it in a var 
page = urllib.request.urlopen(url)
response = page.read()

# to create the initial hash 
currentHash = hashlib.sha224(response).hexdigest() 
print("running") 
time.sleep(10) 
while True: 
	try:
		# perform the get request and store it in a var 
		page = urllib.request.urlopen(url)
		response = page.read() 

		# create a hash 
		currentHash = hashlib.sha224(response).hexdigest() 

		# wait for 30 seconds 
		time.sleep(30) 

		# perform the get request
		page = urllib.request.urlopen(url)
		response = page.read() 

		# create a new hash 
		newHash = hashlib.sha224(response).hexdigest() 

		# check if new hash is same as the previous hash 
		if newHash == currentHash: 
			continue

		# if something changed in the hashes 
		else: 
			# notify 
			print("something changed") 

			# again read the website 
			page = urllib.request.urlopen(url)
			response = page.read()

			# create a hash 
			currentHash = hashlib.sha224(response).hexdigest() 

			# wait for 30 seconds 
			time.sleep(30) 
			continue

	# To handle exceptions 
	except Exception as e: 
		print("error") 

