# -*- coding: utf-8 -*-

import json
import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQC0c_jkD8aoOmkgujNGWoIm1kDnuJDm022KZ59quGoeP5KQwPCf1yV9iIFJZ52R4pqNg5UGh4GaeHDf48njsFxJGywWt3P5IpLoD69uJzij5iviPWnZFTwqMdxlghcbJiaslaCC11zNMF4dbYXY_vv6lE_lBqPVNFeW4JyWv3QbxrKjr6EfMHFL9C6MhkxHiIv36nenmUWAURwmTfu08SpXlxRJb-DTWEGpo5XoFZWKKG8MAcRVR0bPi_7TPqtKFv4rNZla60fxLrTJaA',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

params = (
        ('q', 'Dance Monkey'),
        ('type', 'track'),
				('limit', 1)
    )

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params

json_data = json.loads(response.text) # convert json response to text/dict

print(json.dumps(json_data['tracks']['items'][0]['album']['artists'][0]['name'], sort_keys=True, indent=3)) # A beautified print of the returndata
