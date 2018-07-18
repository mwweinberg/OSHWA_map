#python3

import csv
import json
from pprint import pprint
import pycountry
import collections

#turns the csv into a list of lists [[x, y, z,], [a, b, c]]
exampleFile = open('oshwalist.csv')
exampleReader = csv.reader(exampleFile)
oshwadata = list(exampleReader)
#removes the header
del oshwadata[0]

#imports the country geojson
with open('testcountries.geojson') as f:
    country_data = json.load(f)

#list to hold all of the countries for counting purposes
country_counter_list = []

#work through the list to pull the data
for row in oshwadata:
    #replaces the UID with the alpha_3 country code to match the json
    #gets the country by pulling the first 2 characters from the UID
    country = pycountry.countries.get(alpha_2=row[0][:2])
    #replaces the UID with the alpha_3 country code
    row[0] = country.alpha_3

    #add the country code to the list for future counting
    country_counter_list.append(row[0])

#creates a dictionary with country as key and number of occurances as value
counter = collections.Counter(country_counter_list)
print(counter)
print(counter['BGR'])

#TODO: add a new element to the json that is oshwa_count: value
# if the country code is in the counter, value = counter
# if the country code is not in the counter, value = 0


#print(country_counter_list)
#holder = country_data["features"][0]["properties"]
#pprint(holder['ISO_A3'])
