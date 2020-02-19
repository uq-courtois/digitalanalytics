from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

### IMPORTANT: module to download YouTube video
import youtube_dl

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

print()
print('ALBUM, SALES, RELEASE')

### Isolate the data from the <table> </table> tags (we can do this because there is only one on the page!)

tabledata = soup.find('table') # Extract all table information from page, not that there is only one (needs for-loop when multiple tables are present)

### Within the isolated table data, we loop through each row... <tr> </tr>

for tablerow in tabledata.find_all('tr'):

    album = sales = release = ''
    
    # And extract each specific cell class within that row... ('album','sales','release')
    
    for tablecell in tablerow.find_all('td',class_='album'): # loop through all the table data (cells) with album class
        album = tablecell.getText()

    for tablecell in tablerow.find_all('td',class_='sales'): # loop through all the table data (cells) with sales class
        sales = tablecell.getText()
        sales = sales.replace(',','')

    for tablecell in tablerow.find_all('td',class_='release'): # loop through all the table data (cells) with release class
        release = tablecell.getText()
        
    # When there's some data in the table row, even when incomplete, we print it...
    if album != '' or sales != '' or release != '':
        print(album+','+sales+','+release)
