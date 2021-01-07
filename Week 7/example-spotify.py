# -*- coding: utf-8 -*-

import json
import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQABslKgWgXkd-vtojPePATyNiVRVpVvBy7tspjCsdUH0BcqQn-3O17b4ejyTQSev-WuLXwHGveANZn12tfZWLGaKzAqTTHwDI3ItLmqobta8E6Au_5PDnyXuEqAkeFIR6WzotN1J3hGU_CTqWk-Mrmqju5elNf77DM_En2s7AgCP0jvMj2K-7Ez2oYUd6FXc-7YwwzKjzLlAX76eRsreCqgMn3H5mtU9BQ9cZ_S3p143KvKaNF5GlA5CztSURVlNS9ZN_ZBvIYckVqb7Q',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

params = (
        ('q', 'Taylor Swift'),
        ('type', 'artist'),
    )

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])

json_data = json.loads(response.text) # convert json response to text/dict

#print(json.dumps(json_data, sort_keys=True, indent=3)) # A beautified print of the returndata

genres = json_data['artists']['items'][0]['genres'] # Isolating the genre information - as a list

for genre in genres:
	print(genre)
