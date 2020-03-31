import requests
import json
import pandas as pd

baseurl = "https://api.foursquare.com/v2/venues/search?"

clientid = "HUQT5U2UIPDROTHAWRFBR45LKNHAQUAIJB1PS55VHR5Q33X0" #>>> Mock-up one, please get your own!
clientsecret = "SFJ1NHVVMJEQT5S111O3LNGNWST0KDW1D5HMKNVHICLW20H5" #>>> Mock-up one, please get your own!
credentials = "&client_id="+clientid+"&client_secret="+clientsecret+"&v=20190101" # Adding all the credentials together into the right arguments that will be part of the request

restaurants = ["McDonalds","KFC", "Domino's", "Hungry Jack's","Pizza Hut"]
cities = ["Brisbane","Perth","Melbourne","Adelaide","Sydney","Gold Coast","Darwin","Hobart","Newcastle","Canberra"]

dataset = []

for restaurant in restaurants:
	for city in cities: # Using nested for loop to get get all combinations of restaurants and cities that will be the essential parts of each query
		query = "near="+city+"+Australia"+"&query="+restaurant # Building the query, consisting of the two argument the Foursquare API requires

		compiledurl = baseurl + query + credentials # Compiling the url
		results = requests.get(compiledurl).json() # Making request, getting response
	
		for item in results['response']['venues']:
			address = item['location']["formattedAddress"] # Filtering addres info from response
			address = ', '.join(address) # Joining all address components into a single string
			lat = item['location']["lat"] # Filtering latitude info
			lng = item['location']["lng"] # Filtering longitude info
			print(restaurant,city)
			print(address)
			print(lat,lng)
			print()

			dataset.append(
				{
					'restaurant':restaurant,
					'city':city,
					'address':address,
					'lat':lat,
					'lng':lng,
					}
				) # Writing the information per API call into a temporary list of dicts

dataset = pd.DataFrame(dataset) # Converting list of dictionaries dataset into dataframe
dataset.to_csv('fs-data.csv',sep=';',index=False) # Writing dataframe into CSV file
