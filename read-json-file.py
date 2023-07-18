import json

def getData():
  # "with" keyword provides a safe way to open and close files without exception handling boilerplate
  # this pattern can be used with any object that implements __enter__ and __exit__ methods
  with open('sample-data/songs.json', 'r') as f:
    data = json.load(f)
    return data

data = getData()

# using map
# decades = list(map(lambda x: x['decade'], data))

# using list comprehension
decades = [x['decade'] for x in data]

# nested list comprehension
# set to dedupe
artists = set([data[i]['songs'][j]['artist'] for i in range(len(data)) for j in range(len(data[i]['songs']))])

print(decades, artists)