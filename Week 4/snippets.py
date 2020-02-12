### READ FROM AND WRITE TO CSV FILES

# Open a CSV file as a list of dictionaries (two-dimensional matrix)

import csv

file = open('csvtutorial.csv', 'r') # CSV file is opened

importdata = csv.DictReader(file, delimiter=';') # Filecontents written into list of dictionaries

for item in importdata:
    #print(item)
    print(item['Name'],'is',item['Age'],'years old')

###
###

# New data:

newdata = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]

# Create a new CSV file:

csv_file = open('newfile.csv','a') # Open a new file, called imdprocessed.csv, allow to append information
csv_writer = csv.writer(csv_file, delimiter=';') # Define csv writer, set the delimiter
csv_writer.writerow(['Course','Grade']) # Write the first row, containing variable names
csv_file.close # Close file

for item in newdata:

     csv_file = open('newfile.csv','a') # Open file, allow to append
     csv_writer = csv.writer(csv_file, delimiter=';') # Not necessary, but reset delimiter
     csv_writer.writerow([
                         item['Course'],
                         item['Grade'],
                         ]) # Write result row
     csv_file.flush() # Force to flush
     csv_file.close # Close file

###
