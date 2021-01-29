import pandas as pd
import geopandas
import matplotlib.pyplot as plt

# Load the data from CSV and set index
gdp_world_data = pd.read_csv('gdp_world_data.csv', index_col=0)
gdp_world_data = gdp_world_data.set_index('Country (or dependent territory)')

# Calculate new columns of data
gdp_world_data['2000-2019 GDP growth'] = gdp_world_data['2019'] - gdp_world_data['2000']
gdp_world_data['2000-2019 GDP % growth'] = round(gdp_world_data['2000-2019 GDP growth']/ gdp_world_data['2000']*100, 2)

# Create a view of data and rename columns
gdp_world_data = gdp_world_data.loc[:, ['2000', '2019', '2000-2019 GDP growth', '2000-2019 GDP % growth']]
gdp_world_data.columns = ['2000', '2019', 'Growth', '%-growth']

# Remove all NaN columns
gdp_world_data = gdp_world_data.dropna()

# Create a world map
map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
map = map.set_index('name')
# Change some index names to make a join on gdp_world_data
index_change = {'United States of America':'United States',
                'Central African Rep.': 'Central African Republic',
                'Dem. Rep. Congo': 'Democratic Republic of the Congo',
                'Solomon Is.': 'Solomon Islands',
                'Eq. Guinea': 'Equatorial Guinea',
                'Dominican Rep.': 'Dominican Republic'
                }
map = map.rename(index=index_change)

# Joining data sourses
data = map.join(gdp_world_data, how='outer')

# Set output options
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 300)

# Visualise the data
data['Growth per capita'] = data['Growth']/data['pop_est']
data.plot('Growth per capita', legend = True, figsize=(15,6))
# data.plot('%-growth', legend = True, figsize=(15,6))
plt.show()

# New data set on minimum wages
min_wages = pd.read_csv('min_wages.csv', index_col=0)
min_wages = min_wages.set_index('Country')
min_wages = min_wages.loc[:, ['Workweek (hours)[2]', 'Nominal hourly (US$)[6]']]
min_wages.columns = ['Hours/week', 'US$/hour']

# Join it to the main dataset
data = data.join(min_wages)
data['Hours/week'] = pd.to_numeric(data['Hours/week'], errors='coerce')

print(data)
print("---------------------------- CORELATION ----------------------------")
print(data.corr())