#!/usr/bin/env python
# coding: utf-8

# <h1 style="text-align: center;">DTSC 691 - Database Project</h1>
# <h1 style="text-align: center;">Paul J. Walker</h1>
# <hr style="border:2px solid green">

# <hr style="border:2px solid black">
# <h3 style="text-align: center;">Summary of File</h3>
# 
# This Python notebook comprises a comprehensive suite of scripts aimed at database manipulation and data cleaning for automotive industry analysis. Initially, I introduce a script for populating a MySQL database named dtsc_vehicles with synthetic data pertinent to various automotive industry aspects. Following this, I transition into a data cleaning phase; focusing on preprocessing tasks across multiple data frames related to automotive data. These tasks encompass handling missing values, outlier detection and handling, standardizing data formats, encoding categorical variables, and engineering new features. Lastly, it prepares the cleaned datasets for further analysis and visualization by saving them for future use. In addition, commentary outlining these analyses and visualizations as they are generated. This notebook serves as a foundational tool for database testing, development, educational purposes, and advanced data analysis in the automotive domain.
# <hr style="border:2px solid black">

# ****Blue lines separate individual Python scripts.**

# <hr style="border:2px solid blue">
# 
#    ### Begin Database Data Insertion Script
# 
# <hr style="border:2px solid blue">

# ## Python Script Overview
# 
# This Python script is designed to populate a MySQL database named dtsc_vehicles with synthetic data related to various aspects of the automotive industry. Let's break down the key components and functionalities of this script:
# 
#    1. **Importing Necessary Libraries:** The script begins by importing the required libraries: Faker for generating fake data, VehicleProvider from faker_vehicle to provide vehicle-related data, random for generating random numbers, and mysql.connector for connecting to the MySQL database.
#    
#    
#    2. **Seeding Randomness:** The script seeds the random number generator for reproducibility. This ensures that each time the script is run with the same seed, it produces the same sequence of random numbers.
#    
#    
#    3. **Data Generation Functions:** Several functions are defined to generate fake data for different tables in the database. Each function follows a similar structure where it uses the Faker library to create realistic data for specific attributes of the tables. Functions like generate_cars_data, generate_owners_data, generate_ownership_history_data, generate_vehicle_condition_data, generate_features_data, generate_incidents_data, generate_service_history_data, and generate_market_trends_data are defined for generating data for respective tables like Cars, Owners, OwnershipHistory, VehicleCondition, Features, Incidents, ServiceHistory, and MarketTrends.
#    
#     
#    4. **Database Connection:** The script establishes a connection to the MySQL database named dtsc_vehicles. It provides the host, username, password, and database name for establishing the connection.
#    
#     
#    5. **Data Insertion:** For each table, the script generates fake data using the corresponding data generation function. It then constructs an SQL INSERT query to insert the generated data into the respective table. The executemany() method is used to execute the INSERT query for bulk insertion of data. After insertion, the changes are committed to the database using conn.commit().
#    
#     
#    6. **Error Handling:** Exception handling is implemented to catch any errors that may occur during data insertion. If an error occurs, it prints an error message indicating the nature of the error. Regardless of whether an error occurs or not, the script ensures that the database connection is properly closed after data insertion.
#    
#     
#    7. **Closing Database Connection:** After completing data insertion for each table, the script closes the cursor and the database connection using cursor.close() and conn.close() respectively.
#    
#     
# Overall, this script automates the process of populating a MySQL database with synthetic data, facilitating database testing, development, or educational purposes related to the automotive domain.
# 
# For the code for each of the above components, I will re-iterate what is mentioned above to identify what code corresponds to which component from above. Also to keep the context consistent.

# # ----------------------------------- Start Python Script -----------------------------------------------

# In[1]:


# 1. Importing Necessary Libraries
# ---------------------------------------------------------------------------------------------------------------------------
from faker import Faker
from faker_vehicle import VehicleProvider
import random
import mysql.connector


# 2. Seeding Randomness and Faker maintenance
# ---------------------------------------------------------------------------------------------------------------------------
fake = Faker()
fake.add_provider(VehicleProvider)
Faker.seed(0)
random.seed(0)


# In[2]:


# 3. Data generating functions utilizing the Faker object. 
#   A. Cars_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_cars_data(num_records):
    fake = Faker()
    fake.add_provider(VehicleProvider)
    data = []
    for car_id in range(1, num_records + 1):
        make = fake.vehicle_make()
        model = fake.vehicle_model()
        year = fake.vehicle_year()
        mileage = random.randint(0, 200000)
        vin = fake.vin()
        engine_type = fake.random_element(elements=('2-Cylinder', '3-Cylinder', '4-Cylinder', '5-Cylinder', '6-Cylinder', '8-Cylinder','10-Cylinder+'))
        transmission_type = fake.random_element(elements=('Automatic', 'Manual', 'CVT'))
        fuel_type = fake.random_element(elements=('Gasoline', 'Diesel', 'Hybrid', 'Electric'))
        data.append((car_id, make, model, year, mileage, vin, engine_type, transmission_type, fuel_type))
    return data


# In[3]:


# 3. Data generating functions utilizing the Faker object. 
#   B. Owners_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_owners_data(num_records):
    fake = Faker()
    data = []
    for owner_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 2000 cars in the Cars table
        first_name = fake.first_name()
        last_name = fake.last_name()
        contact_info = fake.email()
        state = fake.state_abbr()
        data.append((owner_id, car_id, first_name, last_name, contact_info, state))
    return data


# In[4]:


# 3. Data generating functions utilizing the Faker object. 
#   C. OwnershipHistory_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_ownership_history_data(num_records):
    fake = Faker()
    data = []
    for ownership_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 2000 cars in the Cars table
        owner_id = random.randint(1, 3000)  # Assuming 3000 owners in the Owners table
        purchase_date = fake.date_between(start_date='-5y', end_date='today')
        sale_date = fake.date_between(start_date=purchase_date, end_date='today')
        sale_price = round(random.uniform(5000, 50000), 2)
        data.append((ownership_id, car_id, owner_id, purchase_date, sale_date, sale_price))
    return data


# In[5]:


# 3. Data generating functions utilizing the Faker object. 
#   D. VehicleCondition_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_vehicle_condition_data(num_records):
    fake = Faker()
    data = []
    for condition_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 2000 cars in the Cars table
        overall_condition = fake.random_element(elements=('Excellent', 'Good', 'Fair', 'Poor'))
        exterior_condition = fake.random_element(elements=('Clean', 'Minor Scratches', 'Dents', 'Needs Repairs'))
        interior_condition = fake.random_element(elements=('Clean', 'Minor Wear', 'Torn Upholstery', 'Needs Cleaning'))
        data.append((condition_id, car_id, overall_condition, exterior_condition, interior_condition))
    return data


# In[6]:


# 3. Data generating functions utilizing the Faker object. 
#   E. Features_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_features_data(num_records):
    fake = Faker()
    data = []
    features_list = ['Air Conditioning', 'Power Windows', 'ABS', 'Cruise Control', 'Bluetooth', 'Backup Camera']
    for feature_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 2000 cars in the Cars table
        feature_name = fake.random_element(elements=features_list)
        feature_value = fake.random_element(elements=('Yes', 'No'))
        data.append((feature_id, car_id, feature_name, feature_value))
    return data


# In[7]:


# 3. Data generating functions utilizing the Faker object. 
#   F. Incidents_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_incidents_data(num_records):
    fake = Faker()
    data = []
    for incident_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 2000 cars in the Cars table
        incident_date = fake.date_between(start_date='-1y', end_date='today')
        description = fake.random_element(elements=('Driving under the influence', 'Distracted driving', 'Head-on collision', 'Speeding', 'Rear-end collision', 'Drowsy driving', 'Rollover', 'Aggressive driving', 'Side-impact collision', 'Improper turns', 'Pedestrian accident', 'Sideswipe collision'))
        cost = round(random.uniform(5000, 15000), 2)
        data.append((incident_id, car_id, incident_date, description, cost))
    return data


# In[8]:


# 3. Data generating functions utilizing the Faker object. 
#   G. ServiceHistory_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_service_history_data(num_records):
    fake = Faker()
    data = []
    service_types = ['Oil Change', 'Brake Inspection', 'Tire Rotation', 'Engine Tune-up']
    for service_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 1000 cars in the Cars table
        service_date = fake.date_between(start_date='-3y', end_date='today')
        service_type = fake.random_element(elements=service_types)
        cost = round(random.uniform(50, 1500), 2)
        data.append((service_id, car_id, service_date, service_type, cost))
    return data


# In[9]:


# 3. Data generating functions utilizing the Faker object. 
#   H. MarketTrends_data
# ---------------------------------------------------------------------------------------------------------------------------

def generate_market_trends_data(num_records):
    fake = Faker()
    data = []
    for trend_id in range(1, num_records + 1):
        car_id = random.randint(1, 2000)  # Assuming 1000 cars in the Cars table
        date = fake.date_between(start_date='-8y', end_date='today')
        average_sale_price = round(random.uniform(10000, 40000), 2)
        market_demand = random.randint(10, 100)
        data.append((trend_id, car_id, date, average_sale_price, market_demand))
    return data


# In[10]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  A. Cars Table - 3,000 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    cars_data = generate_cars_data(2000)
    insert_query = "INSERT INTO Cars (CarID, Make, Model, Year, Mileage, VIN, EngineType, TransmissionType, FuelType) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Inserting data for Cars table using executemany()
    cursor.executemany(insert_query, cars_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[11]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  B. Owners Table - 3,000 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    owners_data = generate_owners_data(3000)
    insert_query = "INSERT INTO Owners (OwnerId, CarID, FirstName, LastName, ContactInfo, State) VALUES (%s, %s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, owners_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[12]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------
conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  C. OwnershipHistory Table - 3,000 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    ownership_history_data = generate_ownership_history_data(3000)
    insert_query = "INSERT INTO OwnershipHistory (OwnershipID, CarID, OwnerID, PurchaseDate, SaleDate, SalePrice) VALUES (%s, %s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, ownership_history_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[13]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  D. VehicleCondition Table - 2,000 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    vehicle_condition_data = generate_vehicle_condition_data(2000)
    insert_query = "INSERT INTO VehicleCondition (ConditionID, CarID, OverallCondition, ExteriorCondition, InteriorCondition) VALUES (%s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, vehicle_condition_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[14]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  E. Features Table - 10,000 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    feature_data = generate_features_data(10000)
    insert_query = "INSERT INTO Features (FeatureID, CarID, FeatureName, FeatureValue) VALUES (%s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, feature_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[15]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  F. Incidents Table - 1,500 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    incidents_data = generate_incidents_data(1500)
    insert_query = "INSERT INTO Incidents (IncidentID, CarID, IncidentDate, Description, Cost) VALUES (%s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, incidents_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[16]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  G. ServiceHistory Table - 4,500 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    service_history_data = generate_service_history_data(4500)
    insert_query = "INSERT INTO ServiceHistory (ServiceID, CarID, ServiceDate, ServiceType, Cost) VALUES (%s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, service_history_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# In[17]:


# 4. Using mysql.connector object to establish a connection to my SQL database 'dtsc691vehicles'
# ---------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)


# 5. Generating fake data and inserting into respective tables. 
#  H. MarketTrends Table - 4,500 records generaeted to be inserted

# 6. In order to handle errors during insertion I use 
    # try: 
    # except: 
    # finally:
# to indicate either that the data inserted correctly or it encountered errors when attempting to insert.

# 7. Closing Database Connection
# ---------------------------------------------------------------------------------------------------------------------------

cursor = conn.cursor()
try:
    market_trends_data = generate_market_trends_data(2000)
    insert_query = "INSERT INTO MarketTrends (TrendID, CarID, Date, AverageSalePrice, MarketDemand) VALUES (%s, %s, %s, %s, %s)"

    # Inserting data for Owners table using executemany()
    cursor.executemany(insert_query, market_trends_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()


# ### **All of my data was inserted successfully into my SQL database.

# # ----------------------------------- END Python Script -----------------------------------------------

# <hr style="border:2px solid blue">

# <hr style="border:2px solid blue">
# 
#    ### Begin Data Cleaning Script
# 
# <hr style="border:2px solid blue">

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

## import mysql.connector ## already imported
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

# <hr style="border:2px solid blue">
# 
#    ### Begin Data Cleaning With Encoding Script
# 
# <hr style="border:2px solid blue">

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

#import mysql.connector #already imported
#import pandas as pd #already imported
#import matplotlib.pyplot as plt #already imported

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

# # ----------------------------------- END Python Script -----------------------------------------------

# <hr style="border:2px solid blue">
# 
#    ### Begin Data Analysis Script
# 
# <hr style="border:2px solid blue">

# ## Python Script Overview
# 
# The provided Python code conducts a comprehensive data analysis on several datasets related to vehicle information. Here's a summary and commentary on each section:
# 
#    1. Importing Libraries: Imports necessary libraries such as pandas and numpy, matplotlib.pyplot, and various statistical models from scipy.
#    
#    
#    2. Data Loading:
#        - Dataframes for various datasets like Cars, Owners, Ownership History, etc., are loaded from CSV files into Pandas DataFrames.
#    
#    
#    3. Data Summary:
#        - The .head() method is used to display the first few rows of each DataFrame for initial inspection.
#        - The .describe() method is applied to each DataFrame to get summary statistics like count, mean, std, min, max, etc.
#    
#    
#    4. Correlation Analysis:
#        - Pearson correlation coefficients are calculated for each pair of variables in each DataFrame using the .corr() method.
#        - Correlation matrices are printed for each DataFrame to understand the relationships between variables.
#    
#     
#    5. Hypothesis Testing:
#        - Several hypothesis tests are conducted to analyze different aspects of the data.
#            - For example, the effect of mileage on sale price is tested using Pearson correlation and linear regression.
#        - ANOVA tests are performed to analyze differences in average sale price based on car make, vehicle condition, and fuel type.
#        - Chi-square test of independence and logistic regression are used to examine the association between incidents and market demand.
#        - Time-series analysis is conducted to identify trends in average sale price over time.
#    
#     
#    6. Data Manipulation:
#        - Dataframes are merged, cleaned, and processed as needed for hypothesis testing and analysis.
#            - For instance, missing values are handled, and new columns like 'Age' and 'MPY' (Miles Per Year) are calculated.
#    
#     
#    7. Data Visualization:
#        - Matplotlib is used to visualize data trends and relationships, such as plotting average sale price over time.
#    
#     
# Overall, the code provides a thorough exploration of the datasets, conducts various statistical analyses, and generates visualizations to gain insights into different aspects of the vehicle data.
# 
# For the code for each of the above components, I will re-iterate with in-line comments what is mentioned above to identify what code corresponds to which component from above. Also to keep the context consistent.

# # ----------------------------------- Start Python Script -----------------------------------------------

# In[1]:


# 1. Importing Necessary Libraries
# ---------------------------------------------------------------------------------------------------------------------------

# import pandas as pd #already imported
import numpy as np

import statsmodels.api as sm
#import matplotlib.pyplot as plt #already imported

from scipy.stats import chi2_contingency
from scipy.stats import f_oneway
from scipy.stats import pearsonr


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


# 3. Data summaries 1
#   A. Cars_df
# ---------------------------------------------------------------------------------------------------------------------------

Cars_df.head(5)


# In[4]:


# 3. Data summaries 1
#   B. Owners_df
# ---------------------------------------------------------------------------------------------------------------------------

Owners_df.head(5)


# In[5]:


# 3. Data summaries 1
#   C. OwnershipHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

OwnershipHistory_df.head(5)


# In[6]:


# 3. Data summaries 1
#   D. VehicleCondition_df
# ---------------------------------------------------------------------------------------------------------------------------

VehicleCondition_df.head(5)


# In[7]:


# 3. Data summaries 1
#   E. Features_df
# ---------------------------------------------------------------------------------------------------------------------------

Features_df.head(5)


# In[8]:


# 3. Data summaries 1
#   F. Incidents_df
# ---------------------------------------------------------------------------------------------------------------------------

Incidents_df.head(5)


# In[9]:


# 3. Data summaries 1
#   G. ServiceHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

ServiceHistory_df.head(5)


# In[10]:


# 3. Data summaries 1
#   H. MarketTrends_df
# ---------------------------------------------------------------------------------------------------------------------------

MarketTrends_df.head(5)


# In[11]:


# 3. Data summaries 2
#   A. Cars_df
# ---------------------------------------------------------------------------------------------------------------------------

summary_stats = Cars_df.describe()
print(summary_stats)


# In[12]:


# 3. Data summaries 2
#   B. OwnershipHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

summary_stats = OwnershipHistory_df.describe()
print(summary_stats)


# In[13]:


# 3. Data summaries 2
#   C. Incidents_df
# ---------------------------------------------------------------------------------------------------------------------------

summary_stats = Incidents_df.describe()
print(summary_stats)


# In[14]:


# 3. Data summaries 2
#   D. ServiceHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

summary_stats = ServiceHistory_df.describe()
print(summary_stats)


# In[15]:


# 4. Pearson Correlation Coefficient
#   A. Cars_df
# ---------------------------------------------------------------------------------------------------------------------------

Cars_corr = Cars_df.corr(method = 'pearson')
print(Cars_corr)


# 1. CarID and Year: There is a very weak negative correlation (-0.018717), suggesting that there is virtually no linear relationship between the car's ID and the year it was made.
# 
# 2. CarID and Mileage: There is a very weak negative correlation (-0.030113), suggesting that there is virtually no linear relationship between the car's ID and its mileage.
# 
# 3. Year and Mileage: There is a very weak negative correlation (-0.010199), indicating that there is virtually no linear relationship between the year the car was made and its mileage.

# In[16]:


# 4. Pearson Correlation Coefficient
#   B. Owners_df
# ---------------------------------------------------------------------------------------------------------------------------

Owners_corr = Owners_df.corr(method = 'pearson')
print(Owners_corr)


# In[17]:


# 4. Pearson Correlation Coefficient
#   C. OwnershipHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

OwnershipHistory_corr = OwnershipHistory_df.corr(method = 'pearson')
print(OwnershipHistory_corr)


# 1. OwnershipID and CarID: Very weak negative correlation (-0.097907), indicating no meaningful linear relationship.
# 
# 2. OwnershipID and OwnerID: Very weak positive correlation (0.005042), indicating no meaningful linear relationship.
# 
# 3. OwnershipID and SalePrice: Weak negative correlation (-0.029520), indicating a negligible linear relationship.
# 
# 4. CarID and OwnerID: Very weak positive correlation (0.005434), indicating no meaningful linear relationship.
# 
# 5. CarID and SalePrice: Weak negative correlation (-0.034504), suggesting a very slight tendency for cars with higher IDs to have lower sale prices, but the relationship is not strong.
# 
# 6. OwnerID and SalePrice: Weak negative correlation (-0.017669), indicating a very slight tendency for owners with higher IDs to have transactions with lower sale prices, which is likely not a meaningful relationship.

# In[18]:


# 4. Pearson Correlation Coefficient
#   D. VehicleCondition_df
# ---------------------------------------------------------------------------------------------------------------------------

VehicleCondition_corr = VehicleCondition_df.corr(method = 'pearson')
print(VehicleCondition_corr)


# In[19]:


# 4. Pearson Correlation Coefficient
#   E. Features_df
# ---------------------------------------------------------------------------------------------------------------------------

Features_corr = Features_df.corr(method = 'pearson')
print(Features_corr)


# In[20]:


# 4. Pearson Correlation Coefficient
#   F. Incidents_df
# ---------------------------------------------------------------------------------------------------------------------------

Incidents_corr = Incidents_df.corr(method = 'pearson')
print(Incidents_corr)


# 1. IncidentID and CarID have a very weak positive correlation (0.055759), which is negligible.
# 
# 2. IncidentID and Cost have a very weak negative correlation (-0.001110), which suggests no meaningful relationship.
# 
# 3. CarID and Cost also have a very weak negative correlation (-0.055861), indicating no significant relationship between the car's ID and the cost associated with its incidents.

# In[21]:


# 4. Pearson Correlation Coefficient
#   G. ServiceHistory_df
# ---------------------------------------------------------------------------------------------------------------------------

ServiceHistory_corr = ServiceHistory_df.corr(method = 'pearson')
print(ServiceHistory_corr)


# 1. ServiceID and CarID have a very weak positive correlation (0.013296), which is negligible.
# 
# 2. ServiceID and Cost have a very weak negative correlation (-0.006288), suggesting no significant relationship.
# 
# 3. CarID and Cost have a very weak negative correlation (-0.008768), which is also negligible.

# In[22]:


# 4. Pearson Correlation Coefficient
#   H. MarketTrends_df
# ---------------------------------------------------------------------------------------------------------------------------

MarketTrends_corr = MarketTrends_df.corr(method = 'pearson')
print(MarketTrends_corr)


# 1. TrendID and CarID have a very weak positive correlation (0.016518), which is negligible.
# 
# 2. TrendID and AverageSalePrice have a very weak negative correlation (-0.019498), indicating no significant relationship.
# 
# 3. TrendID and MarketDemand have a weak positive correlation (0.010106), which is very slight.
# 
# 4. CarID and AverageSalePrice have a very weak negative correlation (-0.015434), suggesting no meaningful relationship.
# 
# 5. CarID and MarketDemand have a very weak positive correlation (0.014181), which is negligible.
# 
# 6. AverageSalePrice and MarketDemand have a very weak negative correlation (-0.003404), indicating no significant relationship.

# In all datasets, the correlations are weak, suggesting that the identifiers (like IncidentID, ServiceID, TrendID, CarID) have no meaningful linear relationship with the other variables such as costs or market trends. This is expected because identifiers are usually arbitrarily assigned and should not logically correlate with these variables.

# Now I will create various correlation matrices to examine the relationships of the variables in each dataframe

# In[23]:


# 4. Correlation Matrices
# ---------------------------------------------------------------------------------------------------------------------------

# Correlation matrix for Cars_df
print("Correlation Analysis for Cars_df:")
print(Cars_df.corr())

# Correlation matrix for Owners_df
print("\nCorrelation Analysis for Owners_df:")
print(Owners_df.corr())

# Correlation matrix for OwnershipHistory_df
print("\nCorrelation Analysis for OwnershipHistory_df:")
print(OwnershipHistory_df.corr())

# Correlation matrix for VehicleCondition_df
print("\nCorrelation Analysis for VehicleCondition_df:")
print(VehicleCondition_df.corr())

# Correlation matrix for Features_df
print("\nCorrelation Analysis for Features_df:")
print(Features_df.corr())

# Correlation matrix for Incidents_df (if applicable)
print("\nCorrelation Analysis for Incidents_df:")
print(Incidents_df.corr())

# Correlation matrix for ServiceHistory_df
print("\nCorrelation Analysis for ServiceHistory_df:")
print(ServiceHistory_df.corr())

# Correlation matrix for MarketTrends_df
print("\nCorrelation Analysis for MarketTrends_df:")
print(MarketTrends_df.corr())


# ## Analysis of results:

# 1. Cars_df: No significant correlation between CarID, Year, and Mileage.
# 
# 2. Owners_df: No significant correlation between OwnerID and CarID.
# 
# 3. OwnershipHistory_df: Very weak correlations among OwnershipID, CarID, OwnerID, and SalePrice.
# 
# 4. VehicleCondition_df: No information on correlations other than a perfect correlation of ConditionID with itself.
# 
# 5. Features_df: No significant correlation between FeatureID and CarID.
# 
# 6. Incidents_df: Very weak correlations among IncidentID, CarID, and Cost.
# 
# 7. ServiceHistory_df: Very weak correlations among ServiceID, CarID, and Cost.
# 
# 8. MarketTrends_df: Very weak correlations among TrendID, CarID, AverageSalePrice, and MarketDemand.

# Overall, the identifiers (like IDs) show no significant correlations with other variables, which is expected. Other variables like Cost, SalePrice, and Market Demand also exhibit very weak correlations with identifiers and each other, suggesting that they are not linearly related within these datasets.

# Now for various hypothesis testing analyses using the scipy library

# In[25]:


# 5. Hypothesis Testing - Pearson Correlation and Linear Regression
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 1: Effect of Mileage on Sale Price
    # Null Hypothesis: There is no significant correlation between the mileage of a car and its sale price.
    # Alternative Hypothesis: There is a significant correlation between the mileage of a car and its sale price.
    # Test: Pearson correlation coefficient and linear regression analysis


# In[26]:


# Currently my Cars_df does not have information on the sales prices for the various vehicles, so I need to 
# merge my Cars_df with my OwnershipHistory_df to obtain the sales prices.


# In[27]:


data_df = pd.merge(Cars_df, OwnershipHistory_df[['CarID', 'SalePrice']], on='CarID', how='left')
data_df.head(5)


# In[28]:


# there are some NaN in SalePrice due to gaps in the OwnershipHistory with respect to the CarID. I will replace the NaN 
# values with the average of the Non-NaN values in SalePrice

average_sale_price = data_df['SalePrice'].mean()
data_df['SalePrice'].fillna(average_sale_price, inplace=True)
data_df.head(5)


# In[29]:


# Calculate Pearson correlation coefficient
pearson_corr, pearson_p_value = pearsonr(data_df['Mileage'], data_df['SalePrice'])
print("Pearson Correlation Coefficient:", pearson_corr)
print("P-value:", pearson_p_value)

# Perform linear regression analysis
X = sm.add_constant(data_df['Mileage']) # Adding constant term
y = data_df['SalePrice']
model = sm.OLS(y, X).fit()
print(model.summary())


# ### Hypothesis Test 1 Interpretation:
# 
# 
# Pearson Correlation Coefficient: The Pearson correlation coefficient measures the strength and direction of the linear relationship between two variables. In this case, the coefficient is approximately 0.021, indicating a very weak positive correlation between mileage and sale price. However, it's important to note that this correlation is close to zero, suggesting little to no linear relationship between the two variables.
# 
# 
# P-value: The p-value associated with the correlation coefficient is approximately 0.267. This p-value represents the probability of observing the data given that the null hypothesis (no correlation) is true. Since the p-value is greater than the conventional significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is insufficient evidence to conclude that there is a significant correlation between mileage and sale price.
# 
# 
# Linear Regression Analysis: The linear regression model further examines the relationship between mileage and sale price by estimating the coefficients of a linear equation (SalePrice = intercept + slope * Mileage). The coefficient for the 'Mileage' variable is approximately 0.0042, indicating that for each unit increase in mileage, the predicted change in sale price is very small (0.0042 units), holding all other variables constant.
# 

# In[30]:


# 5. Hypothesis Testing - One Way ANOVA
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 2: Difference in Average Sale Price between Different Car Makes:
    # Null Hypothesis: There is no significant difference in the average sale price between different car makes.
    # Alternative Hypothesis: There is a significant difference in the average sale price between different car makes.
    # Test: One-way ANOVA


# In[31]:


# I can use my merged dataframe again for these analysis.

# Create a dictionary to store sale prices for each car make
sale_prices_by_make = {}
for make, group in data_df.groupby('Make'):
    sale_prices_by_make[make] = group['SalePrice']

# Perform One-way ANOVA test
f_statistic, p_value = f_oneway(*sale_prices_by_make.values())

# Print results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret results
if p_value < 0.05:
    print("Reject null hypothesis: There is a significant difference in average sale price between different car makes.")
else:
    print("Fail to reject null hypothesis: There is no significant difference in average sale price between different car makes.")


# ### Hypothesis Test 2 Interpretation:
# 
# 
# F-statistic: The F-statistic is approximately 1.071, which is a measure of the variation between the group means relative to the variation within the groups.
# 
# 
# P-value: The p-value associated with the F-statistic is approximately 0.333. This p-value represents the probability of observing the data given that the null hypothesis (no difference in average sale price between different car makes) is true.
# 
# 
# Overall, since the p-value (0.333) is greater than the chosen significance level (e.g., 0.05), we fail to reject the null hypothesis. This means that there is insufficient evidence to conclude that there is a significant difference in average sale price between different car makes.

# In[32]:


# 5. Hypothesis Testing - One Way ANOVA
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 3: Impact of Vehicle Condition on Sale Price:
    # Null Hypothesis: There is no significant difference in the sale price of cars with different overall conditions.
    # Alternative Hypothesis: There is a significant difference in the sale price of cars with different overall conditions.
    # Test: One-way ANOVA


# In[33]:


# Again i will need to merge a few of my dataframes in order to perform this test. I need to merge my OwnershipHistory_df
# with my VehicleCondition_df

data_df2 = pd.merge(data_df, VehicleCondition_df[['CarID', 'OverallCondition']], on='CarID', how='left')
data_df2


# In[34]:


# there are some NaN in OverallCondition due to gaps in the VehicleCondition with respect to the CarID. I will drop rows
# with NaN values as I require the OverallCondition information in order to perform my test.


# In[35]:


data_df2 = data_df2.dropna()
data_df2


# In[36]:


# Perform ANOVA
# Create a dictionary to store sale prices for each vehicle condition
sale_prices_by_condition = {}
for condition, group in data_df2.groupby('OverallCondition'):
    sale_prices_by_condition[condition] = group['SalePrice']

# Perform ANOVA test
f_statistic, p_value = f_oneway(*sale_prices_by_condition.values())

# Print results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret results
if p_value < 0.05:
    print("Reject null hypothesis: There is a significant impact of vehicle condition on sale price.")
else:
    print("Fail to reject null hypothesis: There is no significant impact of vehicle condition on sale price.")


# ### Hypothesis Test 3 Interpretation:
# 
# 
# F-statistic: The F-statistic is approximately 0.177. This statistic measures the variation in sale prices between different vehicle conditions relative to the variation within each vehicle condition group.
# 
# 
# P-value: The p-value associated with the F-statistic is approximately 0.912. This p-value represents the probability of observing the data given that the null hypothesis (no significant impact of vehicle condition on sale price) is true.
# 
# 
# Overall, since the p-value (0.912) is much greater than the chosen significance level (e.g., 0.05), we fail to reject the null hypothesis. This means that there is insufficient evidence to conclude that there is a significant impact of vehicle condition on sale price.

# In[37]:


# 5. Hypothesis Testing - One Way ANOVA
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 4: Effect of Fuel Type on Fuel Efficiency:
    # Null Hypothesis: There is no significant difference in fuel efficiency between different fuel types.
    # Alternative Hypothesis: There is a significant difference in fuel efficiency between different fuel types.
    # Test: ANOVA


# In[38]:


# Since my Cars_df already has both EngineType and FuelType I can just use this dataframe for this test. However, I 
# will need to calculate Fuel Efficiency. Using the vehicle's year I will do so by dividing the mileage for each car by the #
# of years the vehicle has been on the road. Ie; if 2020 vehicle then that is 4 years, 2021 is 3 years etc.

Cars_df2 = Cars_df # I still want to preserve original Cars_df

current_year = pd.Timestamp.now().year
Cars_df2['Age'] = current_year - Cars_df2['Year']

# Now i have a column for the Age and can calulcate a miles/year to use for Fuel Efficiency;
Cars_df2['MPY'] = Cars_df2['Mileage'] / Cars_df2['Age']

Cars_df2


# In[39]:


# Create a dictionary to store fuel efficiencies for each fuel type
fuel_efficiencies_by_fuel_type = {}
for fuel_type, group in Cars_df2.groupby('FuelType'):
    fuel_efficiencies_by_fuel_type[fuel_type] = group['MPY']

# Perform ANOVA test
f_statistic, p_value = f_oneway(*fuel_efficiencies_by_fuel_type.values())

# Print results
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret results
if p_value < 0.05:
    print("Reject null hypothesis: There is a significant effect of engine type on fuel efficiency.")
else:
    print("Fail to reject null hypothesis: There is no significant effect of engine type on fuel efficiency.")


# ### Hypothesis Test 4 Interpretation:
# 
# 
# F-statistic: The F-statistic is approximately 0.089. This statistic measures the variation in fuel efficiencies between different engine types relative to the variation within each engine type group.
# 
# 
# P-value: The p-value associated with the F-statistic is approximately 0.966. This p-value represents the probability of observing the data given that the null hypothesis (no significant effect of engine type on fuel efficiency) is true.
# 
# 
# Overall, since the p-value (0.966) is much greater than the chosen significance level (e.g., 0.05), we fail to reject the null hypothesis. This means that there is insufficient evidence to conclude that there is a significant effect of engine type on fuel efficiency.

# In[40]:


# 5. Hypothesis Testing - Chi-Square and Logistic Regression
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 5: Association between Incidents and Market Demand:
    # Null Hypothesis: There is no association between the occurrence of incidents (accidents or damages) 
    # and market demand for a car.
    # Alternative Hypothesis: There is an association between the occurrence of incidents and market demand for a car.
    # Test: Chi-square test of independence and logisitc regression


# In[41]:


# First I will sum the # of incidents per carID;

incidents_sum_per_car = Incidents_df.groupby('CarID')['IncidentID'].count().reset_index()
incidents_sum_per_car.rename(columns={'IncidentID': 'TotalIncidents'}, inplace=True)


# In[42]:


# Now I will add the incidents per carID as a new column at the end of my Cars_df

Cars_df3 = pd.merge(Cars_df, incidents_sum_per_car, on = 'CarID', how = 'left')
Cars_df3


# In[43]:


# If a CarID has NaN as the value for the sum of incidents, that indicates there were 0 incidents and so
# i will replace these NaNs with 0

Cars_df3['TotalIncidents'].fillna(0, inplace=True)
Cars_df3.head(20)


# In[44]:


# Now i am ready to bring over the MarketDemand into my Cars_df3 for testing

data_df3 = pd.merge(Cars_df3, MarketTrends_df[['CarID', 'MarketDemand']], on='CarID', how='left')
data_df3


# In[45]:


# there are some NaN in MarketDemand due to gaps in the MarketTrends with respect to the CarID. I will replace the NaN 
# values with the average of the Non-NaN values in MarketDemand

average_market_demand = data_df3['MarketDemand'].mean()
data_df3['MarketDemand'].fillna(average_market_demand, inplace=True)
data_df3.head(20)


# In[46]:


# Now i can perform my chi-square and logistic regression tests

contingency_table = pd.crosstab(data_df3['TotalIncidents'], data_df3['MarketDemand'])
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Print results
print("Chi-square statistic:", chi2)
print("P-value:", p_value)

# Interpret results
if p_value < 0.05:
    print("Reject null hypothesis: There is a significant association between incidents and market demand.")
else:
    print("Fail to reject null hypothesis: There is no significant association between incidents and market demand.")

# Perform logistic regression
# Convert 'Incidents' and 'MarketDemand' to binary variables (0 or 1)
data_df3['Incidents_binary'] = np.where(data_df3['TotalIncidents'] > 0, 1, 0)
data_df3['MarketDemand_binary'] = np.where(data_df3['MarketDemand'] > 0, 1, 0)

# Fit logistic regression model
X = data_df3['Incidents_binary']
y = data_df3['MarketDemand_binary']
X = sm.add_constant(X)
logit_model = sm.Logit(y, X)
result = logit_model.fit()

# Print summary of logistic regression model
print(result.summary())


# ### Hypothesis Test 5 Interpretation:
# 
# 
# The Chi-square test indicates that there is no significant association between incidents and market demand.
# 
# 
# The logistic regression model did not converge due to perfect separation, making the estimates unreliable.
# 
# 
# The findings suggest that, based on the available data, there is no evidence of a significant association between incidents and market demand.

# In[47]:


# 5. Hypothesis Testing - Time-Series Analysis
# 6. Data Manipulation
# ---------------------------------------------------------------------------------------------------------------------------

# Hpothesis Test 6: Trend Analysis of Average Sale Price over Time:
    # Null Hypothesis: There is no significant trend in the average sale price of cars over time.
    # Alternative Hypothesis: There is a significant increasing or decreasing trend in the average sale price of cars over time.
    # Test: Time-series analysis


# In[48]:


MarketTrends_df2 = MarketTrends_df
MarketTrends_df2


# In[49]:


MarketTrends_df2['Date'] = pd.to_datetime(MarketTrends_df2['Date'])
MarketTrends_df2


# In[50]:


# 7. Data visualization
# ---------------------------------------------------------------------------------------------------------------------------

# My MarketTrends dataframe already has the required columns needed for this analysis so I will use MarketTrends_df

# Set 'Date' column as index
MarketTrends_df2.set_index('Date', inplace=True)

# Resample the data to monthly frequency and calculate average sale price for each month
monthly_avg_sale_price = MarketTrends_df2['AverageSalePrice'].resample('M').mean()

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_sale_price)
plt.title('Average Sale Price Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sale Price')
plt.grid(True)
plt.show()

# Perform time-series decomposition (optional)
decomposition = sm.tsa.seasonal_decompose(monthly_avg_sale_price, model='additive')
fig = decomposition.plot()
plt.show()


# ### Hypothesis Test 6 Interpretation:
# 
# 
# Time Series Plot (Top): This shows fluctuations in the average sale price over time. There's a clear cyclical pattern, suggesting seasonality in the data, with peaks and troughs occurring at regular intervals.
# 
# 
# Time Series Decomposition (Bottom):
#    - Trend: The trend component indicates the long-term progression of the average sale price. It seems to increase and decrease at different times, but without a clear overall upward or downward trend over the period shown.
#    
# 
#    - Seasonal: The seasonal component captures the regular pattern within each year, which repeats itself. This could be due to various factors like market demand changes, sales incentives, or other seasonal factors.
# 
# 
#    - Residual: The residuals, or the noise in the data, show what's left after the trend and seasonal components are removed. Ideally, the residuals should be random and small; however, there are some larger fluctuations, indicating potential outliers or other patterns not captured by the model.
#    
#    
# 
# This analysis is valuable for understanding the dynamics of sale prices over time and can help in forecasting future trends or identifying periods of high or low average sale prices.

# # ----------------------------------- END Python Script -----------------------------------------------

# <hr style="border:2px solid blue">
# 
#    ### Begin Data Visualization Script
# 
# <hr style="border:2px solid blue">

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

# import pandas as pd #already imported
# import matplotlib.pyplot as plt #already imported
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




