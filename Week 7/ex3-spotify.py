# -*- coding: utf-8 -*-
import json
import requests
import pandas as pd

data = pd.read_csv('artists.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

dataset = [] # Empty list to temporarily save the new data, and at the end write it into a new CSV

# Iterate through the imported data
for item in data:
	print('Searching for',item['Artist'])

	headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer BQDZRAUvTq_1PWQotWOjfTNQal4KrmvMHkR9EXV_ts1QPB5SphF3d4tGk1WJUe9U0Xl4b8IBf_bwrxbPYYfGotRSpGfzdGt0gEp6PeFhdhdnrwyrlY2cK1MGlSPQV5rQgMR4WVUxHPLD5GGxDkiSy7xr4ViuXadu71PqCO36j9kGX-t7B_y1uALZJJSHFU5swieQWzOksaFwLdV7PoFD4v2PXMQ3QAamDtHc5YDAn-NIxnwGO0vbE-Q5SpzH-POLyqqtJEhy2n-LES3yUw',
	} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

	params = (
					('q', item['Artist']), # Per iteration, the value of q = the read artist
					('type', 'artist'),
			)

	response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
	# The endpoint base url is supplemented by the arguments in the variables headers and params

	json_data = json.loads(response.text) # convert json response to text/dict

	genres = json_data['artists']['items'][0]['genres'] # Isolating the genre information - as a list

	genres = ', '.join(genres) # To make a clean string out of the genres list

	followers = json_data['artists']['items'][0]['followers']['total'] # Isolating the follower information

	dataset.append(
		{
			'Artst':item['Artist'],
			'Genres':genres,
			'Followers':followers,
		}) # Appending the information to a list

dataset = pd.DataFrame(dataset) # Converting list of dictionaries dataset into dataframe
dataset.to_csv('spotifydata.csv',sep=';',index=False) # Writing dataframe into CSV file
