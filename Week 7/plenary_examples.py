### FIRST EXAMPLE - GOOGLE GEOCODING

# GOAL: get geolocation data for 'University of Queensland'
# URL to perform a Google Geocoding API query (copy/paste in the browser address bar and hit enter)
# https://maps.googleapis.com/maps/api/geocode/json?address=university+queensland&key=xxx

### SECOND EXAMPLE - SPOTIFY

# GOAL: get genres for Taylor Swift

# FOLLOWING STEPS REQUIRE CHROME/FIREFOX (defintely not Apple Safari)
# Documentation of API endpoint for search: https://developer.spotify.com/documentation/web-api/reference/search/search/
# 1. Scroll down to 'reponse format', then click the first 'try it' buttong (Example: Search for Artists)
# 2. Scroll down to q* (the query field) and type in 'Taylor Swift'
# 3. Scroll down to OAuth Token and click 'Get Token'. This will redirect you to a login page to get access (you need a Spotify account)
# 4. Click 'Try it' at the bottom. You will see the response in black area next to it

# Alternatively we can run this programmatically in Python...
# 1. Scroll back up and go to the "curl -X... " statement in the black area
# 2. Copy/paste the entire code and convert it to Python code at https://curl.trillworks.com/
# 3. Copy/paste the coverted code into your Python script (Note: the access token in this example will be expired, get a new one!)

import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQBz_LYYqX6OxRoZjIRWjAAe7tdzOe0lw_z8PcaV9QX0I9LsTX4SuvtHWKYN6hdwM0APniUnmTkyLHLcxUi22ic1RTgR11qHdb54XmTijsdHVIDyKb-RhzOHBrtO71eBu1HqgWe_TxPfEyiJVNokEEOrnn29hsGY8fBPdcKKicMfFfBRsWW9B4n-ajhKuXN3DD8388qoqoEm1Dxj_HvaISxB9xGuR1QQHnsz_T7ZVpxIsDxCSkEd50DSAmqHgtgXE34_gFqOJofyzvSzCg',
}

params = (
    ('q', 'taylor swift'),
    ('type', 'artist'),
)

response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)

# 4. Add the code to interpret the response

import json

json_data = json.loads(response.text) # convert json response to text/dict
print(json_data) # prints the raw reponse in JSON format
print()

# 5. To get what we specifically need, i.e., the genres:

for genre in json_data['artists']['items'][0]['genres']: #get the genres from the dict
    print(genre)
