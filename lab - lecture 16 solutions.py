# Look at this list of best-selling artists, particularly the table
# for those with more than 250m records sold:
# https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#   What two things should we check?

# Do the terms of service forbid it?
# https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/en

# Does the robots.txt forbid it?
# https://en.wikipedia.org/robots.txt


#2. Once verifying that we're allowed to, collect the 250m+ table
#   into a csv document.

import requests
from bs4 import BeautifulSoup
import os

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = (r"/media/Storage/Teaching/Classes/'metrics/Grad"
               r"/2023_1Spring_Data&Prog-I/Lecture 16-Automated Data Retrieval II")
file = os.path.join(path, 'wiki_table.csv')

# From the web to the Python object
response = requests.get(url)  # requests goes online
soup = BeautifulSoup(response.text, 'lxml')  # BS does not go online

# From the whole page to the table
tables = soup.find_all('table')

# From table to lists of rows
table = tables[0]
rows = table.find_all('tr')

### Method 2:
# A list comprehension to extract the <th> & <td> tags for each row
cells = [r.find_all(lambda c: c.name in ['td', 'th']) for r in rows]

# Clean the text 
text = [[t.text.strip().replace('\n', ' ') for t in c] for c in cells]

# From raw content to csv-suitable content
text_rows = [','.join(t) for t in text]
text_body = '\n'.join(text_rows)

# Write out the csv file
with open(file, 'w') as ofile:
    ofile.write(text_body)
