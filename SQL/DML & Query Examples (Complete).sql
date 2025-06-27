/* I created all of my tables via an initial SQL DDL statements and then generated all 
of my fake data via Python. I used the mysql.connector driver to connect my Python notebook 
(Jupyter notebook) to MySQL server. Using mysql.connector and creating a cursor object
I am able to execute SQL DML statements directly to my server straight from my python notebook. 
This code is available in detail within my "Database Data Insertion.py" file but to satisfy the
requirement to include a SQL file containing thes statements - rather than repeating all of that 
code here (which wouldn't work anyway) each of my DML statements in python follow this structure;*/
/* ------------------------------------------------------------------------------------------------------------------------

conn = mysql.connector.connect(
    host='localhost',
    user='paul_walker',
    password='dtsc691root',
    database='dtsc_vehicles'
)

cursor = conn.cursor()
try:
    cars_data = generate_cars_data(2000)
    insert_query = "INSERT INTO Cars (CarID, Make, Model, Year, Mileage, VIN, EngineType, TransmissionType, FuelType) 
								VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor.executemany(insert_query, cars_data)
    conn.commit()

    print("Data inserted successfully.")
except mysql.connector.Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()
    
-------------------------------------------------------------------------------------------------------------------------- */

/* Below please find SQL code for various queries that interact with my database. */

/* ----------------------------------------------------------------------------------------------------------------------- */

	/* 1. Retrieve all cars with their make, model, and VIN: This query fetches basic information about all cars in the 
	   database. */

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				Make, 
				Model, 
				VIN
			FROM Cars;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/
    

	/* 2. Retrieve the total number of incidents for each car: This query counts the number of incidents associated with each car, 
	   including those with zero incidents */

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/   
			SELECT 
				c.CarID, 
				COUNT(i.IncidentID) AS TotalIncidents
			FROM Cars c
			LEFT JOIN Incidents i ON c.CarID = i.CarID
			GROUP BY 
				c.CarID;            
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 3. Find the average sale price and total market demand for each year: This query calculates the average sale price and 
   total market demand for cars for each year.*/

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/   
			SELECT 
				YEAR(mt.Date) AS Year, 
				AVG(mt.AverageSalePrice) AS AvgSalePrice, 
				SUM(mt.MarketDemand) AS TotalDemand
			FROM MarketTrends mt
			GROUP BY 
				YEAR(mt.Date);            
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 4. Get the top 5 owners who have the most cars: This query identifies the top 5 owners based on the number of cars they 
   own.*/

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				o.OwnerID, 
				CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName, 
				COUNT(oh.CarID) AS TotalCarsOwned
			FROM Owners o
			JOIN OwnershipHistory oh ON o.OwnerID = oh.OwnerID
			GROUP BY 
				o.OwnerID
			ORDER BY 
				TotalCarsOwned DESC
			LIMIT 5;
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 5. Retrieve the number of incidents that occurred in each state: This query counts the number of incidents that occurred 
in each state based on the owner's state. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/    
			SELECT 
				o.State, 
				COUNT(i.IncidentID) AS TotalIncidents
			FROM Owners o
			JOIN Cars c ON o.CarID = c.CarID
			JOIN Incidents i ON c.CarID = i.CarID
			GROUP BY 
				o.State;            
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    


/* 6. Find the total cost of services for each car: This query calculates the total service cost for each car. */

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/    
			SELECT 
				c.CarID, 
				SUM(sh.Cost) AS TotalServiceCost
			FROM Cars c
			JOIN ServiceHistory sh ON c.CarID = sh.CarID
			GROUP BY 
				c.CarID;		
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 7. Identify the average mileage for cars of each make and model: This query calculates the average mileage for cars 
grouped by make and model. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				Make, 
				Model, 
				AVG(Mileage) AS AvgMileage
			FROM Cars
			GROUP BY 
				Make, 
				Model;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    
 
 
/* 8. Retrieve the total number of incidents and average cost of incidents for each car model: This query calculates the 
total number of incidents and the average cost of incidents for each car model. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.Model, 
				COUNT(i.IncidentID) AS TotalIncidents, 
				IFNULL(AVG(i.Cost),0) AS AvgIncidentCost
			FROM Cars c
			LEFT JOIN Incidents i ON c.CarID = i.CarID
			GROUP BY 
				c.Model;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 9.Find the top 3 car models with the highest average sale price: This query identifies the top 3 car models with the 
   highest average sale price. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.Make, 
				c.Model, 
				AVG(mt.AverageSalePrice) AS AvgSalePrice
			FROM Cars c
			JOIN MarketTrends mt ON c.CarID = mt.CarID
			GROUP BY 
				c.Make, 
				c.Model
			ORDER BY 
				AvgSalePrice DESC
			LIMIT 3;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    
 

/* 10. Identify the owner who has owned the most cars and the total number of cars they've owned: This query identifies the 
   owner who has owned the most cars and the total number of cars they've owned. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				o.OwnerID, 
				CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName, 
				COUNT(oh.CarID) AS TotalCarsOwned
			FROM Owners o
			JOIN OwnershipHistory oh ON o.OwnerID = oh.OwnerID
			GROUP BY 
				o.OwnerID
			ORDER BY 
				TotalCarsOwned DESC
			LIMIT 1;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/


/* 11. Calculate the total revenue generated from car sales in each year: This query calculates the total revenue generated 
   from car sales for each year. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				YEAR(t.SaleDate) AS Year, 
				SUM(t.SalePrice) AS TotalRevenue
			FROM OwnershipHistory t
			GROUP BY 
				YEAR(t.SaleDate);        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    
 
 
/* 12. Retrieve the most recent service date and type of service for each car: This query retrieves the most recent service 
   date and type of service for each car. */

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.CarID, 
				MAX(sh.ServiceDate) AS MostRecentServiceDate, 
				sh.ServiceType
			FROM Cars c
			LEFT JOIN ServiceHistory sh ON c.CarID = sh.CarID
			GROUP BY 
				c.CarID, 
				sh.ServiceType;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/   

    
/* 13. Find the average market demand for cars with mileage less than 50,000: This query calculates the average market demand 
   for cars with mileage less than 50,000. */

	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				AVG(mt.MarketDemand) AS AvgMarketDemand
			FROM MarketTrends mt
			JOIN Cars c ON mt.CarID = c.CarID
			WHERE 
				c.Mileage < 50000;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    

    
/* 14. Identify the owner with the highest total service cost and their contact information: This query identifies the owner 
   with the highest total service cost and their contact information */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				o.OwnerID, 
				CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName, 
				o.ContactInfo, SUM(sh.Cost) AS TotalServiceCost
			FROM Owners o
			JOIN Cars c ON o.CarID = c.CarID
			JOIN ServiceHistory sh ON c.CarID = sh.CarID
			GROUP BY 
				o.OwnerID
			ORDER BY 
				TotalServiceCost DESC
			LIMIT 1;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/   

    
/* 15. Calculate the average sale price for cars of each transmission type: This query calculates the average sale price for 
   cars grouped by transmission type. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.TransmissionType, 
				AVG(mt.AverageSalePrice) AS AvgSalePrice
			FROM Cars c
			JOIN MarketTrends mt ON c.CarID = mt.CarID
			GROUP BY 
				c.TransmissionType;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    

    
/* 16. Retrieve the make and model of cars that have been involved in incidents with a cost greater than $1000: This query 
   retrieves the make and model of cars involved in incidents with a cost greater than $1000. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT DISTINCT 
				c.Make, 
				c.Model
			FROM Cars c
			JOIN Incidents i ON c.CarID = i.CarID
			WHERE 
				i.Cost > 1000;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    

    
/* 17. Find the top 3 owners with the highest average mileage of their cars: This query identifies the top 3 owners with the 
   highest average mileage of their cars. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				o.OwnerID, 
				CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName, 
				AVG(c.Mileage) AS AvgMileage
			FROM Owners o
			JOIN Cars c ON o.CarID = c.CarID
			GROUP BY 
				o.OwnerID
			ORDER BY 
				AvgMileage DESC
			LIMIT 3;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    

    
/* 18. Retrieve the VINs of cars with the same make and model that have different transmission types: This query retrieves the 
   VINs of cars with the same make and model but different transmission types. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT DISTINCT 
				c1.VIN
			FROM Cars c1
			JOIN Cars c2 ON c1.Make = c2.Make AND c1.Model = c2.Model AND c1.TransmissionType <> c2.TransmissionType;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/
 
    
/* 19. Calculate the total number of incidents and their average cost for cars with a mileage greater than 100,000: This query 
   calculates the total number of incidents and their average cost for cars with mileage greater than 100,000. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				COUNT(i.IncidentID) AS TotalIncidents, 
				AVG(i.Cost) AS AvgIncidentCost
			FROM Incidents i
			JOIN Cars c ON i.CarID = c.CarID
			WHERE 
				c.Mileage > 100000;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/    

    
/* 20. Retrieve the top 5 owners who have sold their cars for the highest total sale price: This query retrieves the top 5 
   owners who have sold their cars for the highest total sale price. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				o.OwnerID, 
				CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName, 
				SUM(ps.SalePrice) AS TotalSalePrice
			FROM Owners o
			JOIN OwnershipHistory ps ON o.OwnerID = ps.OwnerID
			GROUP BY 
				o.OwnerID
			ORDER BY 
				TotalSalePrice DESC
			LIMIT 5;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/   

    
/* 21. Find the average number of previous owners for cars of each make: This query calculates the average number of previous 
   owners for cars grouped by make. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.Make, 
				AVG(oh.OwnershipCount) AS AvgPreviousOwners
			FROM Cars c
			JOIN (
					SELECT 
						CarID, 
						COUNT(DISTINCT OwnerID) AS OwnershipCount
					FROM OwnershipHistory
					GROUP BY 
						CarID
				) oh ON c.CarID = oh.CarID
			GROUP BY 
				c.Make;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/   

    
/* 22. Retrieve the top 3 most common exterior conditions among cars: This query retrieves the top 3 most common exterior 
   conditions among cars. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				ExteriorCondition, 
				COUNT(*) AS Count
			FROM VehicleCondition
			GROUP BY 
				ExteriorCondition
			ORDER BY 
				Count DESC
			LIMIT 3;        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/
    

/* 23. Identify the make and model of cars that have the highest total service cost: This query identifies the make and model 
   of cars that have the highest total service cost. */
   
	/*-------------------------------------------------- Code Start -------------------------------------------------------*/		
			SELECT 
				c.Make, 
				c.Model, 
				SUM(sh.Cost) AS TotalServiceCost
			FROM Cars c
			JOIN ServiceHistory sh ON c.CarID = sh.CarID
			GROUP BY 
				c.Make, 
				c.Model
			ORDER BY 
				TotalServiceCost DESC
			LIMIT 1;       
        
	/*--------------------------------------------------- Code End ---------------------------------------------------------*/
  