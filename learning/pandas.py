import pandas as pd

# largely based on https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

# Series and Dataframes are the basic data structures in pandas
# Series are a list of values of the same type
# Dataframes are a collection of series - a table of rows and columns

# Viewing data
df = pd.DataFrame({"Name": ["Bill", "Amanda", "Fred"], "Age": [15, 47, 29]})
print(df)  # prints it out nicely
df.describe()  # gives a summary of the data, with count, mean, etc. for each column
df.sort_values(by="Age")  # sorts the data by the given column

# Selecting

# Setting

# Missing data

# Operations
