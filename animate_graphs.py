# animate_graphs.py

import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import geopandas as gpd
import os
from pathlib import Path
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import StrMethodFormatter
import mapclassify as mc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pylab as pl

# download data from https://data.london.gov.uk/dataset/average-house-prices?fbclid=IwAR1tkLuSPkLBIcIwG4RfgXiT_iq_K98cFR4o3qxpV0

df = pd.read_csv('land-registry-house-prices-borough.csv', thousands=',')

# generates unique values from the Area column.
df.Area.unique()

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

# list of all the unique entries in Year column
year_list = london_values.Year.unique()

# read data from https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london
london_geo_data = gpd.read_file('./ESRI/London_Borough_Excluding_MHW.shp')

# change name for borough so it matches with our data sets for merging
london_geo_data = london_geo_data.rename(columns={'NAME': 'Area'})

# save all the maps in the maps folder and create it if there isn't one
#if not os.path.exists('maps'):
#    os.makedirs('maps')

output_path = Path('maps')

# define function which selects rows in December of a chosen year.
def filter_dataframe_by_year(df, year):
     query = f'Dec {year}'
     filtered_dataframe = df[df['Year'].str.contains(query)]
     return filtered_dataframe

# selects all the mean house values
mean_values = london_values[london_values['Measure'] == 'Mean']

# preparing a folder for the data sets
#if not os.path.exists('mean_price'):
#    dir = os.makedirs('mean_price')

# generates a mean house value for a given year and saves it in the current directory
for year in range(1995,2018):
     filter_dataframe_by_year(mean_values, year).to_csv(f'mean_values_{year}.csv')

# list of generated datasets
list_of_years = [
"mean_values_1995.csv",
"mean_values_1996.csv",
"mean_values_1997.csv",
"mean_values_1998.csv",
"mean_values_1999.csv",
"mean_values_2000.csv",
"mean_values_2001.csv",
"mean_values_2002.csv",
"mean_values_2003.csv",
"mean_values_2004.csv",
"mean_values_2005.csv",
"mean_values_2006.csv",
"mean_values_2007.csv",
"mean_values_2008.csv",
"mean_values_2009.csv",
"mean_values_2010.csv",
"mean_values_2011.csv",
"mean_values_2012.csv",
"mean_values_2013.csv",
"mean_values_2014.csv",
"mean_values_2015.csv",
"mean_values_2016.csv",
"mean_values_2017.csv",
]
# set the min and max range for the choropleth map. Minimal value in 1995 and maximal value in 2017
vmin, vmax = 47528, 2092485

# start the for loop to create one map per year
def generate_plot_of_house_prices(year):

    # load data for particular year
    df = pd.read_csv(year)

    # merge mean house price data set with geographical data
    geo_year = london_geo_data.merge(df, left_on = 'Area', right_on = 'Area')

    # create map, added plt.Normalize to keep the legend range the same for all maps
    fig = geo_year.plot(column='Value',
                        cmap='OrRd',
                        figsize=(15,10),
                        linewidth=0.8,
                        edgecolor='1',
                        vmin=vmin,
                        vmax=vmax,
                        legend=True,
                        norm=plt.Normalize(vmin=vmin, vmax=vmax))

    # Get colourbar from second axis and customise the legend ticks
    colourbar = fig.get_figure().get_axes()[1]
    yticks = np.arange(40000,2200000, 293500) # had to be fine-tuned.
    colourbar.set_yticklabels(['£{:,}'.format(ytick) for ytick in yticks])

    # remove axis of chart
    fig.axis('off')

    # add a title to map
    fig.set_title('House Prices in London', \
              fontdict={'fontsize': '25',
                         'fontweight' : '3'})

    # create and position the Year annotation to the bottom left
    only_year = year[12:-4]
    fig.annotate(only_year,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)

    # this will save the figure as a high-res png in the output path.
    filepath = output_path / (only_year + '_price.png')
    chart = fig.get_figure()
    chart.savefig(filepath, dpi=300)

# generates maps
for year in list_of_years:
    generate_plot_of_house_prices(year=year)

# CREATING A TIMELAPSE FROM THE MAPS

#os.chdir('./maps')

# counter for the for loop
#i = 0

# converts png files into jpeg using Mac's sips program - at the moment needs to be entered in terminal
#os.system('for i in *.png; do sips -s format jpeg -s formatOptions 70 "${i}" --out "${i%png}jpg"; done')

# creates a gif file from all the maps. used 'brew install imagemagick'- at the moment needs to be entered in terminal#
#os.system('convert -delay 60 -loop 0 *jpg house_price_timelapse.gif')
