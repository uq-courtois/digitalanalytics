# Functions come in handy to keep your code clean, free of excessive repetition
# They also allow you to easily swap code in teams

### Our first simple program:

listoftemperatures = [45,37,18,130]

for i in listoftemperatures:
    converted = (i*9/5) + 32
    print (i,'°C',converted,'°Fahrenheit')

# now there could be a bunch of code in between
# and after a while, we need to convert a new set of temperatures

print
print ('Some code in the middle')
print

listoftemperatures = [45,37,18,130]

for i in listoftemperatures:
    converted = (i*9/5) + 32
    print (i,'°C',converted,'°Fahrenheit')

###########
###########
###########

print()

### Our first simple program bis:

def convert ():
    for i in listoftemperatures:
        converted = (i*9/5) + 32
        print (i,'°C',converted,'°Fahrenheit')

listoftemperatures = [45,37,18,130]
convert()

# now there could be a bunch of code in between
# and after a while, we need to convert a new set of temperatures

print
print ('Some code in the middle')
print

listoftemperatures = [45,37,18,130]
convert()

# First version: 8 lines of code
# Second version: 6 lines of code
# If changed to Kelvin: changes to formula and print statement in 1 or 2 places

###########
###########
###########
