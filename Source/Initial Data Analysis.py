#!/usr/bin/env python
# coding: utf-8

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

import pandas as pd
import numpy as np

import statsmodels.api as sm
import matplotlib.pyplot as plt

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

# In[ ]:




