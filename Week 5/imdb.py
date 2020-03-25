# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.imdb.com/search/title/?title_type=feature,tv_movie&release_date=1970-01-01,&num_votes=1000,&genres=sci-fi&count=50&start=" # The initial search url, note that feature film and since 1970 are included as arguments
  
counter = 1

# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(baseurl+str(counter), headers=headers)
context = ssl._create_unverified_context()

# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
src_html = uClient.read() # html is stored in variable html
uClient.close()

# Interpret the page source as html
soup = BeautifulSoup(src_html, 'html.parser')

# Isolate total number of results
searchresults = soup.find('div',class_='nav')
searchresults = searchresults.find('div',class_='desc').getText()
searchresults = searchresults.split('of ')[1]
searchresults = searchresults.split(' titles')[0]
searchresults = searchresults.replace(',','')
print('Total number of search results:',searchresults)

# List of dicts to story information
dataset = []

while counter < int(searchresults): # Continue looping over all the search results pages (50 records per page), until all pages are parsed

	# Open URL (i.e., make request) + disguise agent
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(baseurl+str(counter), headers=headers)
	context = ssl._create_unverified_context()
		
	# To fetch html and store in variable 'html'
	uClient= urlopen(req, context=context)
	src_html = uClient.read() # html is stored in variable html
	uClient.close()
		
	# Interpret the page source as html
	soup = BeautifulSoup(src_html, 'html.parser')
		
	for item in soup.find_all('div',class_="lister-item-content"): # All the information we need is in the div with class "lister-item-content"
		print()
		title = item.find('a').getText() # Get the movie title
		print('Title:',title)
			
		year = item.find('span',class_="lister-item-year text-muted unbold").getText() # Get the release year
		print('Year:',year)
			
		try:
			duration = item.find('span',class_="runtime").getText() # Get duration
		except:
			duration = ""
		print('Duration:',duration)
			
		description = item.find_all('p',class_="text-muted")[1].getText().strip()
      
		print('Description:',description)
			
		director = item.find_all('p')[2]
		director = director.find('a').getText()
		print('Director:',director)
			
		rating = item.find('div',class_="inline-block ratings-imdb-rating").getText().strip() # Get rating
		print('Rating:',rating)
			
		votes = item.find_all('p')[3]
		votes = votes.find_all('span')[1].getText().strip() # Get votes
		print('Votes:',votes)
			
		try:
			metascore = item.find('div',class_="inline-block ratings-metascore").getText()
			metascore = int(metascore.replace('Metascore','').strip())
		except:
			metascore = ""
		print('Metascore:',metascore)
			
		details = item.find_all('a')[0]['href']
			
		# Open URL (i.e., make request) + disguise agent
		headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		req = Request("https://www.imdb.com/"+details, headers=headers)
		context = ssl._create_unverified_context()
			
		# To fetch html and store in variable 'html'
		uClient= urlopen(req, context=context)
		new_html = uClient.read() # html is stored in variable html
		uClient.close()
			
		detailpage = BeautifulSoup(new_html, 'html.parser') # Parsing html on webpage
			
		genresource = detailpage.find_all('div',class_="see-more inline canwrap")
			
		genres = []
		countries = []

		for genresourcespecific in genresource:
			if "Genres" in str(genresourcespecific):
				for genre in genresourcespecific.find_all('a'): # Get genres
					genres.append(genre.getText().strip())
						
				genres = ', '.join(genres)
				print('Genres:',genres)
						
				countrysource = detailpage.find('div',id='titleDetails')
				
				for countryinfo in countrysource.find_all('div',class_="txt-block"):
					if "Country" in str(countryinfo):
						for country in countryinfo.find_all('a'): # Get countries
							countries.append(country.getText().strip())
									
				countries = ', '.join(countries)
				print('Countries:',countries)
				
			# Add information to dataset variable

		dataset.append({
			'title':title,
				'year':year,
				'duration':duration,
				'description':description,
				'director':director,
				'rating':rating,
				'votes':votes,
				'metascore':metascore,
				'genres':genres,
				'countries':countries
				})

		counter += 50 # We have just done 50 records (or less), these are added to the counter so the while-loop can be stopped in time

dataset = pd.DataFrame(dataset) # Converting list of dictionaries into dataframe
dataset.to_csv('imdbdata.csv',sep=';',index=False) # Writing dataframe into CSV file
