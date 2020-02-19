from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import csv

######
######

# Function to fetch html from url

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

######
######

# The initial search url, note that feature film and since 1970 are included as arguments
baseurl = "https://www.imdb.com/search/title/?title_type=feature&release_date=1970-01-01,2019-12-31&genres=sci-fi&start="
counter = 1

# Set temporary initial url
url = baseurl

# Activating function fetchurl and get soup as a return variable
soup = fetchurl(url)

### Following lines of code are used to isolate the amount of search results (to use to stop the while loop we're about to use when all results are in)
searchresults = soup.find('div',class_='nav')
searchresults = searchresults.find('div',class_='desc').getText()
searchresults = searchresults.split('of ')[1]
searchresults = searchresults.split(' titles')[0]
searchresults = searchresults.replace(',','')

print('Total number of search results:',searchresults)

### PREPARE CSV
csv_file = open('imdb_data.csv','a')
csv_writer = csv.writer(csv_file, delimiter=';')
csv_writer.writerow(['title','year','rating']) # Three variables headers
csv_file.close

while counter < int(searchresults): # Continue looping over all the search results pages (50 records per page), until all pages are parsed

    # Compile url of the search result page we want (this will change per iteration)
    url = baseurl+str(counter)

    # Activating function fetchurl and get soup as a return variable
    soup = fetchurl(url)

    for item in soup.find_all('div',class_="lister-item-content"): # All the information we need is in the div with class "lister-item-content"

        title = item.find('a').getText() # Get the movie title
        year = item.find('span',class_="lister-item-year text-muted unbold").getText() # Get the release year

        # Clean up release year: remove ( )
        year = year.replace('(','')
        year = year.replace(')','')

        # Get ratings - Note: try/except is used because not all movies have ratings. Otherwise the script would crash (!!!)
        try:
            rating = item.find('div',class_="inline-block ratings-imdb-rating").getText().strip() # Get the rating number + strip blank spaces
        except:
            rating = "" # If there is no rating, we'll use this empty string value instead

        print(title,year,rating) # print to console

        ### WRITE TO CSV FILE
        csv_file = open('imdb_data.csv','a')
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow([title,year,rating]) # We are saving three variable values
        csv_file.flush()
        csv_file.close

    counter += 50 # We have just done 50 records (or less), these are added to the counter so the while loop can be stopped in time
