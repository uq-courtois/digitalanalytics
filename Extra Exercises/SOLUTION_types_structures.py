### SOLUTION A
names = ['Joan','Marc','Jing','Ella'] # Step 1
print(names[2]) # Step 2
names[0] = 'June' # Step 3
names.append('Lisa') # Step 4
print(names) # Step 5

### SOLUTION B
names = ['Lisa','Andrea','Akira','Sam','Lisa'] # Step 1
names = list(set(names)) # Step 2
names.sort() # Step 3
print(names) # Step 4
print(names[:2]) # Step 5
