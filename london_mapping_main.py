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

mean_values = london_values.groupby(['Area']).mean() # collapsing the dataset into groups of boroughs and ther mean value over 20 years.

mean_values['Value'] = mean_values.astype({'Value' : int}) # converting the mean house price into integers.

import matplotlib as mlp
import matplotlib.pyplot as plt

fig, ax = plt.subplots() # initialising figure object

ax.set_xticklabels(mean_values.index,rotation=45, horizontalalignment = 'right', fontsize = '10')

plt.ion() # allows interaction with terminal, otherwise suspended.

plt.tight_layout() # ensures parts of the graph are not cut off, such as long names.

plt.show() # shows the final plot.

plt.savefig('bar_chart_mean_value.png') # saves the plot as a png file.

