# Used Vehicle Sales Database & Analysis Project

## Overview

This project is the culmination of the DTSC 691 Capstone (Spring 2024) and focuses on the design, implementation, and analysis of a relational database for the used vehicle market. The data is artificially generated using the Faker library to simulate real-world automotive records, enabling robust database development, data analysis, and visualization techniques.

---

## Project Goals

- Design and implement a comprehensive relational database for used vehicle sales
- Generate realistic synthetic data for vehicles, owners, transactions, service history, market trends, and more
- Perform statistical and visual analysis to identify patterns and insights in the used car market
- Create a scalable and well-documented platform for future analytical enhancements and potential predictive modeling

---

## Database Design

The database was implemented in **MySQL** with GUI support via **DBeaver**. Key tables include:

- `Cars`: Vehicle details (make, model, VIN, mileage, etc.)
- `Owners`: Owner contact and location data
- `OwnershipHistory`: Tracks purchase and sale history
- `VehicleCondition`: Vehicle condition snapshots over time
- `Features`: Feature availability (e.g., Bluetooth, ABS)
- `Incidents`: Traffic incident records and associated costs
- `ServiceHistory`: Maintenance service records and costs
- `MarketTrends`: Time-based market valuation and demand

---

## Tools & Technologies

- **DBMS**: MySQL, MySQL Workbench, DBeaver
- **Programming**: Python (Jupyter Notebooks)
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, SciPy, Statsmodels, WordCloud, Faker
- **Data Generation**: Python Faker library with `faker_vehicle` provider
- **ETL**: MySQL connector and Python scripts for data insertion

---

## Key Analyses

- Correlation and regression analyses on mileage, vehicle condition, incidents, and sale price
- ANOVA and chi-square tests for car make impact and incident correlation
- Time series decomposition of sale price trends
- Visualization of ownership trends, market demand, and transmission types

> ⚠️ **Note**: The analysis is based on synthetic data and some results (e.g., no correlation between condition and price) may not align with real-world logic.

---

## Notable SQL Queries

- Top 5 owners by car ownership
- Incident cost per car model
- Sale price trends by transmission type
- VINs of cars with the same make/model but different transmissions
- Most recent service per vehicle

(See `/sql/` for full query examples)

---

## Visualizations

Utilized Seaborn and Matplotlib for:

- Histograms, scatter plots, line charts, box/violin plots
- Heatmaps of correlation matrices
- Word clouds for incident types
- Seasonal trend exploration

---

## Future Enhancements

- Integrate real-world datasets for validation
- Implement machine learning for predictive pricing and demand modeling
- Expand geographic coverage for regional analysis
- Track external economic indicators (e.g., gas prices, interest rates)

---

## Author

**Paul J. Walker**  
Business Strategy Analyst  
Automotive Finance Industry  
📍 Pennsylvania, USA

---

## License

This project is developed for academic purposes as part of the MS in Data Science program and uses synthetic data generated solely for educational and research use.

