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

### Run through interpreted html and find all <div> </div> tags that are labeled as class = blogpost
for blogpost in soup.find_all('div',class_='blogpost'):

  # Store each blogpost title => <h2> </h2> in the variable title and print it
  title = blogpost.find('h2').getText()
  print(title)

  # Store each blogpost text => <p> </p> in the variable blogtext and print it
  blogtext = blogpost.find('p').getText()
  print(blogtext)

  print()
