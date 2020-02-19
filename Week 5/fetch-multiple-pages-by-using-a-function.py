### HOW TO USE A FUNCTION TO GET PAGE HTML - EASILY ITERABLE WHEN HAVING TO HARVEST INFORMATION FROM MULTIPLE PAGES

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

### The function

def fetchurl(url):

    # Open URL (i.e., make request) + disguise agent
    headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = Request(url, headers=headers)
    context = ssl._create_unverified_context()

    # To fetch html and store in variable 'html'
    uClient= urlopen(req, context=context)
    html = uClient.read() # html is stored in variable html
    uClient.close()

    # Interpret the page source as html
    soup = BeautifulSoup(html, 'html.parser')

    return soup

# Defining the url
url = "http://www.cedriccourtois.be/fanpage"

# Activating the function, sending the url, to return the html in a variable 'soup'
soup = fetchurl(url)

# See the result...
print(soup)

### This could be used to automate getting the html (and elements) of a list of webpages

urls = ['http://www.uq.edu.au','http://www.abc.com.au']

for url in urls:
    print('WEBPAGE HTML of',url)
    soup = fetchurl(url)
    print(soup)
    print()
