### Credentials: https://developers.google.com/maps/documentation/geocoding/get-api-key#get-the-api-key

import json
from urllib.request import urlopen

baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "University of Queensland" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyDC60i9o-E4sOVCsYCZCYGB3DIlhAenZy0" # API key - you will need to get your own to try this example
# I de-actived the API key in this example for safety reasons

compiledurl = baseurl + query + apikey

json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result

print(locationdata)
