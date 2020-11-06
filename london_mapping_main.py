# london_mapping_main.py

import pandas as pd

# download data from https://data.london.gov.uk/dataset/average-house-prices?fbclid=IwAR1tkLuSPkLBIcIwG4RfgXiT_iq_K98cFR4o3qxpV0pxYxuCXwcAQwKN6yA

df = pd.read_csv('land-registry-house-prices-borough.csv', thousands=',')

# df['Year'] = df['df'].str.slice(16,20) # reduces the year values to the YYYY format.

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

year_list = london_values.Year.unique()

price_by_year = dict()
for year in year_list:
     price_by_year.update({year : df[df["Year"]==year]})

price_by_year['2005'] 

# view = df[df['Area'] == 'Barking and Dagenham']

# mean_values = london_values.groupby(['Area', as_index=False]).mean() # collapsing the dataset into groups of boroughs and ther mean value over 20 years.

mean_values = london_values[london_values['Measure'] == 'Mean']

def by_year(df, year):
     query = f'Dec {year}'
     return df[df['Year'].str.contains(query)]

for year in range(1995,2018):
     by_year(mean_values, year).to_csv(f'mean_values_{year}.csv')



           

# values = mean_values.rename(columns={'Area': 'NAME','Value': 'PRICE'}) # changing column names to make merging possible

import matplotlib as mlp
import matplotlib.pyplot as plt

fig, ax = plt.subplots() # initialising figure object

ax.set_xticklabels(mean_values.index,rotation=45, horizontalalignment = 'right', fontsize = '10')

plt.ion() # allows interaction with terminal, otherwise suspended.

plt.tight_layout() # ensures parts of the graph are not cut off, such as long names.

plt.show() # shows the final plot.

plt.savefig('bar_chart_mean_value.png') # saves the plot as a png file.

import geopandas as gpd
pip3 install descartes 

# download data from https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london

boroughs = gpd.read_file('./ESRI/London_Borough_Excluding_MHW.shp') # reading files in the ESRI directory

london_houses = boroughs.merge(mean_values, left_on = 'NAME', right_on = 'NAME') # merging location data with house prices

fig, ax = plt.subplots(1, 1)

# plots different prices from the PRICE column on the map.
london_houses.plot(column='PRICE', ax=ax, legend=True, legend_kwds={'label': "Mean house price per borough between 1995 and 2017 (in £)", 'orientation': "horizontal"}, cmap = 'seismic')

london_houses.plot(column='NAME', ax=ax, legend=True) # plots different boroughs with a name legend.







