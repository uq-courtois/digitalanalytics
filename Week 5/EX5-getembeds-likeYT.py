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

# Loop through all the embedded <iframe> </iframe>
for link in soup.find_all('iframe'):
    linkref = link['src'] # Get link from iframe

    if 'youtube' in linkref: # Proceed if 'youtube' is in link from iframe (indicates YouTube embed)

        videoid = linkref.split('embed/')[1] # get the videoid from the embed link, so we can contact YouTube to get that one, specific video

        try: # Try to...

            print()

            ### The following three lines of code access a Python package designed to download videos from YouTube, we borrowed this code
            ### See https://pypi.org/project/youtube_dl/ for more information

            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v='+videoid]) # Download YouTube video with id == videoid

        except: # If try fails
            print('Video download failed.')
