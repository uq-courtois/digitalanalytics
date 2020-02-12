### An example of a try/except routine to mitigate errors

mydata = [
	{'name':'Karen','yearofbirth':1999},
	{'name':'Walter'},
	]

for item in mydata:
	try:
		item['age'] = 2020 - item['yearofbirth']
		print(item['age'])
	except:
		print('Missing data...')
