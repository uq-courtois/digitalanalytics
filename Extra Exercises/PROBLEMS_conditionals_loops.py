### EXERCISE A
# The following list of dictionaries contains four Instagram account names and the amount of followers
# 1K = 1000, 1M = 1000000
# Convert the follower numbers to actual integers, store the solution in a key 'followers_int'
# Print the conversion to the console, line by line in the following format:
# Accountname has x followers (x should be the value of followers_int)

instagramfollowers = [
{'account':'Rebeccah','followers':'384'},
{'account':'Billiee','followers':'1K'},
{'account':'Beyonce','followers':'150M'},
{'account':'Drake','followers':'130M'},
]

### EXERCISE B
# The variable listurls is a list of webpages
# Extract all domain names (i.e., news.com.au and abc.net.au) and print them in each iteration
# Store the domains in a new list domainnames
# Only keep unique domains (i.e., filter out duplicates)
# Print the unique domains

listurls = [
'https://www.news.com.au/finance/economy/australian-economy/coronavirus-stimulus-package-to-support-apprentices-offer-taxfree-money-to-small-businesses/news-story/3336f2391c9a5243422be433984d2d40',
'https://www.news.com.au/travel/travel-updates/health-safety/coronavirus-australia-what-life-will-be-like-in-virus-lockdown/news-story/e40d3ce8cf12e85e441c06ac0f47ca4e',
'https://www.news.com.au/lifestyle/health/health-problems/queen-ditches-handshakes-amid-coronavirus-fears/news-story/d9f5431acd776b3464bf03ad7d3f736c',
'https://www.abc.net.au/news/2020-03-11/coronavirus-stimulus-package-to-include-billions-for-apprentices/12046688',
'https://www.abc.net.au/news/2020-03-11/bear-market-share-stocks-investing-superannuation-coronavirus/12046630',
]

### EXERCISE C
# Isolate the students that have at least one A on a course
# Print their names, and the grades for their courses
# i.e., Name has a grade 'grade' for course and a grade 'grade' for course

studentgrades = [
{'student':'Mark','English':'A','History':'A'},
{'student':'Lisa','English':'B','History':'A'},
{'student':'Laura','English':'B','History':'C'},
{'student':'Eva','English':'C','History':'C'},
{'student':'Pradip','English':'A','History':'A'},
]

### EXERCISE D
# Print the names that are shared by both lists using a nested for loop

firstlist = ['Steve Jones','Andrea Becket','Lisa Murphy','Joan Bennet']
secondlist = ['Bruce Jackson','Andrea Becket','Lisa Murphy','Danilo di Luca']
