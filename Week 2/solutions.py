### EXERCISE 1:

# Define a string variable named ‘name’ and set value to ‘Eric’
name = 'Eric'
# Define a integer variable named ‘age’ and set value to 25
age = 25
# Define a float variable named ‘weight_kg’ and set value to 65.50
weight_kg = 65.50
# Print the variables to the console
print(name,age,weight_kg)

### EXERCISE 2:

# Define a string variable named ‘surname’ and set value to ‘Jones’
surname = 'Jones'
# Make a new variable ‘fullname’ by concatenating name and surname (with a whitespace in between)
fullname = name + ' ' + surname
# Make a new variable named ‘weight_pound’ with Eric’s weight in pounds (1kg = 2.20462 pounds)
weight_pound = weight_kg * 2.20462
# Print the variables fullname and weight_pound to the console (i.e.  The full name followed by “weighs” and then the person’s weight in pounds)
print(fullname,'weighs',weight_pound,'pounds')

### EXERCISE 3:

# Define an empty list with the name ‘cities’
cities =[]
# Add the following cities:  ‘Brisbane’, ‘Melbourne’, ‘Sydney’, ‘Perth’
cities.append('Brisbane')
cities.append('Melbourne')
cities.append('Sydney')
cities.append('Perth')
# Delete ‘Melbourne’
cities.remove('Melbourne')
# Print the list to the console
print(cities)
# Print the first city to the console
print(cities[0])
# Print the last city to the console
print(cities[-1])
# Check (programmatically!) whether Brisbane is in the list
print('Brisbane' in cities)

### EXERCISE 4:

# Define a list with the following words: ‘cow’, ‘sheep’, ‘horse’ and print it to the console
animals = ['cow','sheep','horse']
# Define a list of dictionaries, based on the matrix (below) and print it to the console

# Name  Couse   Grade
# Mark  Math    A
# Mark  English A
# Eric  Math    B
# Eric  English B

mydata = [
	{'name':'Mark','course':'Math','grade':'A'},
	{'name':'Mark','course':'Math','grade':'A'},
	{'name':'Eric','course':'English','grade':'B'},
	{'name':'Eric','course':'English','grade':'B'},
]

# From that dictionary, print Eric’s and Mark’s math scores to the console

print(mydata[0]['grade'])
print(mydata[2]['grade'])
