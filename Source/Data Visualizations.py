#!/usr/bin/env python
# coding: utf-8

# ## Python Script Overview
# 
# This Python code involves data loading, visualization, and analysis tasks using pandas, matplotlib, seaborn, and wordcloud libraries. Below is a summary of each section:
# 
#    1. Importing Libraries: Imports necessary libraries such as pandas matplotlib.pyplot, seaborn and wordcloud.
#    
#    
#    2. Data Loading:
#        - CSV files containing datasets related to cars, owners, ownership history, vehicle condition, features, incidents, service history, and market trends are loaded into Pandas DataFrames.
#    
#    
#    3. Data Visualizations:
#        - **Histogram of Car Mileage:** Visualizes the distribution of car mileage using a histogram to understand the range and spread of mileage among the vehicles.
#        - **Bar Chart of Car Makes:** Shows the frequency of different car makes in the dataset using a bar chart.
#        - **Box Plot of Car Prices:** Displays the distribution of car prices using a box plot to identify outliers and understand price ranges.
#        - **Scatter Plot of Car Price vs. Mileage:** Explores the relationship between car price and mileage using a scatter plot.
#        - **Line Chart of Average Sale Price Over Time:** Illustrates the trend of average sale prices of vehicles over time using a line chart.
#        - **Bar Chart of Market Demand by Car Make:** Visualizes the market demand for different car makes using a bar chart.
#        - **Pie Chart of Transmission Types:** Displays the distribution of transmission types among vehicles using a pie chart.
#        - **Heatmap of Correlation Matrix:** Generates a heatmap to visualize the correlation matrix between numerical variables.
#        - **Pair Plot of Select Features:** Creates a pair plot to visualize relationships between multiple variables.
#        - **Violin Plot of Car Prices by Make:** Combines a box plot with a kernel density plot to show the distribution of car prices for each make.
#        - **Bar Chart of Ownership Duration:** Illustrates the frequency of ownership durations for vehicles using a bar chart.
#        - **Line Chart of Mileage Over Time:** Demonstrates how the mileage of vehicles changes over time using a line chart.
#        - **Stacked Bar Chart of Features by Car Make:** Visualizes the prevalence of features for each car make using a stacked bar chart.
#        - **Histogram of Sale Prices by State:** Displays the distribution of sale prices for each state using a histogram.
#        - **Word Cloud of Incident Descriptions:** Creates a word cloud to visualize the most common types of incidents reported for vehicles.
#    
#     
# Each visualization provides insights into various aspects of the dataset, including distributions, trends, correlations, and market demand. These visualizations aid in understanding the data and extracting valuable information for analysis and decision-making.
# 
# For the code for each of the above components, I will re-iterate with in-line comments what is mentioned above to identify what code corresponds to which component from above. Also to keep the context consistent.

# # ----------------------------------- Start Python Script -----------------------------------------------

# In[1]:


# 1. Importing Necessary Libraries
# ---------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


# In[2]:


# 2. Data loading - using pandas function ".read_csv()" since in my prior script I retrieved the data from my SQL database,
# cleaned it, and saved it to .csv files on my own machine. 
# ---------------------------------------------------------------------------------------------------------------------------

Cars_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Cars_df.csv')

Owners_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Owners_df.csv')

OwnershipHistory_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\OwnershipHistory_df.csv')

VehicleCondition_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\VehicleCondition_df.csv')

Features_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Features_df.csv')

Incidents_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Incidents_df.csv')

ServiceHistory_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\ServiceHistory_df.csv')

MarketTrends_df = pd.read_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\MarketTrends_df.csv')


# In[3]:


# 3. Data Visualizations: Histogram of Car Mileage
# ---------------------------------------------------------------------------------------------------------------------------

# Histogram of Car Mileage: Visualize the distribution of car mileage to understand the range and spread of 
# mileage among the vehicles in your database. This can help identify common mileage ranges and outliers.

plt.figure(figsize=(10, 6))
plt.hist(Cars_df['Mileage'], bins=20, color='skyblue', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Histogram of Car Mileage')
plt.xlabel('Mileage')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# ### Histogram of Car Mileage Interpretation:
# 
# The histogram of car mileage shows the distribution of mileage across vehicles in the dataset. The x-axis represents the mileage, divided into bins, and the y-axis represents the frequency of cars within each mileage bin. 
# 
# The distribution appears to be right-skewed, meaning there are a significant number of cars with lower mileage compared to high mileage. This could suggest that newer, less-used cars are more common in the dataset. There are also cars with very high mileage, which could be outliers or represent a segment of older, well-used vehicles. 
# 
# Overall, the histogram is useful for identifying the range and spread of mileage, as well as for spotting common mileage ranges and potential outliers.
# 
# 

# In[4]:


# 3. Data Visualizations: Bar Chart of Car Makes
# ---------------------------------------------------------------------------------------------------------------------------

# Bar Chart of Car Makes: Create a bar chart showing the frequency of different car makes in your database. 
# This can provide insights into the most popular car brands among the available used vehicles.

car_make_counts = Cars_df['Make'].value_counts()

# Plot bar chart of car makes
plt.figure(figsize=(12, 6))
car_make_counts.plot(kind='bar', color='skyblue')
plt.title('Bar Chart of Car Makes')
plt.xlabel('Car Make')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines to y-axis
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# ### Bar Chart of Car Makes Interpretation:
# 
# The bar chart represents the frequency of different car makes within a database. Each bar corresponds to a car make and the height of the bar indicates how many times each make appears in the dataset. 
# 
# The chart shows a descending order of frequency, with the leftmost bar (the most frequent make) being the highest and each subsequent bar getting progressively shorter, indicating fewer occurrences of each car make. 
# 
# This visualization helps in quickly identifying the most and least common car makes in the database and can be a useful tool for understanding the distribution of car makes, which could be important for market analysis, inventory management, or consumer preference studies.
# 
# 

# In[25]:


# 3. Data Visualizations: Box Plot of Car Prices
# ---------------------------------------------------------------------------------------------------------------------------

# Box Plot of Car Prices: Use a box plot to visualize the distribution of car prices, including measures of central tendency
# (median) and variability (interquartile range). This can help identify outliers and understand the 
# price range for different types of vehicles.

# Currently my Cars_df does not have information on the sales prices for the various vehicles, so I need to 
# merge my Cars_df with my OwnershipHistory_df to obtain the sales prices.


data_df = pd.merge(Cars_df, OwnershipHistory_df[['CarID', 'SalePrice']], on='CarID', how='left')
data_df.head(5)


# In[26]:


# there are some NaN in SalePrice due to gaps in the OwnershipHistory with respect to the CarID. I will replace the NaN 
# values with the average of the Non-NaN values in SalePrice

average_sale_price = data_df['SalePrice'].mean()
data_df['SalePrice'].fillna(average_sale_price, inplace=True)
data_df.head(5)


# In[7]:


# Create a box plot of car prices
plt.figure(figsize=(10, 6))
sns.boxplot(x='SalePrice', data=data_df, color='skyblue')
plt.title('Box Plot of Car Prices')
plt.xlabel('Price')
plt.ylabel('Distribution')
plt.grid(axis='y')  # Add gridlines to y-axis
plt.show()


# ### Box Plot of Car Prices Interpretation:
# 
# The box plot visualizes the distribution of car prices. It's designed to show the median price, the interquartile range (IQR), and any potential outliers. The median is represented by the line inside the box, the IQR by the box itself, and outliers by dots outside the whiskers. This plot indicates that there is a wide range of prices.

# In[8]:


# 3. Data Visualizations: Scatter Plot of Car Price vs. Mileage
# ---------------------------------------------------------------------------------------------------------------------------

# Scatter Plot of Car Price vs. Mileage: Explore the relationship between car price and mileage by creating a scatter plot. 
# This can help identify any trends or patterns, such as whether higher mileage correlates with lower prices.

# Create a scatter plot of car price vs. mileage
plt.figure(figsize=(10, 6))
plt.scatter(data_df['Mileage'], data_df['SalePrice'], color='orange', alpha=0.5)
plt.title('Scatter Plot of Car Price vs. Mileage')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.grid(True)  # Add gridlines
plt.show()


# ### Scatter Plot of Car Price vs. Mileage Interpretation:
# 
# The scatter plot of car price versus mileage shows a distribution of individual car sales, with the price on the y-axis and mileage on the x-axis. 
# 
# The plot does not show a clear trend or pattern that would suggest a strong correlation between higher mileage and lower prices.
# 
# The points are widely dispersed across the graph, which could indicate a lot of variability in car prices that is not solely explained by mileage. This may imply that while mileage could be a factor in the pricing of cars, other factors such as make, model, condition, and market trends may also significantly influence the sale price.

# In[9]:


# 3. Data Visualizations: Line Chart of Average Sale Price Over Time
# ---------------------------------------------------------------------------------------------------------------------------

# Line Chart of Average Sale Price Over Time: If your data includes sale dates, create a line chart showing the 
# average sale price of vehicles over time. This can help identify trends in pricing and seasonality effects.

# Group by date and calculate the average sale price
average_price_over_time = MarketTrends_df.groupby('Date')['AverageSalePrice'].mean()

# Convert the index to datetime for proper plotting
average_price_over_time.index = pd.to_datetime(average_price_over_time.index)

# Create a line plot of average sale price over time
plt.figure(figsize=(10, 6))
average_price_over_time.plot(color='blue', marker='o')
plt.title('Average Sale Price Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sale Price')
plt.grid(True)  # Add gridlines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# The above is quite chaotic with a significant amount of overlap in data points, making it difficult to discern any clear trends or patterns.
# 
# In order to enhance readability and interpretability I will simplify the plot by using a 30 day rolling average to smooth out short-term fluctuations and highlight longer-term trends.

# In[15]:


# 3. Data Visualizations: Line Chart of Average Sale Price Over Time (Simplified)
# ---------------------------------------------------------------------------------------------------------------------------

rolling_window_size = 30
average_price_over_time = MarketTrends_df.groupby('Date')['AverageSalePrice'].mean()
average_price_over_time.index = pd.to_datetime(average_price_over_time.index)
smoothed_data = average_price_over_time.rolling(window=rolling_window_size).mean()

plt.figure(figsize=(10, 6))
plt.plot(smoothed_data, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
plt.title('Smoothed Average Sale Price Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sale Price')
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust Layout to prevent overlapping Labels
plt.show()


# ### Line Chart of Average Sale Price Over Time Interpretation:
# 
# The new plot with the smoothed average sale price over time provides a clearer view of the overall trend compared to the previous one. 
# 
# The application of the rolling mean has reduced the noise, making it easier to see the general direction in which the average sale prices are moving. While the plot still shows variability, the extreme short-term fluctuations are toned down. 
# 
# It seems that there are still some fluctuations that could represent seasonal trends or other cyclical factors affecting car prices, but the general trend over time is now more discernible.

# In[10]:


# 3. Data Visualizations: Bar Chart of Market Demand by Car Make
# ---------------------------------------------------------------------------------------------------------------------------

# Bar Chart of Market Demand by Car Make: If available, visualize the market demand for different car makes using a bar chart.
# This can provide insights into which car brands are currently in high demand among buyers.

# Currently my MarketTrends_df does not have information on the make for the various vehicles, so I need to 
# merge my Cars_df with my MarketTrends_df to obtain the vehicle make.

data_df2 = pd.merge(MarketTrends_df, Cars_df[['CarID', 'Make']], on='CarID', how='left')
data_df2.head()


# In[11]:


# Group by car make and calculate the total market demand
market_demand_by_make = data_df2.groupby('Make')['MarketDemand'].sum()

# Sort the data by market demand in descending order
market_demand_by_make_sorted = market_demand_by_make.sort_values(ascending=False)

# Create a bar plot of market demand by car make
plt.figure(figsize=(10, 6))
market_demand_by_make_sorted.plot(kind='bar', color='skyblue')
plt.title('Market Demand by Car Make')
plt.xlabel('Car Make')
plt.ylabel('Market Demand')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines to the y-axis only
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# The above specific values and rankings are not discernible from the text description alone. In order to enhance readability and interpretability I will simplify the plot by grouping my makes into 10 various categories as follows;
# 
# **Luxury Brands:**
# 
#    - European Luxury: Aston Martin, Audi, Bentley, BMW, Ferrari, Lamborghini, Lotus, Maserati, Maybach, McLaren, Mercedes-Benz, Porsche, Rolls-Royce
# 
#    - American Luxury: Cadillac, Lincoln, Tesla
# 
#    - Asian Luxury: Acura, Genesis, INFINITI, Lexus
# 
# 
# **Mainstream Brands:**
# 
#    - European Mainstream: Alfa Romeo, FIAT, MINI, Volkswagen, Volvo
# 
#    - American Mainstream: Buick, Chevrolet, Chrysler, Dodge, Ford, GMC, Jeep, Ram
# 
#    - Asian Mainstream: Honda, Hyundai, Kia, Mazda, Mitsubishi, Nissan, Subaru, Toyota
# 
# 
# **Special Categories:**
# 
#    - Exotic/Super Sports: Ferrari, Lamborghini, McLaren
# 
#    - Discontinued or Niche: Daewoo, Eagle, Geo, HUMMER, Isuzu, Mercury, Oldsmobile, Panoz, Plymouth, Pontiac, Saab, Saturn, Scion, smart, Suzuki
# 
# 
# **Electric Vehicle (EV) and Hybrid Focus:**
# 
#    - Dedicated EV Brands: Tesla
# 
# 
# **Commercial Vehicles:**
# 
#    - Commercial/Fleet: Freightliner 

# In[21]:


data_df3 = pd.merge(MarketTrends_df, Cars_df[['CarID', 'Make']], on='CarID', how='left')

# Dictionary that maps makes to groups
make_to_group = {
    # European Luxury
    'aston martin': 'European Luxury', 'audi': 'European Luxury', 'bentley': 'European Luxury',
    'bmw': 'European Luxury', 'lotus': 'European Luxury', 'maserati': 'European Luxury',
    'maybach': 'European Luxury', 'mercedes-benz': 'European Luxury', 'porsche': 'European Luxury',
    'rolls-royce': 'European Luxury',
    
    # American Luxury
    'cadillac': 'American Luxury', 'lincoln': 'American Luxury',
    
    # Asian Luxury
     'acura': 'Asian Luxury', 'genesis': 'Asian Luxury', 'infiniti': 'Asian Luxury', 'lexus': 'Asian Luxury',
    
    # European Mainstream
    'alfa romeo': 'European Mainstream', 'fiat': 'European Mainstream', 'mini': 'European Mainstream',
    'volkswagen': 'European Mainstream', 'volvo': 'European Mainstream',
    
    # American Mainstream
    'buick': 'American Mainstream', 'chevrolet': 'American Mainstream', 'chrysler': 'American Mainstream',
    'dodge': 'American Mainstream', 'ford': 'American Mainstream', 'gmc': 'American Mainstream',
    'jeep': 'American Mainstream', 'ram': 'American Mainstream',
    
    # Asian Mainstream
    'honda': 'Asian Mainstream', 'hyundai': 'Asian Mainstream', 'kia': 'Asian Mainstream',
    'mazda': 'Asian Mainstream', 'mitsubishi': 'Asian Mainstream', 'nissan': 'Asian Mainstream',
    'subaru': 'Asian Mainstream', 'toyota': 'Asian Mainstream',
    
    # Exotic/Super Sports
    'ferrari': 'Exotic/Super Sports', 'lamborghini': 'Exotic/Super Sports', 'mclaren': 'Exotic/Super Sports',
    
    # Discontinued or Niche
    'daewoo': 'Discontinued or Niche', 'eagle': 'Discontinued or Niche', 'geo': 'Discontinued or Niche',
    'hummer': 'Discontinued or Niche', 'isuzu': 'Discontinued or Niche', 'mercury': 'Discontinued or Niche',
    'oldsmobile': 'Discontinued or Niche', 'panoz': 'Discontinued or Niche', 'plymouth': 'Discontinued or Niche',
    'pontiac': 'Discontinued or Niche', 'saab': 'Discontinued or Niche', 'saturn': 'Discontinued or Niche',
    'scion': 'Discontinued or Niche', 'smart': 'Discontinued or Niche', 'suzuki': 'Discontinued or Niche',
    
    # Dedicated EV Brands
    'tesla': 'Dedicated EV',
    
    # Commercial Vehicles
    'freightliner': 'Commercial/Fleet'
}

# Map the 'Make' column to a new 'Group' column
data_df3['MakeGroup'] = data_df3['Make'].map(make_to_group)

# Fill any missing groups with a default category or leave as NaN
data_df3['MakeGroup'] = data_df3['MakeGroup'].fillna('Other')
data_df3


# In[23]:


# Group by car makegroup and calculate the total market demand
market_demand_by_make = data_df3.groupby('MakeGroup')['MarketDemand'].sum()

# Sort the data by market demand in descending order
market_demand_by_make_sorted = market_demand_by_make.sort_values(ascending=False)

# Create a bar plot of market demand by car make
plt.figure(figsize=(10, 6))
market_demand_by_make_sorted.plot(kind='bar', color='skyblue')
plt.title('Market Demand by Car Make Grouping')
plt.xlabel('Make Group')
plt.ylabel('Market Demand')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines to the y-axis only
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


# ### Bar Chart of Market Demand by Car Make Group Interpretation:
# 
# The bar chart displays the aggregated market demand for each defined group of car makes. The tallest bar, representing the highest market demand, seems to correspond to the "American Mainstream" category, indicating that this group has the highest demand in the market according to the dataset. 
# 
# Following this, the "Asian Mainstream" and "European Luxury" groups also show significant market demand. The chart simplifies the analysis by consolidating individual car makes into broader categories, which allows for easier comparison of market demand across different segments of the automotive industry.

# In[12]:


# 3. Data Visualizations: Pie Chart of Transmission Types
# ---------------------------------------------------------------------------------------------------------------------------

# Pie Chart of Transmission Types: Create a pie chart to visualize the distribution of transmission types 
# (e.g., automatic, manual) among the vehicles in your database. This can help understand the prevalence 
# of different transmission options.

# Count the frequency of each transmission type
transmission_counts = Cars_df['TransmissionType'].value_counts()

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(transmission_counts, labels=transmission_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Transmission Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# ### Pie Chart of Transmission Types Interpretation:
# 
# The pie chart illustrates the distribution of transmission types across a set of vehicles. It shows three segments:
# 
#    - Automatic transmission vehicles make up 34.7% of the dataset.
#    - Manual transmission vehicles constitute 31.7%.
#    - CVT (Continuously Variable Transmission) represents 33.6%.
#    
# The distribution is relatively even among the three transmission types, indicating a diverse set of preferences or availabilities in the market. No single transmission type dominates, suggesting that consumers have a balanced selection of transmission options when choosing vehicles.

# In[13]:


# 3. Data Visualizations: Heatmap of Correlation Matrix
# ---------------------------------------------------------------------------------------------------------------------------

# Heatmap of Correlation Matrix: Generate a heatmap to visualize the correlation matrix between numerical variables 
# such as mileage, price, and year. This can help identify correlations between different attributes of the vehicles.

# Selecting numerical columns for correlation analysis
numerical_columns = ['Mileage', 'SalePrice', 'Year']  # Adjust as per your DataFrame

# Calculating correlation matrix
correlation_matrix = data_df[numerical_columns].corr()

# Plotting heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()


# ### Heatmap of Correlation Matrix Interpretation:
# 
# The heatmap shows the Pearson correlation coefficients between three numerical variables: 'Mileage', 'SalePrice', and 'Year'. The coefficients range from -1 to 1, where 1 would indicate a perfect positive correlation, -1 a perfect negative correlation, and 0 no linear correlation.
# 
# In this heatmap:
# 'Mileage' and 'SalePrice' have a coefficient close to 0, indicating no significant linear relationship.
# 'Mileage' and 'Year' also have a coefficient close to 0, suggesting no significant linear relationship.
# 'SalePrice' and 'Year' have a coefficient close to 0, indicating no significant linear relationship as well.
# 
# The results suggest that there is no strong linear correlation between these three variables based on the data provided.

# In[14]:


# 3. Data Visualizations: Pair Plot of Select Features
# ---------------------------------------------------------------------------------------------------------------------------

# Pair Plot of Select Features: If your database includes additional features such as engine type or fuel type, create 
# a pair plot to visualize relationships between multiple variables simultaneously. This can help identify interesting
# patterns or clusters in the data.

# Selecting features for pair plot
selected_features = ['Mileage', 'SalePrice', 'Year', 'EngineType', 'FuelType']

# Creating pair plot
sns.pairplot(data_df[selected_features])
plt.title('Pair Plot of Select Features')
plt.show()


# ### Pair Plot of Select Features Interpretation:
# 
# The pair plot visualizes the relationships between the variables 'Mileage', 'SalePrice', 'Year', 'EngineType', and 'FuelType'. However, 'EngineType' and 'FuelType' are categorical and not shown in the pair plot. 
# 
# The scatter plots for numerical data don't show any clear linear relationships between the variables, as points are widely scattered. The histograms on the diagonal provide distributions for each variable, with 'Year' showing a concentration of more recent years, and 'SalePrice' and 'Mileage' showing wide ranges. 
# 
# This kind of visualization is useful for identifying patterns, trends, and outliers across multiple dimensions of the data.

# In[15]:


# 3. Data Visualizations: Violin Plot of Car Prices by Make
# ---------------------------------------------------------------------------------------------------------------------------

# Violin Plot of Car Prices by Make: This plot combines a box plot with a kernel density plot to show the distribution 
# of car prices for each make. It provides a clearer view of the price distribution compared to a traditional box plot.

# Set the style of the plot
sns.set(style="whitegrid")

# Create the violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='Make', y='SalePrice', data=data_df)
plt.title('Violin Plot of Car Prices by Make')
plt.xlabel('Car Make')
plt.ylabel('SalePrice')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# Again, the above specific values and rankings are not discernible from the text description alone. In order to enhance readability and interpretability I will use my newly created MakeGroup to simplify the plot.

# In[28]:


# 3. Data Visualizations: Violin Plot of Car Prices by MakeGroup
# ---------------------------------------------------------------------------------------------------------------------------

# Dictionary that maps makes to groups
make_to_group = {
    # European Luxury
    'aston martin': 'European Luxury', 'audi': 'European Luxury', 'bentley': 'European Luxury',
    'bmw': 'European Luxury', 'lotus': 'European Luxury', 'maserati': 'European Luxury',
    'maybach': 'European Luxury', 'mercedes-benz': 'European Luxury', 'porsche': 'European Luxury',
    'rolls-royce': 'European Luxury',
    
    # American Luxury
    'cadillac': 'American Luxury', 'lincoln': 'American Luxury',
    
    # Asian Luxury
     'acura': 'Asian Luxury', 'genesis': 'Asian Luxury', 'infiniti': 'Asian Luxury', 'lexus': 'Asian Luxury',
    
    # European Mainstream
    'alfa romeo': 'European Mainstream', 'fiat': 'European Mainstream', 'mini': 'European Mainstream',
    'volkswagen': 'European Mainstream', 'volvo': 'European Mainstream',
    
    # American Mainstream
    'buick': 'American Mainstream', 'chevrolet': 'American Mainstream', 'chrysler': 'American Mainstream',
    'dodge': 'American Mainstream', 'ford': 'American Mainstream', 'gmc': 'American Mainstream',
    'jeep': 'American Mainstream', 'ram': 'American Mainstream',
    
    # Asian Mainstream
    'honda': 'Asian Mainstream', 'hyundai': 'Asian Mainstream', 'kia': 'Asian Mainstream',
    'mazda': 'Asian Mainstream', 'mitsubishi': 'Asian Mainstream', 'nissan': 'Asian Mainstream',
    'subaru': 'Asian Mainstream', 'toyota': 'Asian Mainstream',
    
    # Exotic/Super Sports
    'ferrari': 'Exotic/Super Sports', 'lamborghini': 'Exotic/Super Sports', 'mclaren': 'Exotic/Super Sports',
    
    # Discontinued or Niche
    'daewoo': 'Discontinued or Niche', 'eagle': 'Discontinued or Niche', 'geo': 'Discontinued or Niche',
    'hummer': 'Discontinued or Niche', 'isuzu': 'Discontinued or Niche', 'mercury': 'Discontinued or Niche',
    'oldsmobile': 'Discontinued or Niche', 'panoz': 'Discontinued or Niche', 'plymouth': 'Discontinued or Niche',
    'pontiac': 'Discontinued or Niche', 'saab': 'Discontinued or Niche', 'saturn': 'Discontinued or Niche',
    'scion': 'Discontinued or Niche', 'smart': 'Discontinued or Niche', 'suzuki': 'Discontinued or Niche',
    
    # Dedicated EV Brands
    'tesla': 'Dedicated EV',
    
    # Commercial Vehicles
    'freightliner': 'Commercial/Fleet'
}

# Map the 'Make' column to a new 'Group' column
data_df['MakeGroup'] = data_df['Make'].map(make_to_group)

# Fill any missing groups with a default category or leave as NaN
data_df['MakeGroup'] = data_df['MakeGroup'].fillna('Other')

# Set the style of the plot
sns.set(style="whitegrid")

# Create the violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='MakeGroup', y='SalePrice', data=data_df)
plt.title('Violin Plot of Car Prices by Make Grouping')
plt.xlabel('Make Group')
plt.ylabel('SalePrice')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# ### Violin Plot of Car Prices by Make Group Interpretation:
# 
# The violin plot is a method for visualizing the distribution of a numeric variable for different categories, combining aspects of both a box plot and a kernel density plot. In this case, the plot shows the distribution of 'SalePrice' for different car makes.
# 
# Each 'violin' represents a car make. The width of each violin indicates the density of the data points at different price levels, with wider sections representing a higher concentration of sales at a particular price. Black bars in the center represent the interquartile range of the distribution, and the white dot represents the median sale price.
# 
# Certain groups, like "Exotic/Super Sports," likely show a higher median and a wider range of sale prices, indicating a larger variance in the price of cars in this category.
# 
# Groups like "American Mainstream" and "Asian Mainstream" show a narrower distribution, which could indicate more consistent pricing within these categories.
# 
# The presence of thick sections in the violins indicates a higher concentration of sale prices, while thin sections represent price points with fewer cars sold.
# 

# In[29]:


# 3. Data Visualizations: Bar Chart of Ownership Duration
# ---------------------------------------------------------------------------------------------------------------------------

# Bar Chart of Ownership Duration: Calculate the duration of ownership for each vehicle (SaleDate - PurchaseDate) 
# and create a bar chart showing the frequency of ownership durations. This can provide insights into how long 
# owners typically keep their vehicles before selling them.

# Convert 'PurchaseDate' and 'SaleDate' columns to datetime objects
OwnershipHistory_df['PurchaseDate'] = pd.to_datetime(OwnershipHistory_df['PurchaseDate'])
OwnershipHistory_df['SaleDate'] = pd.to_datetime(OwnershipHistory_df['SaleDate'])

# Calculate ownership duration (in days) for each vehicle
OwnershipHistory_df['OwnershipDuration'] = (OwnershipHistory_df['SaleDate'] - OwnershipHistory_df['PurchaseDate']).dt.days

# Create a bar chart of ownership durations
plt.figure(figsize=(10, 6))
OwnershipHistory_df['OwnershipDuration'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Bar Chart of Ownership Duration')
plt.xlabel('Ownership Duration (Days)')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Due to the compressed scale and the volume of data, it's challenging to discern specific patterns or to identify the most common ownership duration from this visualization. In order to enhance readability and interpretability I will simplify the plot by adjusting the bin sizes.

# In[30]:


ownership_durations = OwnershipHistory_df['OwnershipDuration']

# Define the number of bins
bin_size = 30  # days
max_duration = ownership_durations.max()
bins = range(0, max_duration + bin_size, bin_size)

# Create a histogram with the defined bins
plt.figure(figsize=(10, 6))
plt.hist(ownership_durations, bins=bins, color='skyblue', edgecolor='black')
plt.title('Histogram of Ownership Duration')
plt.xlabel('Ownership Duration (Days)')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ### Bar Chart of Ownership Duration:
# 
# A significant number of vehicles are sold within a relatively short period after purchase, as indicated by the tall bars on the left side of the histogram. The frequency decreases as the duration of ownership increases, which suggests that fewer people sell their vehicles as the length of ownership grows.
# 
# This pattern could indicate that many vehicles are sold within a certain "sweet spot" of ownership duration. Understanding this distribution helps in identifying typical ownership cycles and planning for resales or trade-ins.
# 

# In[17]:


# 3. Data Visualizations: Line Chart of Mileage Over Time
# ---------------------------------------------------------------------------------------------------------------------------

# Line Chart of Mileage Over Time: If your data includes mileage readings over time (e.g., from service history records), 
# create a line chart showing how the mileage of vehicles changes over time. This can help identify trends in 
# mileage accumulation and potential patterns related to vehicle usage.

# Currently my ServiceHistory_df does not have information on the mileage for the various vehicles, so I need to 
# merge my ServiceHistory_df with my Cars_df to obtain the mileage.

data_df3 = pd.merge(ServiceHistory_df, Cars_df[['CarID', 'Mileage']], on='CarID', how='left')
data_df3.head()


# In[18]:


# Convert 'ServiceDate' column to datetime object
data_df3['ServiceDate'] = pd.to_datetime(data_df3['ServiceDate'])

# Group by 'ServiceDate' and calculate the average mileage for each date
mileage_over_time = data_df3.groupby('ServiceDate')['Mileage'].mean()

# Create a line chart of mileage over time
plt.figure(figsize=(10, 6))
mileage_over_time.plot(kind='line', color='green', marker='o', linestyle='-')
plt.title('Line Chart of Mileage Over Time')
plt.xlabel('Service Date')
plt.ylabel('Average Mileage')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[19]:


# 3. Data Visualizations: Stacked Bar Chart of Features by Car Make
# ---------------------------------------------------------------------------------------------------------------------------

# Stacked Bar Chart of Features by Car Make: If your data includes features such as air conditioning, power windows, 
# etc., create a stacked bar chart showing the prevalence of these features for each car make. 
# This can help identify which features are most common for different brands.

# Pivot the DataFrame to get a count of each feature by car make
feature_counts = Features_df.pivot_table(index='CarID', columns='FeatureName', aggfunc='size', fill_value=0)

# Merge with the Cars DataFrame to get the make of each car
feature_counts = feature_counts.merge(Cars_df[['CarID', 'Make']], on='CarID', how='left')

# Group by make and sum the counts of each feature
feature_counts_by_make = feature_counts.groupby('Make').sum()

# Plot a stacked bar chart
plt.figure(figsize=(12, 8))
feature_counts_by_make.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Features by Car Make')
plt.xlabel('Car Make')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Feature Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# The above specific values and rankings are not discernible from the text description alone. In order to enhance readability and interpretability I will simplify the plot by using my MakeGroup column.

# In[31]:


# 3. Data Visualizations: Stacked Bar Chart of Features by Car Make Group
# ---------------------------------------------------------------------------------------------------------------------------

data_df4 = Cars_df

# Dictionary that maps makes to groups
make_to_group = {
    # European Luxury
    'aston martin': 'European Luxury', 'audi': 'European Luxury', 'bentley': 'European Luxury',
    'bmw': 'European Luxury', 'lotus': 'European Luxury', 'maserati': 'European Luxury',
    'maybach': 'European Luxury', 'mercedes-benz': 'European Luxury', 'porsche': 'European Luxury',
    'rolls-royce': 'European Luxury',
    
    # American Luxury
    'cadillac': 'American Luxury', 'lincoln': 'American Luxury',
    
    # Asian Luxury
     'acura': 'Asian Luxury', 'genesis': 'Asian Luxury', 'infiniti': 'Asian Luxury', 'lexus': 'Asian Luxury',
    
    # European Mainstream
    'alfa romeo': 'European Mainstream', 'fiat': 'European Mainstream', 'mini': 'European Mainstream',
    'volkswagen': 'European Mainstream', 'volvo': 'European Mainstream',
    
    # American Mainstream
    'buick': 'American Mainstream', 'chevrolet': 'American Mainstream', 'chrysler': 'American Mainstream',
    'dodge': 'American Mainstream', 'ford': 'American Mainstream', 'gmc': 'American Mainstream',
    'jeep': 'American Mainstream', 'ram': 'American Mainstream',
    
    # Asian Mainstream
    'honda': 'Asian Mainstream', 'hyundai': 'Asian Mainstream', 'kia': 'Asian Mainstream',
    'mazda': 'Asian Mainstream', 'mitsubishi': 'Asian Mainstream', 'nissan': 'Asian Mainstream',
    'subaru': 'Asian Mainstream', 'toyota': 'Asian Mainstream',
    
    # Exotic/Super Sports
    'ferrari': 'Exotic/Super Sports', 'lamborghini': 'Exotic/Super Sports', 'mclaren': 'Exotic/Super Sports',
    
    # Discontinued or Niche
    'daewoo': 'Discontinued or Niche', 'eagle': 'Discontinued or Niche', 'geo': 'Discontinued or Niche',
    'hummer': 'Discontinued or Niche', 'isuzu': 'Discontinued or Niche', 'mercury': 'Discontinued or Niche',
    'oldsmobile': 'Discontinued or Niche', 'panoz': 'Discontinued or Niche', 'plymouth': 'Discontinued or Niche',
    'pontiac': 'Discontinued or Niche', 'saab': 'Discontinued or Niche', 'saturn': 'Discontinued or Niche',
    'scion': 'Discontinued or Niche', 'smart': 'Discontinued or Niche', 'suzuki': 'Discontinued or Niche',
    
    # Dedicated EV Brands
    'tesla': 'Dedicated EV',
    
    # Commercial Vehicles
    'freightliner': 'Commercial/Fleet'
}

# Map the 'Make' column to a new 'Group' column
data_df4['MakeGroup'] = data_df4['Make'].map(make_to_group)

# Fill any missing groups with a default category or leave as NaN
data_df['MakeGroup'] = data_df['MakeGroup'].fillna('Other')


# Pivot the DataFrame to get a count of each feature by car make
feature_counts = Features_df.pivot_table(index='CarID', columns='FeatureName', aggfunc='size', fill_value=0)

# Merge with the Cars DataFrame to get the make of each car
feature_counts = feature_counts.merge(data_df4[['CarID', 'MakeGroup']], on='CarID', how='left')

# Group by make and sum the counts of each feature
feature_counts_by_make = feature_counts.groupby('MakeGroup').sum()

# Plot a stacked bar chart
plt.figure(figsize=(12, 8))
feature_counts_by_make.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Features by Car Make Grouping')
plt.xlabel('Make Group')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Feature Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# In[ ]:





# In[33]:


# 3. Data Visualizations: Histogram of Sale Prices by State
# ---------------------------------------------------------------------------------------------------------------------------

# Histogram of Sale Prices by State: If your data includes the state where each sale occurred, create a histogram 
#showing the distribution of sale prices for each state. This can help identify regional differences in pricing 
# and market conditions.

# Currently my OwnershipHistory_df does not have information on the state for the various vehicles, so I need to 
# merge my OwnershipHistory_df with my Owners_df to obtain the mileage.

data_df5 = pd.merge(OwnershipHistory_df, Owners_df[['OwnerID', 'State']], on='OwnerID', how='left')
data_df5.head()


# In[21]:


# Filter out any missing or invalid sale prices
valid_sale_prices = data_df5['SalePrice'].dropna()

# Plot a histogram of sale prices for each state
plt.figure(figsize=(12, 8))
for state in data_df5['State'].unique():
    state_sale_prices = data_df5.loc[data_df5['State'] == state, 'SalePrice']
    plt.hist(state_sale_prices, bins=20, alpha=0.5, label=state, density=True)

plt.title('Histogram of Sale Prices by State')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


# Due to the compressed scale and the volume of data, it's challenging to discern specific patterns from this visualization. In order to enhance readability and interpretability I will simplify the plot by grouping the states based on geogrpahic location as follows;
# 
# **Northeast:**
# 
#    - New England: CT, MA, ME, NH, RI, VT
# 
#    - Mid-Atlantic: NJ, NY, PA
# 
# 
# **Midwest:**
# 
#    - East North Central: IL, IN, MI, OH, WI
# 
#    - West North Central: IA, KS, MN, MO, ND, NE, SD
# 
# 
# **South:**
# 
#    - South Atlantic: DC, DE, FL, GA, MD, NC, SC, VA, WV
# 
#    - East South Central: AL, KY, MS, TN
#    
#    - West South Central: AR, LA, OK, TX
# 
# 
# **West:**
# 
#    - Mountain: AZ, CO, ID, MT, NM, NV, UT, WY
#    - Pacific: AK, CA, HI, OR, WA
# 
# 
# **Territories:**
# 
#    - U.S. Territories: AS (American Samoa), FM (Federated States of Micronesia), GU (Guam), MH (Marshall Islands), MP (Northern Mariana Islands), PR (Puerto Rico), PW (Palau), VI (U.S. Virgin Islands)

# In[35]:


# Define a dictionary mapping states to location categories
state_to_location = {
    # Northeast
    'CT': 'New England', 'MA': 'New England', 'ME': 'New England', 'NH': 'New England',
    'RI': 'New England', 'VT': 'New England', 'NJ': 'Mid-Atlantic', 'NY': 'Mid-Atlantic',
    'PA': 'Mid-Atlantic',
    
    # Midwest
    'IL': 'East North Central', 'IN': 'East North Central', 'MI': 'East North Central',
    'OH': 'East North Central', 'WI': 'East North Central', 'IA': 'West North Central',
    'KS': 'West North Central', 'MN': 'West North Central', 'MO': 'West North Central',
    'ND': 'West North Central', 'NE': 'West North Central', 'SD': 'West North Central',
    
    # South
    'DC': 'South Atlantic', 'DE': 'South Atlantic', 'FL': 'South Atlantic', 'GA': 'South Atlantic',
    'MD': 'South Atlantic', 'NC': 'South Atlantic', 'SC': 'South Atlantic', 'VA': 'South Atlantic',
    'WV': 'South Atlantic', 'AL': 'East South Central', 'KY': 'East South Central',
    'MS': 'East South Central', 'TN': 'East South Central', 'AR': 'West South Central',
    'LA': 'West South Central', 'OK': 'West South Central', 'TX': 'West South Central',
    
    # West
    'AZ': 'Mountain', 'CO': 'Mountain', 'ID': 'Mountain', 'MT': 'Mountain', 'NM': 'Mountain',
    'NV': 'Mountain', 'UT': 'Mountain', 'WY': 'Mountain', 'AK': 'Pacific', 'CA': 'Pacific',
    'HI': 'Pacific', 'OR': 'Pacific', 'WA': 'Pacific',
    
    # Territories
    'AS': 'U.S. Territories', 'FM': 'U.S. Territories', 'GU': 'U.S. Territories',
    'MH': 'U.S. Territories', 'MP': 'U.S. Territories', 'PR': 'U.S. Territories',
    'PW': 'U.S. Territories', 'VI': 'U.S. Territories'
}

data_df5['Location'] = data_df5['State'].map(state_to_location)

# Plot a histogram of sale prices for each location
plt.figure(figsize=(12, 8))
for location in data_df5['Location'].unique():
    state_sale_prices = data_df5.loc[data_df5['Location'] == location, 'SalePrice']
    plt.hist(state_sale_prices, bins=20, alpha=0.5, label=location, density=True)

plt.title('Histogram of Sale Prices by Geographic Location')
plt.xlabel('Sale Price')
plt.ylabel('Frequency')
plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


# Still not as clear - let's try as a boxplot.

# In[37]:


sale_prices_by_location = [data_df5[data_df5['Location'] == location]['SalePrice'].values for location in data_df5['Location'].unique()]
plt.figure(figsize=(12, 8))
plt.boxplot(sale_prices_by_location, labels=data_df5['Location'].unique())
plt.title('Boxplot of Sale Prices by Geographic Location')
plt.xlabel('Location')
plt.ylabel('Sale Price')
plt.xticks(rotation=45) 
plt.grid(True)
plt.tight_layout()
plt.show()


# ### Histogram of Sale Prices by State Duration:
# 
# Median Prices: The median sale price across most regions seems to be around the 20,000 USD to 30,000 USD range, with the median line (in orange) situated near the center of most boxes. This suggests a somewhat balanced distribution of sale prices around the median.
# 
# Variability: The interquartile ranges (IQRs) vary between regions. Some regions have a relatively small IQR, indicating that the middle 50% of the data is clustered within a narrower price range. Other regions have a larger IQR, showing a wider distribution of sale prices in the middle 50%.
# 
# Range of Prices: The range of sale prices, as indicated by the whiskers, shows significant variability between regions. Some regions have a wide range, extending from below 10,000 USD to above 40,000 USD, while others have a more compact range.
# 
# Outliers: There are a few outliers, particularly in regions such as Pacific and Mountain, indicating a few sale prices that are well above the typical range for that region. These are the data points that lie outside the ends of the whiskers.
# 
# Symmetry: The boxes for some regions, such as New England and Mid-Atlantic, are fairly symmetrical around the median, suggesting an even distribution of data points above and below the median within the IQR. In contrast, other regions show a slight asymmetry, indicating a skew in the data.
# 
# Comparison: When comparing the regions, it's noticeable that no single region appears to have a drastically different median sale price compared to the others; however, the spread of prices and the presence of outliers do vary, which could suggest differences in housing market dynamics, economic conditions, or data sample sizes across regions.
# 
# 

# In[22]:


# 3. Data Visualizations: Word Cloud of Incident Descriptions
# ---------------------------------------------------------------------------------------------------------------------------

# Word Cloud of Incident Descriptions: If your data includes incident descriptions, create a word cloud to visualize 
# the most common types of incidents reported for the vehicles in your database. This can provide insights into common 
#issues or concerns with different types of vehicles.

# Combine all incident descriptions into a single string and convert to lowercase
all_descriptions = ' '.join(Incidents_df['Description'].dropna()).lower()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_descriptions)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Incident Descriptions')
plt.axis('off')
plt.show()


# ### Word Cloud of Incident Descriptions:
# 
# Common Terms: The most prominent terms in the word cloud are "distracted", "driving", "collision", and "accident". These larger words indicate they are among the most frequently occurring in the incident descriptions.
# 
# Secondary Terms: Other notable terms that appear with some prominence are "rear", "impact", "side", "sideswipe", "improper", "turns", "aggressive", "driving", "collision", "speeding", and "drowsy". These terms are somewhat smaller than the most common terms but are still significant, suggesting they are commonly reported factors in incidents.
# 
# Safety Concerns: The prevalence of terms like "distracted", "aggressive", and "drowsy" suggests that driver behavior is a significant factor in these incidents. "Speeding" and "improper turns" also indicate common issues leading to incidents.
# 
# Types of Collisions: "Rear" and "side" may refer to the parts of the vehicles most often involved in collisions, suggesting that rear-end and side collisions are common.
# 
# Pedestrian Safety: The word "pedestrian" is visible, though not as large as some other terms, indicating that pedestrian-related incidents are also a concern but perhaps less frequent than other types of incidents.
# 
# Incident Descriptions: The size of words such as "impact" and "collision" emphasizes the nature of the incidents being described, likely involving some form of contact or crash.
# 
# 

# # ----------------------------------- END Python Script -----------------------------------------------

# In[ ]:




