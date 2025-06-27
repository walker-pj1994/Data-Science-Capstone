drop table MarketTrends;
drop table ServiceHistory;
drop table Features;
drop table OwnershipHistory;
drop table Owners;
drop table Cars;
drop table vehiclecondition;
drop table incidents;

CREATE TABLE Cars (
    CarID INT PRIMARY KEY,
    Make VARCHAR(255),
    Model VARCHAR(255),
    Year INT,
    Mileage INT,
    VIN VARCHAR(255),
    EngineType VARCHAR(255),
    TransmissionType VARCHAR(255),
    FuelType VARCHAR(255)
);

CREATE TABLE Owners (
    OwnerID INT PRIMARY KEY,
    CarID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    ContactInfo VARCHAR(255),
    State VARCHAR(2),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE OwnershipHistory (
    OwnershipID INT PRIMARY KEY,
    CarID INT,
    OwnerID INT,
    PurchaseDate DATE,
    SaleDate DATE,
    SalePrice DECIMAL,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID),
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);

CREATE TABLE VehicleCondition (
    ConditionID INT PRIMARY KEY,
    CarID INT,
    OverallCondition VARCHAR(255),
    ExteriorCondition VARCHAR(255),
    InteriorCondition VARCHAR(255),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE Features (
    FeatureID INT PRIMARY KEY,
    CarID INT,
    FeatureName VARCHAR(255),
    FeatureValue VARCHAR(255),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE Incidents (
    IncidentID INT PRIMARY KEY,
    CarID INT,
    IncidentDate DATE,
    Description TEXT,
    Cost DECIMAL,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE ServiceHistory (
    ServiceID INT PRIMARY KEY,
    CarID INT,
    ServiceDate DATE,
    ServiceType VARCHAR(255),
    Cost DECIMAL,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);

CREATE TABLE MarketTrends (
    TrendID INT PRIMARY KEY,
    CarID INT,
    Date DATE,
    AverageSalePrice DECIMAL,
    MarketDemand INT,
    FOREIGN KEY (CarID) REFERENCES Cars(CarID)
);