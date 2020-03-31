### EXERCISE 1:

# Read data from dataset.csv - Download it from < SEE BLACKBOARD LINK >
# Print the artists and songs in the dataset to the console, line by line

### READING

# Import pandas
import pandas as pd

data = pd.read_csv('dataset.csv',sep=',') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

# Iterate through the imported data
for item in data:
	print(item['artist'],'-',item['song'])

### EXERCISE 2:

# Name    Couse     Grade
# Mark    Math      A
# Mark    English   A
# Eric    Math      B
# Eric    English   B

# Enter data from table into your script (i.e., hard code it)
# Write it into a new csv file ‘grades.csv’

dataset = [
	{'name':'Mark','course':'Math','grade':'A'},
	{'name':'Mark','course':'English','grade':'A'},
	{'name':'Eric','course':'Math','grade':'B'},
	{'name':'Eric','course':'English','grade':'B'},
]

print(dataset) # Just printing it to check

### WRITING

newdata = pd.DataFrame(dataset) # Converting list of dictionaries into dataframe
newdata.to_csv('grades.csv',sep=';',index=False) # Writing dataframe into CSV file


### EXERCISE 3

# Read the data from searchresults.csv (< See Blackboard item for URL >)
# Print the unique domain names extracted from all results (url variable in the data file)
# Count the number of times ‘hln.be’ is in the results
# Make a new csv file with only the top 3 ranked results (name it searchresults_top3.csv)

# Import pandas
import pandas as pd

data = pd.read_csv('searchresult.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

urllist = [] # empty list to store all domain names we're about the extract from the page urls

# Iterate through the imported data
for item in data:
	urllist.append(item['URL'].split('/')[0])
	# We get the value for the URL key in each iteration
	# We split on the /, which returns a list with the url in bits and pieces
	# The first bit (or element in that list), is the domain name
	# We append that domain name to urllist

print(set(urllist)) # We print urllist as a set so we're sure that there are no duplicates, only uniques
print(urllist.count('www.hln.be')) # We count the amount of times www.hln.be is in the list (this is on the list, not a set version of it)

topthree = [] # empty list that will be our list of dictionaries with top three results we want to export in a file

for item in data:
  if item['Rank'] < 4: # Conditional to make sure we only add information of top three results
		print(item['URL'],item['Rank']) # Just printing the top three resuls' URL and Rank
		topthree.append({'URL':item['URL'],'Rank':item['Rank']}) # topthree list - empty before loop - is populated with top 3 results
		# Note that we are adding a dictionary to the list per iteration, containing the iteration value of URL and Rank

### WRITING

# New data, hardcoded into our script:

topthree = pd.DataFrame(topthree) # Converting list of dictionaries into dataframe
topthree.to_csv('searchresults_top3.csv',sep=';',index=False) # Writing dataframe into CSV file

### EXERCISE 4:

# Read the data from instagramdata.csv (< SEE LINK ON BLACKBOARD >)
# Convert the followers and following variables into proper integers (K = 1,000, M = 1,000,000)
# Make a new csv file with the new data (name it instagram_clean.csv)

# Import pandas
import pandas as pd

data = pd.read_csv('instagramdata.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

# Iterate through the imported data
for item in data:
  item['followers'] = item['followers'].replace('K','000') # Replacing the string value of the key with a numerical equivalent
  item['followers'] = item['followers'].replace('M','000000') # Replacing the string value of the key with a numerical equivalent
  item['following'] = item['following'].replace('K','000') # Replacing the string value of the key with a numerical equivalent
  item['following'] = item['following'].replace('M','000000') # Replacing the string value of the key with a numerical equivalent
  print(item['followers'],item['following']) # Printing the results before writing

### WRITING

# New data, hardcoded into our script:
data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('instagram_clean.csv',sep=';',index=False) # Writing dataframe into CSV file
