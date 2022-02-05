 import csv
 import requests
 from bs4 import BeautifulSoup

#What to scrape?
#Could add lines to a csv at each scrape-- so data should be one row: a whole bunch of details for one item.
#The soup du jour is COVID data, but I did a lot of that in Annapolis and most things are built out now-- 
#unless I could make a map of who has tests available where. But that data isn't structured, and 
#wouldn't be useful for writers, just users.
#The upside, of course, is that I know exactly how to access that data and happen to know
#it's extremely accessible.

#Let's take a look: 
#https://coronavirus.maryland.gov/search?collection=Dataset

#I do love a good zip code map. Automatically generating a map from
#scraped data would be beautiful.
#Cases per 100k by jurisdiction might be a nice easy one. It's data in the most
#human-comprehensible, comparable form, and might aid in easy comparisons of
#eastern shore vs western maryland.