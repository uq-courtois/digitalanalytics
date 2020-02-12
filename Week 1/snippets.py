### We distinguish between the following four types of variables

x = 3 # Integer variable
print(x)

x = 2.5 # Float variable
print(x)

x = 'The contents of a string'
print(x) # String variable

x = True
print(x) # Boolean variable

### Examples of manipulations possible on numeric (Int & Float) variables (Many more are possible, e.g. cheat sheet)

# Addition
A = 2 + 3
print(A)
B = A + 5
print(B)

# Subtraction
A = 5 - 3
print(A)
B = A - 1
print(B)

# Multiplication
A = 3 * 2
print(A)
B = 4 * A
print(B)

# Division
A = 6 / 2
print(A)
B = A / 2
print(B)

### Examples of manipulations possible on a string variable

# Concatenate (= combining strings)
firstvar = "First string"
secondvar = "Second string"
newvar = firstvar + secondvar
print(newvar)

# Combine both string variables and literal string expressions
newvar = "First string" + " " + secondvar # Here we add a space between the two strings variables we want to concatenate
print(newvar)

# Replace (portions) of a string with others
oldvar = "Old text"
print(oldvar)
newvar = oldvar.replace("Old text","New text")
print(newvar)

# Split up string based on a defined character (e.g., a space)

sentence = 'This is a random sentence'
print(sentence)

# Splitting on each space, store result in variable 'chopped'
chopped = sentence.split(' ')
print(chopped)

# The split character could be any character, e.g., every 'i'
chopped = sentence.split('i')
print(chopped)

# Printing each element of the chopped up string
print(chopped[0]) # First word
print(chopped[1]) # Second word
print(chopped[2]) # Third word

### Verifying the datatype of your variable (or how Python interprets it)

varx = "Erik"
vary = 35
varz = 23.34
print(type(varx))
print(type(vary))
print(type(varz))

### Variables can be converted into each other if the values allow for it...

# Convert a string to an integer or float
varx = '1000' # Originally a string
print(type(varx)) # Shows that it's a string

varx = int(varx) # We change it into a integer
print(type(varx)) # Shows that it's an integer
varx = float(varx) # We change it into a float
print(type(varx)) # Shows that it's a float

varx = 'Random text'
#varx = int(varx) # Will cause error because cannot be converted!

# Convert an integer to a string
varx = 1000 # An integer variable
print(type(varx)) # Shows that it's an integer
varx = str(varx)
print(type(varx)) # Shows that it's a string

### Examples of boolean variables

varx = 4
vary = 5

# Suppose we want to test whether the value of varx is larger than the value of vary
result = varx > vary
print(result) # Will be 'False' of course

# Suppose we want to test whether the value of varx is larger than 2
result = varx > 2
print(result) # Will be 'True' of course
