import requests
import json
import pandas as pd

baseurl = "https://api.foursquare.com/v2/venues/search?"

clientid = "HUQT5U2UIPDROTHAWRFBR45LKNHAQUAIJB1PS55VHR5Q33X0" #>>> Mock-up one, please get your own!
clientsecret = "SFJ1NHVVMJEQT5S111O3LNGNWST0KDW1D5HMKNVHICLW20H5" #>>> Mock-up one, please get your own!
credentials = "&client_id="+clientid+"&client_secret="+clientsecret+"&v=20190101"

restaurants = ["McDonalds","KFC", "Domino's", "Hungry Jack's","Pizza Hut"]

cities = ["Brisbane","Perth","Melbourne","Adelaide","Sydney","Gold Coast","Darwin","Hobart","Newcastle","Canberra"]

dataset = []

for restaurant in restaurants:
	for city in cities:
		query = "near="+city+"+Australia"+"&query="+restaurant

		compiledurl = baseurl + query + credentials
		results = requests.get(compiledurl).json()
	
		for item in results['response']['venues']:
			address = item['location']["formattedAddress"]
			address = ', '.join(address)
			lat = item['location']["lat"]
			lng = item['location']["lng"]
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
				)

dataset = pd.DataFrame(dataset) # Converting list of dictionaries dataset into dataframe
dataset.to_csv('fs-data.csv',sep=';',index=False) # Writing dataframe into CSV file
