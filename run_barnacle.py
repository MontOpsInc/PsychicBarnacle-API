"""
author: Niklaus Parcell
date: Monday 22 January 2024
objective: Run Psychic Barnacle on the API
"""


import os
import requests
import json
import time 


def run_barnacle(config):

	"""
	API URL Endpoint
	"""
	api_url = "https://75agyozjrd.execute-api.us-west-1.amazonaws.com/dev"
	
	
	
	"""
	Post request to get pre-signed URL's to upload data and config(secure)
	"""
	url = api_url + "/test_upload_s3"
	response = requests.post(url, json=config)
	if response.json()["statusCode"] != 200:
		print(response.json()["message"])
		return
	key = response.json()["key"]
	config["key"] = key  # update key in config
	print("Using key: %s"%key)




	"""
	Post request to get pre-signed URL to download (secure)
	"""
	# Upload config
	pre_signed_config = response.json()["url_config"]
	response_for_config = requests.put(pre_signed_config, data=json.dumps(config))

	# Upload data 
	pre_signed_data = response.json()["url_data"]
	with open(config["path"], "rb") as f:
		response_for_df = requests.put(pre_signed_data, data=f) 




	"""
	Alternatively, trigger psychic_barnacle_function manually
	"""
	url = api_url + "/api-barnacle"
	pb_response = requests.post(url)



	"""
	Download the results from s3, which also deletes the files from s3
	"""
	seconds = config["wait_time"]
	print("Patiently giving Psychic Barnacle %d seconds to breathe,\n talk to the data gods, and complete work..."%seconds)
	time.sleep(seconds)  # wait for the function to finish


	# Get pre-signed url for download
	url = api_url + "/barn_download"
	response_for_download_url = requests.get(url, json=config)
	try:
		if response_for_download_url.json()["statusCode"] != 200:
			print(response_for_download_url.json()["body"])
			return
		pre_signed_download = response_for_download_url.json()["url"]

		# Download the file
		response = requests.get(pre_signed_download)
		file_save_path = os.path.join(config["save_name"])
		with open(file_save_path, 'wb') as file:
			file.write(response.content) 
	except:
		print(response_for_download_url.json())
		return