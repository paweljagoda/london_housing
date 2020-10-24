# london_mapping_main.py

import pandas as import pd

df = pd.read_csv('land-registry-house-prices-borough.csv', thousands=',')

df = df['Year'].str.slice(16,20) # reduces the year values to the YYYY format.

df.Area.unique() # generates unique values from the Area column.

# I had to manually deselect some of the areas outside of Greater London.

unique_values =  {
     'City of London', 'Barking and Dagenham', 'Barnet', 'Bexley',
     'Brent', 'Bromley', 'Camden', 'Croydon', 'Ealing', 'Enfield',
     'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Haringey',
     'Harrow', 'Havering', 'Hillingdon', 'Hounslow', 'Islington',
     'Kensington and Chelsea', 'Kingston upon Thames', 'Lambeth',
     'Lewisham', 'Merton', 'Newham', 'Redbridge',
     'Richmond upon Thames', 'Southwark', 'Sutton', 'Tower Hamlets',
     'Waltham Forest', 'Wandsworth', 'Westminster'
     }

london_values = df[df['Area'].isin(unique_values)]

