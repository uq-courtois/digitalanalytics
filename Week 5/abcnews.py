#Build a scraper that tracks ABC's latest news articles on #https://www.abc.net.au/news/justin/.

#You should scrape the news article title and the hyperlink that links to it. Start from the top, and stop scraping just before the 'load more stories' button. Print the results to the console. An add-on: automatically calculate the percentage of articles that are on the COVID-19/Corona virus at the end.

#TIP 1: First narrow down the value of your soup variable (all the html) to that of the div that holds all of the news updates we are interested in...

#TIP 2: If you want to check whether a certain substring is in a string value, but you don't want to be hindered by upper/lower case restrictions, it might be helpful to convert your string variable into lower case by using the .lower() method - e.g., for the string variable varx >>> varx.lower()

#TIP 3: You can use len(listx) to get the length of a list named listx
  
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# The URL we want to scrape
url = 'https://www.abc.net.au/news/justin/' 

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
maindiv = soup.find('div',class_='sidebar__main--6TJ0W')

allarticles = []
covidarticles = []

for item in maindiv.find_all('div',class_='card-layout__content--38hRP'):
	title = item.find('a').getText()
	link = 'http://abc.net.au'+item.find('a')['href']

	print(title)
	print(link)
	print()

	allarticles.append(title)

	if 'corona' in title.lower() or 'covid' in title.lower():
		
		covidarticles.append(title)

print()
print(len(covidarticles)/len(allarticles)*100,'percent of the articles is on COVID-19')
