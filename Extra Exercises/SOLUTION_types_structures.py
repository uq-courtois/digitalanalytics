### SOLUTION A
names = ['Joan','Marc','Jing','Ella'] # Defining list
print(names[2]) # Printing third name
names[0] = 'June' # Changing first name into June
names.append('Lisa') # Adding Lisa to list
print(names) # Printing list

### SOLUTION B
names = ['Lisa','Andrea','Akira','Sam','Lisa'] # Defining list
names = list(set(names)) # Converting into a set first (to drop duplicates), again converting to a list to allow for all list methods
names.sort() # Step 3 # Sorting ascending
print(names) # Step 4 # Printing the whole list
print(names[:2]) # Step 5 # Print the first two elements

# EXERCISE C

dataset = [
	{'Name':'Jane','Age':21},
	{'Name':'Eric','Age':30},
	{'Name':'Sonia','Age':32},
] # Enter data as a list of dictionaries

dataset[0]['Name'] = 'Jean' # Access line by index (line 1 = 0), and key by keyname (key 'Name'), overwriting the original value by 'Jean'
dataset[1]['Age'] = 31
# Access line by index (line 2 = 1), and key by keyname (key 'Age'), overwriting the original value by 31

print(dataset) # Print entire variable
