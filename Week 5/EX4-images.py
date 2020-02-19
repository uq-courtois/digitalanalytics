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

### Run through interpreted html and find all <img> </img> tags
for imglink in soup.find_all('img'):

    # Get the image link from the img-tag and print it:
    imgurl = url+"/"+imglink['src']
    print(imgurl)

    imgfile = open(imglink['src'],'wb') # Create a new, empty picture file
    imgfile.write(urlopen(imgurl).read()) # Write picture information into empty file
    imgfile.close() # Close file

    print('Picture downloaded...')
