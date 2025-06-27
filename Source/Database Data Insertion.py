#!/usr/bin/env python
# coding: utf-8

# ## Python Script Overview
# 
# This Python script is designed to populate a MySQL database named dtsc_vehicles with synthetic data related to various aspects of the automotive industry. Let's break down the key components and functionalities of this script:
# 
#    1. Importing Necessary Libraries: The script begins by importing the required libraries: Faker for generating fake data, VehicleProvider from faker_vehicle to provide vehicle-related data, random for generating random numbers, and mysql.connector for connecting to the MySQL database.
#    
#    
#    2. Seeding Randomness: The script seeds the random number generator for reproducibility. This ensures that each time the script is run with the same seed, it produces the same sequence of random numbers.
#    
#    
#    3. Data Generation Functions: Several functions are defined to generate fake data for different tables in the database. Each function follows a similar structure where it uses the Faker library to create realistic data for specific attributes of the tables. Functions like generate_cars_data, generate_owners_data, generate_ownership_history_data, generate_vehicle_condition_data, generate_features_data, generate_incidents_data, generate_service_history_data, and generate_market_trends_data are defined for generating data for respective tables like Cars, Owners, OwnershipHistory, VehicleCondition, Features, Incidents, ServiceHistory, and MarketTrends.
#    
#     
#    4. Database Connection: The script establishes a connection to the MySQL database named dtsc_vehicles. It provides the host, username, password, and database name for establishing the connection.
#    
#     
#    5. Data Insertion: For each table, the script generates fake data using the corresponding data generation function. It then constructs an SQL INSERT query to insert the generated data into the respective table. The executemany() method is used to execute the INSERT query for bulk insertion of data. After insertion, the changes are committed to the database using conn.commit().
#    
#     
#    6. Error Handling: Exception handling is implemented to catch any errors that may occur during data insertion. If an error occurs, it prints an error message indicating the nature of the error. Regardless of whether an error occurs or not, the script ensures that the database connection is properly closed after data insertion.
#    
#     
#    7. Closing Database Connection: After completing data insertion for each table, the script closes the cursor and the database connection using cursor.close() and conn.close() respectively.
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

# In[ ]:




