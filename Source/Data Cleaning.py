#!/usr/bin/env python
# coding: utf-8

# ## Python Script Overview
# 
# This Python code performs various data cleaning and preprocessing tasks on multiple dataframes related to automotive data. Here's a summary of what each part of the code does:
# 
#    1. Importing Libraries: Imports necessary libraries such as mysql.connector, pandas, matplotlib.pyplot, LabelEncoder from sklearn.preprocessing, and datetime.
#    
#    
#    2. Data Retrieval: Retrieves data from MySQL database tables into separate pandas DataFrames.
#    
#    
#    3. Handling Missing Values: Checks for missing values in each DataFrame.
#    
#     
#    4. Outlier Detection and Handling: 
#        - Visualizes the distribution of the 'Mileage' column using a box plot.
#        - Filters out outliers from the 'Mileage' column using the 99th percentile.
#        - Filters data based on specified date ranges for the 'OwnershipHistory' table.
#        - Identifies outliers in the 'VehicleCondition' table using the Interquartile Range (IQR) method.
#    
#     
#    5. Standardizing Data Formats: Standardizes date columns in several DataFrames.
#    
#     
#    6. Saving Cleaned Datasets: Saves cleaned DataFrames to CSV files.
#    
#     
# Overall, this code prepares the data for further analysis and visualization by handling missing values, outliers, and standardizing formats. Finally, it saves the cleaned datasets for future use.
# 
# For the code for each of the above components, I will re-iterate with in-line comments what is mentioned above to identify what code corresponds to which component from above. Also to keep the context consistent.

# # ----------------------------------- Start Python Script -----------------------------------------------

# In[1]:


# 1. Importing Necessary Libraries
# ---------------------------------------------------------------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# The following 45 lines of code pertain to the cleaning of my datasets. By cleaning I am referring to the handling of 
# missing values, addressing outliers, and standardizing my data formats to ensure I have final 'clean' datasets 
# or further analysis and visualization. First we will tackle any missing values.

# In[2]:


# 2A. Connect to database for sunsequent data retrieval
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 2B. Actual data retrieval
# ---------------------------------------------------------------------------------------------------------------------------

Cars_df = pd.read_sql_query("SELECT * FROM Cars", conn)
Owners_df = pd.read_sql_query("SELECT * FROM Owners", conn)
OwnershipHistory_df = pd.read_sql_query("SELECT * FROM OwnershipHistory", conn)
VehicleCondition_df = pd.read_sql_query("SELECT * FROM VehicleCondition", conn)
Features_df = pd.read_sql_query("SELECT * FROM Features", conn)
Incidents_df = pd.read_sql_query("SELECT * FROM Incidents", conn)
ServiceHistory_df = pd.read_sql_query("SELECT * FROM ServiceHistory", conn)
MarketTrends_df = pd.read_sql_query("SELECT * FROM MarketTrends", conn)


# In[4]:


# 3. Handling missing values
# ---------------------------------------------------------------------------------------------------------------------------

# Check for missing values in each dataframe
Cars_missing_values = Cars_df.isna().sum()
Owners_missing_values = Owners_df.isna().sum()
OwnershipHistory_missing_values = OwnershipHistory_df.isna().sum()
VehicleCondition_missing_values = VehicleCondition_df.isna().sum()
Features_missing_values = Features_df.isna().sum()
Incidents_missing_values = Incidents_df.isna().sum()
ServiceHistory_missing_values = ServiceHistory_df.isna().sum()
MarketTrends_missing_values = MarketTrends_df.isna().sum()


# In[5]:


Cars_missing_values


# In[6]:


Owners_missing_values


# In[7]:


OwnershipHistory_missing_values


# In[8]:


VehicleCondition_missing_values


# In[9]:


Features_missing_values


# In[10]:


Incidents_missing_values


# In[11]:


ServiceHistory_missing_values


# In[12]:


MarketTrends_missing_values


# In[13]:


# Based on initial findings above, it appears as though I luckily do not have to deal with any missing values - which
# does make sense based on the simple fact that I generated the data myself and made sure every datapoint was populated
# in each of my tables.


# In[14]:


# There are some points of interest (dataframe columns) that I would like to examine for outliers however. 


# In[15]:


# 4. Outlier Detection and Handling
# ---------------------------------------------------------------------------------------------------------------------------

# Visualize distribution of 'Mileage' using a box plot
plt.boxplot(Cars_df['Mileage'])
plt.xlabel('Mileage')
plt.title('Box Plot of Mileage')
plt.show()


# In[16]:


Cars_df.describe()


# In[17]:


# Filtering outliers from the 'Mileage' column

mileage_threshold = Cars_df['Mileage'].quantile(0.99)
Cars_df = Cars_df[Cars_df['Mileage'] <= mileage_threshold]


# In[18]:


Cars_df.describe()


# In[19]:


# For my ownershiphistory data I am not interested in data for records before the year 2020 or after the year 2023.   


# In[20]:


# Check min date value
OwnershipHistory_df['SaleDate'].min()


# In[21]:


# Check max date value
OwnershipHistory_df['SaleDate'].max()


# In[22]:


# Create custom start and end date variables

start_date = pd.to_datetime('2020-01-01')
end_date = pd.to_datetime('2024-01-01')


# In[23]:


# Filtering data based on specified date ranges

OwnershipHistory_df = OwnershipHistory_df[(OwnershipHistory_df['PurchaseDate'] >= start_date) & (OwnershipHistory_df['PurchaseDate'] <= end_date)]
OwnershipHistory_df = OwnershipHistory_df[(OwnershipHistory_df['SaleDate'] >= start_date) & (OwnershipHistory_df['SaleDate'] <= end_date)]


# In[24]:


# Check min date value after change
OwnershipHistory_df['SaleDate'].min()


# In[25]:


# Check max date value after change
OwnershipHistory_df['SaleDate'].max()


# In[26]:


# Calculate the quartiles
Q1 = VehicleCondition_df.quantile(0.25)
Q3 = VehicleCondition_df.quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = ((VehicleCondition_df < lower_bound) | (VehicleCondition_df > upper_bound)).any(axis=1)

# Display the outliers
print(VehicleCondition_df[outliers])


# In[27]:


## ^ no outliers


# In[28]:


# Now for the rest of the dataframes, I create individual functions for detecting the outliers using interquartile range


# In[29]:


def detect_outliers_iqr(df, feature_col):
    Q1 = df[feature_col].quantile(0.25)
    Q3 = df[feature_col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((df[feature_col] < lower_bound) | (df[feature_col] > upper_bound)).any()
    return outliers

outliers_mask = detect_outliers_iqr(Features_df, 'FeatureID')

# Check if any outliers are detected
if outliers_mask.any():
    # Filter the DataFrame to select only the rows that are outliers
    outliers_df = Features_df[outliers_mask]

    # Print the DataFrame containing outliers
    print(outliers_df)
else:
    print("No outliers detected.")


# In[30]:


# Function to detect outliers using Interquartile Range (IQR)
def detect_outliers_iqr(df, feature_col):
    Q1 = df[feature_col].quantile(0.25)
    Q3 = df[feature_col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_mask = (df[feature_col] < lower_bound) | (df[feature_col] > upper_bound)
    return outliers_mask

# Detect outliers in Cost column
outliers_mask = detect_outliers_iqr(Incidents_df, 'Cost')

# Filter the DataFrame to select only the rows that are outliers
outliers_df = Incidents_df[outliers_mask]

# Print the DataFrame containing outliers
print(outliers_df)


# In[31]:


## ^ no outliers


# In[32]:


# Function to detect outliers using Interquartile Range (IQR)
def detect_outliers_iqr(df, feature_col):
    Q1 = df[feature_col].quantile(0.25)
    Q3 = df[feature_col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_mask = (df[feature_col] < lower_bound) | (df[feature_col] > upper_bound)
    return outliers_mask

# Detect outliers in Cost column
outliers_mask = detect_outliers_iqr(ServiceHistory_df, 'Cost')

# Filter the DataFrame to select only the rows that are outliers
outliers_df = ServiceHistory_df[outliers_mask]

# Print the DataFrame containing outliers
print(outliers_df)


# In[33]:


## ^ no outliers


# In[34]:


# Function to detect outliers using Interquartile Range (IQR)
def detect_outliers_iqr(df, feature_col):
    Q1 = df[feature_col].quantile(0.25)
    Q3 = df[feature_col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_mask = (df[feature_col] < lower_bound) | (df[feature_col] > upper_bound)
    return outliers_mask

# Detect outliers in AverageSalePrice column
outliers_mask = detect_outliers_iqr(MarketTrends_df, 'AverageSalePrice')

# Filter the DataFrame to select only the rows that are outliers
outliers_df = MarketTrends_df[outliers_mask]

# Print the DataFrame containing outliers
print(outliers_df)


# In[35]:


## ^ no outliers


# My next task is to standardize my data formats 

# In[37]:


# 5. Standardize data formats
#   A. Cars table
# ---------------------------------------------------------------------------------------------------------------------------

# For my Cars_df; Convert 'Make', 'Model' to lowercase

Cars_df['Make'] = Cars_df['Make'].str.lower()
Cars_df['Model'] = Cars_df['Model'].str.lower()


# In[38]:


# 5. Standardize data formats
#   B. Owners table
# ---------------------------------------------------------------------------------------------------------------------------

# Owners_df is already standardized


# In[39]:


# 5. Standardize data formats
#   C. OwnershipHistory Table
# ---------------------------------------------------------------------------------------------------------------------------

# For OwnershipHistory_df, I will standardize the date columns

OwnershipHistory_df['PurchaseDate'] = pd.to_datetime(OwnershipHistory_df['PurchaseDate'])
OwnershipHistory_df['SaleDate'] = pd.to_datetime(OwnershipHistory_df['SaleDate'])


# In[40]:


# 5. Standardize data formats
#   D. VehicleCondition Table
# ---------------------------------------------------------------------------------------------------------------------------

# VehicleCondition_df is already standardized


# In[41]:


# 5. Standardize data formats
#   E. Features Table
# ---------------------------------------------------------------------------------------------------------------------------

# Features_df is already standardized


# In[42]:


# 5. Standardize data formats
#   F. Incidents Table
# ---------------------------------------------------------------------------------------------------------------------------

# For my Incidents_df; Convert 'description' to lowercase and also standardize the IncidentDate

Incidents_df['Description'] = Incidents_df['Description'].str.lower()
Incidents_df['IncidentDate'] = pd.to_datetime(Incidents_df['IncidentDate'])


# In[43]:


# 5. Standardize data formats
#   G. ServiceHistory Table
# ---------------------------------------------------------------------------------------------------------------------------

# For ServiceHistoruy data I am going to standardize the data column

ServiceHistory_df['ServiceDate'] = pd.to_datetime(ServiceHistory_df['ServiceDate'])


# In[44]:


# 5. Standardize data formats
#   H. MarketTrends Table
# ---------------------------------------------------------------------------------------------------------------------------

# For MarketTrends data I am going to standardize the data column

MarketTrends_df['Date'] = pd.to_datetime(MarketTrends_df['Date'])


# Now I have handled mising values, outliers, and standardized my data formats.
# I am ready to re-insert my data into my database and can start in a new notebook for the analysis and visualization

# In[46]:


# 6. Saving cleaned datasets
# ---------------------------------------------------------------------------------------------------------------------------

Cars_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Cars_df.csv', index=False)
Owners_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Owners_df.csv', index=False)
OwnershipHistory_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\OwnershipHistory_df.csv', index=False)
VehicleCondition_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\VehicleCondition_df.csv', index=False)
Features_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Features_df.csv', index=False)
Incidents_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Incidents_df.csv', index=False)
ServiceHistory_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\ServiceHistory_df.csv', index=False)
MarketTrends_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\MarketTrends_df.csv', index=False)


# ### **Now in a new notebook I will re-read the CSVs into python dataframes. 
# ### **(Somewhat redundant but allows me to preserve original data)

# # ----------------------------------- END Python Script -----------------------------------------------

# In[ ]:




