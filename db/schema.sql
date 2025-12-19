
-- 1. Devices
-- -----------------------------------------------------
CREATE TABLE Devices (
    DeviceID INT PRIMARY KEY AUTO_INCREMENT,
    SerialNumber VARCHAR(255),
    DeviceType VARCHAR(100),
    Brand VARCHAR(100),
    Model VARCHAR(100),
    ManufactureDate DATE,
    CollectionPointID INT,
    StatusID INT,
    ReceivedDate DATE,
    FOREIGN KEY (CollectionPointID) REFERENCES CollectionPoints(CollectionPointID),
    FOREIGN KEY (StatusID) REFERENCES DeviceStatus(StatusID)
);

-- -----------------------------------------------------
-- 2. CollectionPoints
-- -----------------------------------------------------
CREATE TABLE CollectionPoints (
    CollectionPointID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Location VARCHAR(255),
    ManagerName VARCHAR(255),
    ContactNumber VARCHAR(50),
    Capacity INT
);

-- -----------------------------------------------------
-- 3. CollectionEvents
-- -----------------------------------------------------
CREATE TABLE CollectionEvents (
    EventID INT PRIMARY KEY AUTO_INCREMENT,
    CollectionPointID INT,
    EventDate DATE,
    CollectedBy VARCHAR(255),
    DeviceCount INT,
    Notes TEXT,
    FOREIGN KEY (CollectionPointID) REFERENCES CollectionPoints(CollectionPointID)
);

-- -----------------------------------------------------
-- 4. DeviceStatus
-- -----------------------------------------------------
CREATE TABLE DeviceStatus (
    StatusID INT PRIMARY KEY AUTO_INCREMENT,
    StatusName VARCHAR(100),
    Description TEXT
);

-- -----------------------------------------------------
-- 5. SortingResults
-- -----------------------------------------------------
CREATE TABLE SortingResults (
    SortingID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    SortingDate DATE,
    Category VARCHAR(100),
    SortedBy VARCHAR(255),
    Remarks TEXT,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

-- -----------------------------------------------------
-- 6. RefurbishmentJobs
-- -----------------------------------------------------
CREATE TABLE RefurbishmentJobs (
    JobID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    StartDate DATE,
    EndDate DATE,
    TechnicianID VARCHAR(255),
    JobStatus VARCHAR(100),
    Notes TEXT,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

-- -----------------------------------------------------
-- 7. PartsInventory
-- -----------------------------------------------------
CREATE TABLE PartsInventory (
    PartID INT PRIMARY KEY AUTO_INCREMENT,
    PartName VARCHAR(255),
    PartType VARCHAR(100),
    Condition VARCHAR(100),
    Quantity INT,
    Location VARCHAR(255),
    DeviceID INT,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

-- -----------------------------------------------------
-- 8. DismantlingLogs
-- -----------------------------------------------------
CREATE TABLE DismantlingLogs (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    DismantleDate DATE,
    TechnicianID VARCHAR(255),
    RecoveredPartsCount INT,
    HazardousMaterialFlag BOOLEAN,
    Notes TEXT,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

-- -----------------------------------------------------
-- 9. MaterialRecoveryLogs
-- -----------------------------------------------------
CREATE TABLE MaterialRecoveryLogs (
    RecoveryID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    MaterialType VARCHAR(100),
    Quantity DECIMAL(10,3),
    RecoveryDate DATE,
    RecoveredBy VARCHAR(255),
    Destination VARCHAR(255),
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

-- -----------------------------------------------------
-- 10. DisposalRecords
-- -----------------------------------------------------
CREATE TABLE DisposalRecords (
    DisposalID INT PRIMARY KEY AUTO_INCREMENT,
    DeviceID INT,
    DisposalDate DATE,
    Method VARCHAR(100),
    DisposedBy VARCHAR(255),
    ComplianceCertificate BOOLEAN,
    Notes TEXT,
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);