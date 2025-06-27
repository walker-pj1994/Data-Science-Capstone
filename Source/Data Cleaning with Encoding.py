#!/usr/bin/env python
# coding: utf-8

# ### Note: I did not end up using the encoded variables or features that I engineered myself and so the Original 'Data Cleaning.py' file is the version I ran and used for further analysis. I am including this script in addition in order to showcase that I have the knowledge required for encoding categorical variables and engineering custom features. 
# ### -------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#    6. Encoding Categorical Variables: Encodes categorical variables using label encoding and one-hot encoding.
#    
#    
#    7. Feature Engineering: 
#        - Calculates new features such as car age, luxury brand indicator, mileage per year, length of ownership, etc.
#        
#        
#    8. Saving Cleaned Datasets: Saves cleaned DataFrames to CSV files.
#    
#     
# Overall, this code prepares the data for further analysis and visualization by handling missing values, outliers, standardizing formats, encoding categorical variables, and engineering new features. Finally, it saves the cleaned datasets for future use.
# 
# For the code for each of the above components, I will re-iterate with in-line comments what is mentioned above to identify what code corresponds to which component from above. Also to keep the context consistent.

# # ----------------------------------- Start Python Script -----------------------------------------------

# In[1]:


# 1. Importing Necessary Libraries
# ---------------------------------------------------------------------------------------------------------------------------

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from datetime import datetime


# The following 58 lines of code pertain to the cleaning of my datasets. By cleaning I am referring to the handling of 
# missing values, addressing outliers, standardizing my data formats, encoding my categorical variables, and engineering
# new features to ensure I have final 'clean' datasets for further analysis and visualization. 
# 
# First we will tackle any missing values.

# In[3]:


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


Owners_df


# In[5]:


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


# In[6]:


Cars_missing_values


# In[7]:


Owners_missing_values


# In[8]:


OwnershipHistory_missing_values


# In[9]:


VehicleCondition_missing_values


# In[10]:


Features_missing_values


# In[11]:


Incidents_missing_values


# In[12]:


ServiceHistory_missing_values


# In[13]:


MarketTrends_missing_values


# In[14]:


# Based on initial findings above, it appears as though I luckily do not have to deal with any missing values - which
# does make sense based on the simple fact that I generated the data myself and made sure every datapoint was populated
# in each of my tables.


# In[15]:


# There are some points of interest (dataframe columns) that I would like to examine for outliers however. 


# In[16]:


# 4. Outlier Detection and Handling
# ---------------------------------------------------------------------------------------------------------------------------

# Visualize distribution of 'Mileage' using a box plot
plt.boxplot(Cars_df['Mileage'])
plt.xlabel('Mileage')
plt.title('Box Plot of Mileage')
plt.show()


# In[17]:


Cars_df.describe()


# In[18]:


# Filtering outliers from the 'Mileage' column

mileage_threshold = Cars_df['Mileage'].quantile(0.99)
Cars_df = Cars_df[Cars_df['Mileage'] <= mileage_threshold]


# In[19]:


Cars_df.describe()


# In[20]:


# For my ownershiphistory data I am not interested in data for records before the year 2020 or after the year 2023.   


# In[21]:


# Check min date value
OwnershipHistory_df['SaleDate'].min()


# In[22]:


# Check max date value
OwnershipHistory_df['SaleDate'].max()


# In[23]:


# Create custom start and end date variables

start_date = pd.to_datetime('2020-01-01')
end_date = pd.to_datetime('2024-01-01')


# In[24]:


# Filtering data based on specified date ranges

OwnershipHistory_df = OwnershipHistory_df[(OwnershipHistory_df['PurchaseDate'] >= start_date) & (OwnershipHistory_df['PurchaseDate'] <= end_date)]
OwnershipHistory_df = OwnershipHistory_df[(OwnershipHistory_df['SaleDate'] >= start_date) & (OwnershipHistory_df['SaleDate'] <= end_date)]


# In[25]:


# Check min date value after change

OwnershipHistory_df['SaleDate'].min()


# In[26]:


# Check max date value after change

OwnershipHistory_df['SaleDate'].max()


# In[27]:


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


# In[28]:


## ^ no outliers


# In[29]:


# Now for the rest of the dataframes, I create individual functions for detecting the outliers using interquartile range


# In[30]:


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


# In[31]:


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


# In[32]:


## ^ no outliers


# In[33]:


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


# In[34]:


## ^ no outliers


# In[35]:


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


# In[36]:


## ^ no outliers


# My next task is to standardize my data formats 

# In[38]:


# 5. Standardize data formats
#   A. Cars table
# ---------------------------------------------------------------------------------------------------------------------------

# For my Cars_df; Convert 'Make', 'Model' to lowercase

Cars_df['Make'] = Cars_df['Make'].str.lower()
Cars_df['Model'] = Cars_df['Model'].str.lower()


# In[39]:


# 5. Standardize data formats
#   B. Owners table
# ---------------------------------------------------------------------------------------------------------------------------

# Owners_df is already standardized


# In[40]:


# 5. Standardize data formats
#   C. OwnershipHistory Table
# ---------------------------------------------------------------------------------------------------------------------------

# For OwnershipHistory_df, I will standardize the date columns

OwnershipHistory_df['PurchaseDate'] = pd.to_datetime(OwnershipHistory_df['PurchaseDate'])
OwnershipHistory_df['SaleDate'] = pd.to_datetime(OwnershipHistory_df['SaleDate'])


# In[41]:


# 5. Standardize data formats
#   D. VehicleCondition Table
# ---------------------------------------------------------------------------------------------------------------------------

# VehicleCondition_df is already standardized


# In[42]:


# 5. Standardize data formats
#   E. Features Table
# ---------------------------------------------------------------------------------------------------------------------------

# Features_df is already standardized


# In[43]:


# 5. Standardize data formats
#   F. Incidents Table
# ---------------------------------------------------------------------------------------------------------------------------

# For my Incidents_df; Convert 'description' to lowercase and also standardize the IncidentDate

Incidents_df['Description'] = Incidents_df['Description'].str.lower()
Incidents_df['IncidentDate'] = pd.to_datetime(Incidents_df['IncidentDate'])


# In[44]:


# 5. Standardize data formats
#   G. ServiceHistory Table
# ---------------------------------------------------------------------------------------------------------------------------

# For ServiceHistoruy data I am going to standardize the data column

ServiceHistory_df['ServiceDate'] = pd.to_datetime(ServiceHistory_df['ServiceDate'])


# In[45]:


# 5. Standardize data formats
#   H. MarketTrends Table
# ---------------------------------------------------------------------------------------------------------------------------

# For MarketTrends data I am going to standardize the data column

MarketTrends_df['Date'] = pd.to_datetime(MarketTrends_df['Date'])


# Now for encoding my categorical variables.

# In[47]:


# 6. Encoding Categorical Variables
#   A. Cars table
# ---------------------------------------------------------------------------------------------------------------------------

# In Cars table;
# 1. EngineType - values: ('2-Cylinder', '3-Cylinder', '4-Cylinder', '5-Cylinder', '6-Cylinder', '8-Cylinder','10-Cylinder+')
# 2. TransmissionType - values: ('Automatic', 'Manual', 'CVT')
# 3. FuelType - values: ('Gasoline', 'Diesel', 'Hybrid', 'Electric')

# Label Encoding for 'EngineType' in Cars_df
label_encoder = LabelEncoder()
Cars_df['EngineType_encoded'] = label_encoder.fit_transform(Cars_df['EngineType'])

# One-Hot Encoding for'TransmissionType' in Cars_df
Cars_df = pd.get_dummies(Cars_df, columns=['TransmissionType'], drop_first=True)

# One-Hot Encoding for 'FuelType' in Cars_df
Cars_df = pd.get_dummies(Cars_df, columns=['FuelType'], drop_first=True)
Cars_df


# In[48]:


# 6. Encoding Categorical Variables
#   B. VehicleCondition table
# ---------------------------------------------------------------------------------------------------------------------------

# In VehicleCondition table;
# 1. OverallCondition - values: ('Excellent', 'Good', 'Fair', 'Poor')
# 2. ExteriorCondition - values: ('Clean', 'Minor Scratches', 'Dents', 'Needs Repairs')
# 3. InteriorCondition - values: ('Clean', 'Minor Wear', 'Torn Upholstery', 'Needs Cleaning')

# Label Encoding for various conditions in VehicleHistory_df
VehicleCondition_df['OverallCondition_encoded'] = label_encoder.fit_transform(VehicleCondition_df['OverallCondition'])
VehicleCondition_df['ExteriorCondition_encoded'] = label_encoder.fit_transform(VehicleCondition_df['ExteriorCondition'])
VehicleCondition_df['InteriorCondition_encoded'] = label_encoder.fit_transform(VehicleCondition_df['InteriorCondition'])
VehicleCondition_df


# In[49]:


# 6. Encoding Categorical Variables
#   C. Features table
# ---------------------------------------------------------------------------------------------------------------------------

# In Features table;
# 1. FeatureName - values: ('Air Conditioning', 'Power Windows', 'ABS', 'Cruise Control', 'Bluetooth', 'Backup Camera')

# Label Encoding feature name in Features_df
Features_df['FeatureName_encoded'] = label_encoder.fit_transform(Features_df['FeatureName'])
Features_df


# In[50]:


# 6. Encoding Categorical Variables
#   D. ServiceHistory table
# ---------------------------------------------------------------------------------------------------------------------------

# In ServiceHistory table;
# 1. ServiceType - values: ('Oil Change', 'Brake Inspection', 'Tire Rotation', 'Engine Tune-up')

# Label Encoding for ServiceType in ServiceHistory_df
ServiceHistory_df['ServiceType_encoded'] = label_encoder.fit_transform(ServiceHistory_df['ServiceType'])
ServiceHistory_df


# Now for engineering new features.

# In[52]:


# 7. Feature Engineering
#   A. Cars Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the age of the car based on the current year and the 'Year' column.
current_year = datetime.now().year
Cars_df['Age'] = current_year - Cars_df['Year']


# Create a binary feature indicating whether the car is a luxury brand or not based on the 'Make' column.
luxury_brands = ['Mercedes', 'BMW', 'Audi', 'Lexus', 'Porsche', 'Jaguar', 'Infiniti', 'Acura', 'Cadillac', 'Lincoln']
Cars_df['IsLuxury'] = Cars_df['Make'].apply(lambda x: 1 if any(brand in x for brand in luxury_brands) else 0)


# Calculate the mileage per year for each car.
Cars_df['MileagePerYear'] = Cars_df['Mileage'] / Cars_df['Age']

Cars_df.head()


# In[53]:


# 7. Feature Engineering
#   B. Owners Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the length of ownership for each owner by subtracting PurchaseDate from SaleDate
Owners_df['LengthOfOwnership'] = (OwnershipHistory_df['SaleDate'] - OwnershipHistory_df['PurchaseDate']).dt.days

# Determine the number of cars each owner has owned
car_counts = OwnershipHistory_df['OwnerID'].value_counts().rename('NumCarsOwned')
Owners_df = Owners_df.merge(car_counts, left_on='OwnerID', right_index=True, how='left')

# Encode the contact information to identify patterns such as phone number format or email domain
# For simplicity, let's just check if the contact info contains an email address or phone number
Owners_df['HasEmail'] = Owners_df['ContactInfo'].str.contains('@').astype(int)
Owners_df['HasPhoneNumber'] = Owners_df['ContactInfo'].str.contains(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b').astype(int)

Owners_df.head()


# In[54]:


# 7. Feature Engineering
#   C. OwnershipHistory Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the duration of ownership for each entry
OwnershipHistory_df['OwnershipDuration'] = (OwnershipHistory_df['SaleDate'] - OwnershipHistory_df['PurchaseDate']).dt.days

# Calculate the percentage change in sale price for each transaction
OwnershipHistory_df['SalePriceChange'] = OwnershipHistory_df.groupby('CarID')['SalePrice'].pct_change()

# Fill NaN values resulting from the pct_change operation with 0, as the first transaction won't have a previous value to compare to
OwnershipHistory_df['SalePriceChange'].fillna(0, inplace=True)

OwnershipHistory_df.head()


# In[55]:


# 7. Feature Engineering
#   D. VehicleCondition Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Define a mapping of condition metrics to scores
condition_mapping = {
    'Excellent': 5,
    'Good': 4,
    'Fair': 3,
    'Poor': 2,
    'Very Poor': 1
}

# Calculate an overall condition score based on the given condition metrics
def calculate_overall_condition(row):
    overall_condition_score = 0
    condition_metrics = [row['OverallCondition'], row['ExteriorCondition'], row['InteriorCondition']]
    for condition in condition_metrics:
        overall_condition_score += condition_mapping.get(condition, 0)
    return overall_condition_score / len(condition_metrics)

VehicleCondition_df['OverallConditionScore'] = VehicleCondition_df.apply(calculate_overall_condition, axis=1)

VehicleCondition_df.head()


# In[56]:


# 7. Feature Engineering
#   E. Features Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the number of features for each car
num_features_per_car = Features_df.groupby('CarID').size().rename('NumFeatures')

# Merge the calculated number of features with the main DataFrame
Features_df = Features_df.merge(num_features_per_car, left_on='CarID', right_index=True, how='left')

Features_df.head()


# In[57]:


# 7. Feature Engineering
#   F. Incidents Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the average cost per incident
average_cost_per_incident = Incidents_df.groupby('CarID')['Cost'].mean().rename('AvgCostPerIncident')

# Merge the calculated average cost per incident with the main DataFrame
Incidents_df = Incidents_df.merge(average_cost_per_incident, left_on='CarID', right_index=True, how='left')

Incidents_df.head()


# In[58]:


# 7. Feature Engineering
#   G. ServiceHistory Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Calculate the frequency of services per car
service_frequency_per_car = ServiceHistory_df.groupby('CarID').size().rename('ServiceFrequency')

# Calculate the total cost of services per car
total_cost_of_services_per_car = ServiceHistory_df.groupby('CarID')['Cost'].sum().rename('TotalCostOfServices')

# Merge the calculated features with the main DataFrame
ServiceHistory_df = ServiceHistory_df.merge(service_frequency_per_car, left_on='CarID', right_index=True, how='left')
ServiceHistory_df = ServiceHistory_df.merge(total_cost_of_services_per_car, left_on='CarID', right_index=True, how='left')

ServiceHistory_df.head()


# In[59]:


# 7. Feature Engineering
#   H. MarketTrends Table:
# ---------------------------------------------------------------------------------------------------------------------------

# Sort the DataFrame by CarID and Date
MarketTrends_df.sort_values(by=['CarID', 'Date'], inplace=True)

# Calculate the percentage change in average sale price compared to the previous period
MarketTrends_df['AvgSalePriceChange'] = MarketTrends_df.groupby('CarID')['AverageSalePrice'].pct_change()

# Create a feature indicating whether the market demand is increasing or decreasing
MarketTrends_df['DemandChange'] = pd.cut(MarketTrends_df['MarketDemand'].diff(), bins=[float('-inf'), 0, float('inf')], labels=['Decreasing', 'Increasing'])

MarketTrends_df.head()


# Now I have handled, mising values, outliers, standardized my data formats, encoded my categorical variables, and engineered
# new features. I am ready to re-insert my data into my database and can start in a new notebook for the
# analysis and visualization.

# In[61]:


# 8. Saving cleaned datasets
# ---------------------------------------------------------------------------------------------------------------------------

# Cars_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Cars_dfV2.csv', index=False)
# Owners_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Owners_dfV2.csv', index=False)
# OwnershipHistory_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\OwnershipHistory_dfV2.csv', index=False)
# VehicleCondition_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\VehicleCondition_dfV2.csv', index=False)
# Features_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Features_dfV2.csv', index=False)
# Incidents_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\Incidents_dfV2.csv', index=False)
# ServiceHistory_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\ServiceHistory_dfV2.csv', index=False)
# MarketTrends_df.to_csv(r'P:\Users\paulj\Desktop\Important Documentation\Education\Eastern University\DTSC 691 - Capstone II\Clean Datasets\MarketTrends_dfV2.csv', index=False)


# ### **As mentioned at beginning of file, I am not utilizing these versions of my cleaned datasets and so that is why all of the ".to_csv()" functions have been commented out.

# In[ ]:





# In[ ]:




