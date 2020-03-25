from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# The URL we want to scrape
url = 'http://www.cedriccourtois.be/fanpage'

#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS

# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()

#################################################
#################################################

### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

### Isolating the table data (mind that there is only one table,if there would be more, than we need to use a find_all)
tabledata = soup.find('table')

### Looping through all the table rows
for row in tabledata.find_all('tr'):

	# Use a try/except because otherwise we will get errors because we are not handling the <th> table header tags
	try:
		album = row.find('td', class_ = 'album').getText()
		sales = row.find('td', class_ = 'sales').getText()
		release = row.find('td', class_ = 'release').getText()
		print(album,sales,release)
	except:
		pass
