### READ FROM AND WRITE TO CSV FILES

### READING

# Open a CSV file as a list of dictionaries (two-dimensional matrix)

import csv # We need to call this module - Can't do without...

file = open('csvtutorial.csv', 'r') # CSV file is opened

importdata = csv.DictReader(file, delimiter=';') # Filecontents written into list of dictionaries

for item in importdata: # Let's loop through the data first to get a grasp of it and/or to process/manipulate it further...
    #print(item)
    print(item['Name'],'is',item['Age'],'years old')

###
###

### WRITING

# New data, hardcoded into our script:

newdata = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]

# Create a new CSV file:

csv_file = open('newfile.csv','a') # Open a new file, called imdprocessed.csv, allow to append information
csv_writer = csv.writer(csv_file, delimiter=';') # Define csv writer, set the delimiter
csv_writer.writerow(['Course','Grade']) # Write the first row, containing variable names - DO THIS ONLY ONCE...
csv_file.close # Close file

for item in newdata:

     csv_file = open('newfile.csv','a') # Open file, allow to append
     csv_writer = csv.writer(csv_file, delimiter=';') # Not necessary, but reset delimiter just to be sure...
     csv_writer.writerow([
                         item['Course'],
                         item['Grade'],
                         ]) # Write result row
     csv_file.flush() # Force to flush
     csv_file.close # Close file

###
