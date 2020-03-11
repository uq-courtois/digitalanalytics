### SOLUTION A

instagramfollowers = [
{'account':'Rebeccah','followers':'384'},
{'account':'Billiee','followers':'1K'},
{'account':'Beyonce','followers':'150M'},
{'account':'Drake','followers':'130M'},
]

for item in instagramfollowers:
    # Starting the for loop to iterate through every dictionary in the list instagramfollowers: we'll process one after the other
    conversion = item['followers']
    # Defining a variable conversion, which initially equals the string value of the key followers in each dictionary
    conversion = conversion.replace('K','1000')
    # Replace the substring K with 1000, to turn it into an interpretable integer
    conversion = conversion.replace('M','1000000')
    # Replace the substring M with 1000000, to turn it into an interpretable integer
    item['followers_int'] = int(conversion)
    # Add a new key to the dictionary called item['followers_int'], which is the string conversion that is now convertable into a proper integer

    print(item['account'],'has',item['followers_int'],'followers')
    # Printing the final statement

#### SOLUTION B

listurls = [
'https://www.news.com.au/finance/economy/australian-economy/coronavirus-stimulus-package-to-support-apprentices-offer-taxfree-money-to-small-businesses/news-story/3336f2391c9a5243422be433984d2d40',
'https://www.news.com.au/travel/travel-updates/health-safety/coronavirus-australia-what-life-will-be-like-in-virus-lockdown/news-story/e40d3ce8cf12e85e441c06ac0f47ca4e',
'https://www.news.com.au/lifestyle/health/health-problems/queen-ditches-handshakes-amid-coronavirus-fears/news-story/d9f5431acd776b3464bf03ad7d3f736c',
'https://www.abc.net.au/news/2020-03-11/coronavirus-stimulus-package-to-include-billions-for-apprentices/12046688',
'https://www.abc.net.au/news/2020-03-11/bear-market-share-stocks-investing-superannuation-coronavirus/12046630',
]

domainnames = []

for item in listurls:
    # Start the loop to iterate through all the urls
    item = item.split('/')
    # Split each url on every / this leads to a list item like e.g., ['https:', '', 'www.news.com.au', 'lifestyle', 'health', 'health-problems', 'queen-ditches-handshakes-amid-coronavirus-fears', 'news-story', 'd9f5431acd776b3464bf03ad7d3f736c']
    print(item[2])
    # We want to have the www.domain.com.au, so we select the second element from our list item
    domainnames.append(item[2])
    # Add that part of our split list item to the initially empty list domainnames

domainnames = list(set(domainnames))
# Convert to set (to ditch duplicates), then converting back to a list
print(domainnames)
# Print the unique domain names

### SOLUTION C

studentgrades = [
{'student':'Mark','English':'A','History':'A'},
{'student':'Lisa','English':'B','History':'A'},
{'student':'Laura','English':'B','History':'C'},
{'student':'Eva','English':'C','History':'C'},
{'student':'Pradip','English':'A','History':'A'},
]

for item in studentgrades:
    # Loop through each dictionary in the list studentgrades
    if item['English'] == 'A' or item['History'] == 'A':
        # If the student has either a grade A for English or History (or for both), we should print their scores
        print(item['student'],'has a grade',item['English'],'for English and a grade',item['History'],'for History')

### SOLUTION D

firstlist = ['Steve Jones','Andrea Becket','Lisa Murphy','Joan Bennet']
secondlist = ['Bruce Jackson','Andrea Becket','Lisa Murphy','Danilo di Luca']

for name1 in firstlist:
    # Looping through the first list (LOOP 1, outer loop)
    for name2 in secondlist:
        # Looping through the second list for every iteration of the first list (LOOP 2, inner loop)
        if name1 == name2:
            # Testing whether the item in the first outer loop matches any names in the second inner loop
            print(name1)
