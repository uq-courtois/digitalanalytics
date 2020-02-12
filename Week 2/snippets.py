### DATA STRUCTURES
### We distinguish between four major data structures

varx = ['Erik','John','Lisa'] # A list
print(type(varx))
varx = {'Erik','John','Lisa'} # A set
print(type(varx))
varx = ('Erik','John','Lisa') # A tuple
print(type(varx))
varx = {'Name':'Erik','Age':25} # A dictionary
print(type(varx))

varx = [
	{'Name':'Erik','Age':25},
	{'Name':'John','Age':21},
	{'Name':'Lisa','Age':27}
] # A list (of dictionaries)
print(type(varx))

### LIST

emptylist = []
names = ['John','Mark','Lisa','Sarah']
distances = [45,23,120,56,87]
likes = ['9K','334','1.2M']

# Lists consist of elements. We can add each specific element (or range of elements) by calling its index (their placement in the list, starting from 0)

names = ['John','Mark','Lisa','Sarah'] # A list with four elements, with indices O,1,2,3

print(names[0]) # Print first element
print(names[1]) # Print second element 
print(names[2]) # Print third element 
print(names[3]) # Print fourth element
print(names[2:]) # Print from second to last element
print(names[:2]) # Print from first until (!) the third element
print(names[-1]) # Print last element
print(names[-2]) # Print last two elements

# We can manipulate lists (i.e., change them)

ourclass = ['Mark','Zoran','Jing','Lisa'] # A list with four elements, with indices O,1,2,3

ourclass.remove('Mark') # Mark is removed from our list
print(ourclass)

ourclass.append('Mark') # Mark is added again at the end of the list
print(ourclass)

ourclass.remove('Mark') # Mark is removed from our list
print(ourclass)

ourclass.insert(0,'Mark') # Mark is added again. First element of a list has an index 0 (!)
print(ourclass)

ourclass.sort() # Sorting the list; strings are sorted alfabetically
print(ourclass)

ourclass.reverse() # we can reverse our prior order
print(ourclass)

# Numerical lists offer specific opporunities:

listofnumbers = [3,4,9,12,4]
print(max(listofnumbers)) # Print highest number
print(min(listofnumbers)) # Print smallest number
print(sum(listofnumbers)) # Print sum of all numbers
listofnumbers.sort() # Sort (small to large by default)
print(listofnumbers)
listofnumbers.reverse() # Reverse sorting
print(listofnumbers)

# We can - of course - glue lists together and even search in them

lista = ['a','e','f']
listb = ['c','d','e']

# Combine lista and listb
listab = lista + listb
# Check whether 'a' and 'd' are in listab
print('a' in listab) # There's an 'a' in the combined list, so this will return a value 'True'
print('d' in listab) # There's a 'd' in the combined list, so this will return a value 'True'

### SET

# Similar to a list, but with fewer opportunities. Contains no duplicates... (unique elements only)

uniquenames = {'Jane','Marc','Joe'} # This is a set
print(uniquenames)

names = ['Jane','Marc','Joe','Joe'] # This is a list
print(names)

uniquenames = set(names) # The list names is the list converted to a set called uniquenames
print(uniquenames)

### DICTIONARY

participant = {'name':'Mark','age':23, 'weight':75,'length':1.75}

person = {
'name':'Mark',
'age':23,
'weight':75,
'length':1.75
}

# 'name', 'age', 'weight', and 'length' are keys
# 'Mark',23,75,1.75 are values
# 'name'='Mark' is a key-value pair

# Both of the above notations are equivalent. The second is a bit more practical though
print(participant)
print(person)

# Access values (through their keys)

# We can access each element seperately, by refering to the key
print(person['name'])
print(person['age'])
print(person['weight'])
print(person['length'])

# We can change value of a specific key
person['age'] = 25
print('Changed age to',person['age'])

# Accessing this information allows to build programs, of which the output could be stored as a new key-value pair - EXAMPLE: a BMI calculator

participant = {'name':'Mark','age':23, 'weight':75,'length':1.75}
# Add key 'bmi'
participant['bmi'] = participant['weight']/(participant['length']**2)
print('BMI:',participant['bmi'])
# Delete key 'bmi'
del participant['bmi']
#print(participant['bmi']) # A now it's gone... so running actually this would produce an error

### LIST OF DICTIONARIES - or how to deal with two-dimensional datasets as we know them from for example survey research

mydataset = [{'name':'Mark','age':23,'weight':75,'length':1.75},{'name':'Jane','age':21,'weight':60,'length':1.70},{'name':'Eric','age':30,'weight':80,'length':1.78},]

# Logic for accessing remains te same...

# We can access each (or range of) row(s):
print(mydataset[0]) # print first line in dataset
print(mydataset[1]) # print second line in dataset
print(mydataset[2]) # print third line in dataset

# We can dive in deeper by getting values for the keys of certain rows
print(mydataset[0]['name']) # print name value in first line in dataset
print(mydataset[2]['age']) # print age value in third line in dataset
