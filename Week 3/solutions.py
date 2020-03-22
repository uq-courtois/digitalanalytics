### EXERCISE 6

# Define a variable name with a value Jane
# Build a program that prints ‘Found Jane’ when the value of name matches ‘Jane’ 
# and ‘Jane not found’ when the value does not match ‘Jane’

name = 'Jane'

if name == 'Jane':
	print('Found Jane')
else:
	print('Jane not found')

### EXERCISE 7a

# Define a list with the following names: Jane, John, Marisa, Kobe, Eliza
# Print each name on a separate line by looping through the list

names = ['Jane', 'John', 'Marisa', 'Kobe', 'Eliza']

for name in names: # Iterate through variable names
	print(name) # Printing iteration variable name

### EXERCISE 7b:

# Define a list with the following numbers: 34, 45, 23, 49
# Divide each number by 2 and print the result on a seperate line

numbers = [34, 45, 23, 49]

for number in numbers: # Iterate through variable numbers
	print(number/2) # Printing iteration variable number divided by 2

### EXERCISE 8:

# Write a program that filters strings from the following list and
# stores each of the string values in a new list called newcollection: 

# TIP: test whether value is a string >>>
# if type(item) == str:

collection = ['Eric',10,34,'Karen',32,'Lisa']
newcollection = [] # Empty list to store string values

for item in collection:
	if type(item) == str: # Adding conditional to execute code only if item contains a string value in that iteration
		newcollection.append(item) # If so, add to list newcollection

# Print the final list to the console
print(newcollection)

### EXERCISE 9:

# Write a program that multiplies every number in list x by 5 
# and store those new values in a new list that you can use after the for loop is finished.
# Print the results in descending order...

x = [4,5,2,4,5,2,4]
y = [] # Empty list to store multiplications

for item in x: # Iterate through all numbers in x
	y.append(item*5) # Multiply each number by 5, storing it in the dedicated list y

y.sort() # Sort y ascending
y.reverse() # Reverse ascendeding list
print(y) 

### EXERCISE 10:

# Variable lyric is a string. Loop through the individual words.
# Only print the word ‘rock’ to the console each time it is mentioned.

lyric = "Everybody rock your body Everybody rock your body right Backstreet's Back alright"

chopped = lyric.split(' ') # Split the string value in lyric on each space in the list chopped

for word in chopped: # Iterate through all words in chopped
	if word == 'rock': # Only execute code when iteration variable word contains the string value 'rock
		print(word) # Print word

### EXERCISE 11:

# Format the following matrix in the appropriate data structure

# Name  Year of Birth
# Mark  1976
# Jane  1999
# Eric  2002

mydata = [
	{'name':'Mark','yob':1976},
	{'name':'Jane','yob':1999},
	{'name':'Eric','yob':2002},
	]

# Write a program that transforms the years of birth to years of age

for item in mydata:
	# Add age as a new key in the already given list of dictionaries
	item['age'] = 2020 - item['yob']

	# Print the name and the age of every person if they are over 30 years old
	if item['age'] > 30:
		print(item['name'],'is',item['age'],'old')

### EXERCISE 12a - A harder exercise...

# Print the first five urls that contain an .au domain form the list urls

# TIP 1: use a variable 'count' that starts with a value 0 at the beginning of the script
# The count variable should update itself with +1 per RELEVANT iteration 
# to keep count of the number of RELEVANT iterations
# count += 1 (=> is adding 1 to the original value of the variable)

# TIP 2: if 'break' is used in a for loop, the loops terminates immediately

urls = [
"www.abc.net.au/",
"www.cnn.com/",
"10play.com.au/",
"www.freeview.com.au/",
"www.freeview.com.au/",
"www.bbc.co.uk/",
"www.ariacharts.com.au/",
"www.9now.com.au/",
"www.yourtv.com.au/"
]

count = 0 # define counting varibale, set as 0

for url in urls:
	if '.au' in url: # Conditional to filter .au domains
		count += 1 # Update counter if .au domain is found (i.e., relevant iteration)
		if count <= 5: # Check whether the relevant iteration count is smaller than or equal to 5
			print(count,url) # Print iteration count and url

### EXERCISE 12b - Adding just one extra bit...

# Print the first five unique urls that contain an .au domain form the list urls (i.e., www.freeview.com.au/ is in there twice)

count = 0 # define counting varibale, set as 0
urls = list(set(urls))

for url in urls:
	if '.au' in url: # Conditional to filter .au domains
		count += 1 # Update counter if .au domain is found (i.e., relevant iteration)
		if count <= 5: # Check whether the relevant iteration count is smaller than or equal to 5
			print(count,url) # Print iteration count and url
