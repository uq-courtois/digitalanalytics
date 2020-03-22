# READING

# Import pandas
import pandas as pd

data = pd.read_csv('newdata.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

# Iterate through the imported data
for item in data:
	print(item)

### WRITING

# Import pandas
import pandas as pd

# New data, hardcoded into our script:

newdata = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]

newdata = pd.DataFrame(newdata) # Converting list of dictionaries into dataframe
newdata.to_csv('newdata.csv',sep=';',index=False) # Writing dataframe into CSV file
