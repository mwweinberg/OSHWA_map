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

#TODO: replace the original holder data with the new holder data
#probably something like country_data["features"][i]["properties"] =  holder
#reversing how you pulled the info into the loop in the first place.
for i in range(0, len(country_data["features"])):
    #outputs something like {'ISO_A3': 'ABW', 'ADMIN': 'Aruba'}
    holder = country_data["features"][i]["properties"]
    print(holder)
    #if the country code is in the counter list
    if holder['ISO_A3'] in counter:
        #make oshwa_count equal to the corresponding value
        holder['oshwa_count'] = counter[holder['ISO_A3']]
    else:
        #make oshwa_count equal to zero
        holder['oshwa_count'] = 0
    #adds another pair along the lines of
    #{'ISO_A3': 'ABW', 'oshwa_count': 3, 'ADMIN': 'Aruba'}
    #holder['oshwa_count'] = 3
    print(holder)
'''
#this is just to remember how this works when you are builidng the loop above
holder = country_data["features"][0]["properties"]
print(holder)
holder['oshwa_count'] = 3
print(holder)'''




#pprint(holder['ISO_A3'])
