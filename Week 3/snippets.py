### LOGICAL STATEMENTS AND LOOPS

participant = {'name':'Waldo','age':23,'weight':75,'length':1.75}

# We implement a conditional: if the value for the key 'name' in the dictionary 'participant' equals to 'Waldo', then, and only then, we want to print 'Found Waldo...'

if participant['name'] == 'Waldo':
	print('Found Waldo...')

# When an if-condition is not satified, we would provide an alternative through an 'else'-statement

if participant['age'] > 18:
	print(participant['name'],'is an adult')
else:
	print(participant['name'],'is a minor')

# We can add as many as we need... Let's revisit our BMI program and return a print-statement tailored to the BMI score...

# Original data
participant = {'name':'Mark','age':23, 'weight':75,'length':1.75}

# Calculated BMI
participant['bmi'] = participant['weight']/(participant['length']**2)

# Print message depending on BMI score
if participant['bmi'] < 18.5:
	print(participant['name'],'is underweight')
if participant['bmi'] >= 18.5 and participant['bmi'] < 25:
	print(participant['name'],'has a healthy weight')
if participant['bmi'] >= 25 and participant['bmi'] < 30:
	print(participant['name'],'is overweight')
if participant['bmi'] >= 30:
	print(participant['name'],'is obese')

### FOR LOOPS: what we need when we want to work on a data structure that contains multiple elements (e.g., a list)

# An example...

ages = [17,19,22,21,16,18]

for age in ages:
	if age >= 18:
		print('Found an adult')
	else:
		print('Found a minor')

# Another example...

ourclass = ['Mark','Zoran','Jing','Lisa']

# ourclass is iterable, we want to loop through all its elements, we here name 'name'
for name in ourclass:
	print (name)

# this is the same... we freely choose the loop variable (in this case 'item' - as long as it's unique and doesn't overlap with the name of a function/command, it's fine...)
for item in ourclass:
	print (item)

### NESTED FOR LOOPS: a loop in a loop - per iteration of the outer loop, the inner loop is ENTIRELY completed. The indenting is EXTREMELY important because it prioritizes the order of completing tasks...

lista = ['a','e','f']
listb = ['c','d','e']

for itema in lista:
	for itemb in listb:
		print(itema,itemb)
		print('Iteration INNER')
	print('Iteration OUTER')

# Often used to find matching elements between iterables, e.g. common elements in lists...

lista = ['a','e','f']
listb = ['c','d','e']

for itema in lista:
	for itemb in listb:
		if itema == itemb:
			# The following print statement will only be triggered when both the INNER and OUTER loop are handling an element that's the same letter
			print(itema,itemb,'> Match found')
		else:
			print(itema,itemb,'> No match found')

# When we want to stop iterating (because we already have what we need): use the 'break' command

# List of years of birth
yearofbirth = [1986,1979,1999,2001]

# Stop if someone older than 35 is found
for item in yearofbirth:
	item = 2020 - item
	print(item)
	
	if item > 35:
		break

### WHILE LOOPS

# This following program will keep adding up one to the value op stopvalue (which is 0 at first) AT THE END OF THE LOOP for as long as the resulting value is smaller than or equals to 5 WHEN THE NEW LOOP STARTS...

stopvalue = 0

while stopvalue <= 5:
	print(stopvalue)
	stopvalue += 1

# Another example generating a random string of letters until the sting has increased to a length of 10 letters

import string # Package to process strings
import random # Package to randomize things

alphabet = string.ascii_letters.lower()[0:26]
print(alphabet)

randomstring = ""

while len(randomstring) < 10:
	letter = random.choice(alphabet)
	randomstring = randomstring + letter
	print(randomstring)
