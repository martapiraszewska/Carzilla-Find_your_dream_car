CREATE TABLE "Car" (
  "Car_ID" integer PRIMARY KEY,
  "Brand" text NOT NULL,
  "Model" text NOT NULL,
  "Color" text NOT NULL,
  "Mileage" integer NOT NULL,
  "Price" integer NOT NULL,
  "Condition_ID" integer NOT NULL,
  "Dealer_ID" integer NOT NULL
);

CREATE TABLE "Car_condition" (
  "Condition_ID" integer PRIMARY KEY,
  "Condition" name NOT NULL
);

CREATE TABLE "Car_dealer" (
  "Car_dealer_ID" integer PRIMARY KEY,
  "Name" text NOT NULL,
  "Address_ID" integer NOT NULL
);

CREATE TABLE "Address" (
  "Address_ID" integer PRIMARY KEY,
  "Postcode" text NOT NULL,
  "Street" text NOT NULL,
  "Street_number" integer NOT NULL,
  "City_ID" integer NOT NULL
);

CREATE TABLE "City" (
  "City_ID" integer PRIMARY KEY,
  "Name" text NOT NULL,
  "Country" text NOT NULL
);

CREATE TABLE "Client" (
  "Client_ID" integer PRIMARY KEY,
  "Name" text NOT NULL,
  "Surname" text NOT NULL,
  "Gender" text NOT NULL,
  "Mail" text NOT NULL,
  "Phone" text NOT NULL
);

CREATE TABLE "Transaction" (
  "Transaction_ID" integer PRIMARY KEY,
  "Date" date NOT NULL,
  "Value" integer NOT NULL,
  "Client_ID" integer NOT NULL,
  "Employee_ID" integer NOT NULL,
  "Transaction_type_ID" integer NOT NULL,
  "Invoice_ID" integer UNIQUE
);

CREATE TABLE "Employee" (
  "Employee_ID" integer PRIMARY KEY,
  "Name" text NOT NULL,
  "Surname" text NOT NULL,
  "Gender" text NOT NULL,
  "Salary" integer,
  "Date_of_birth" date NOT NULL,
  "Phone_number" text,
  "Employee_status_ID" integer NOT NULL,
  "Car_dealer_ID" integer NOT NULL,
  "Login_credentials_ID" integer NOT NULL
);

CREATE TABLE "Employee_status" (
  "Employee_status_ID" integer PRIMARY KEY,
  "Status_name" text NOT NULL
);

CREATE TABLE "Position" (
  "Position_ID" integer PRIMARY KEY,
  "Name" text NOT NULL,
  "Min_salary" integer,
  "Max_salary" integer
);

CREATE TABLE "Position_history" (
  "Position_history_ID" integer PRIMARY KEY,
  "Date_start" date NOT NULL,
  "Date_end" date,
  "Position_ID" integer NOT NULL,
  "Employee_ID" integer NOT NULL
);

CREATE TABLE "Transaction_type" (
  "Transaction_type_ID" integer PRIMARY KEY,
  "Name" text NOT NULL
);

CREATE TABLE "Invoice" (
  "Invoice_ID" integer PRIMARY KEY,
  "Status" text NOT NULL,
  "Issue_date" date,
  "NIP" integer NOT NULL
);

CREATE TABLE "Employee_stats" (
  "Year" integer,
  "Month" integer,
  "Employee_ID" integer,
  "Sales_sum" integer NOT NULL,
  PRIMARY KEY ("Year", "Month", "Employee_ID")
);

CREATE TABLE "Login_credentials" (
  "Login_credentials_ID" integer PRIMARY KEY,
  "Login" text NOT NULL,
  "Password" text NOT NULL
);

ALTER TABLE "Car" ADD FOREIGN KEY ("Condition_ID") REFERENCES "Car_condition" ("Condition_ID");

ALTER TABLE "Car" ADD FOREIGN KEY ("Dealer_ID") REFERENCES "Car_dealer" ("Car_dealer_ID");

ALTER TABLE "Transaction" ADD FOREIGN KEY ("Client_ID") REFERENCES "Client" ("Client_ID");

ALTER TABLE "Transaction" ADD FOREIGN KEY ("Employee_ID") REFERENCES "Employee" ("Employee_ID");

ALTER TABLE "Address" ADD FOREIGN KEY ("City_ID") REFERENCES "City" ("City_ID");

ALTER TABLE "Employee" ADD FOREIGN KEY ("Employee_status_ID") REFERENCES "Employee_status" ("Employee_status_ID");

ALTER TABLE "Employee" ADD FOREIGN KEY ("Car_dealer_ID") REFERENCES "Car_dealer" ("Car_dealer_ID");

ALTER TABLE "Position_history" ADD FOREIGN KEY ("Employee_ID") REFERENCES "Employee" ("Employee_ID");

ALTER TABLE "Position_history" ADD FOREIGN KEY ("Position_ID") REFERENCES "Position" ("Position_ID");

ALTER TABLE "Transaction" ADD FOREIGN KEY ("Transaction_type_ID") REFERENCES "Transaction_type" ("Transaction_type_ID");

ALTER TABLE "Transaction" ADD FOREIGN KEY ("Invoice_ID") REFERENCES "Invoice" ("Invoice_ID");

ALTER TABLE "Car_dealer" ADD FOREIGN KEY ("Address_ID") REFERENCES "Address" ("Address_ID");

ALTER TABLE "Employee_stats" ADD FOREIGN KEY ("Employee_ID") REFERENCES "Employee" ("Employee_ID");

ALTER TABLE "Employee" ADD FOREIGN KEY ("Login_credentials_ID") REFERENCES "Login_credentials" ("Login_credentials_ID");

-- SOME DATA

INSERT INTO "City" ("City_ID", "Name", "Country") VALUES (1, 'Davisside', 'Mongolia');
INSERT INTO "City" ("City_ID", "Name", "Country") VALUES (2, 'Carlachester', 'Slovakia (Slovak Republic)');
INSERT INTO "City" ("City_ID", "Name", "Country") VALUES (3, 'Leeberg', 'Trinidad and Tobago');
INSERT INTO "City" ("City_ID", "Name", "Country") VALUES (4, 'Davidbury', 'United Kingdom');
INSERT INTO "City" ("City_ID", "Name", "Country") VALUES (5, 'Burnettmouth', 'Cote dIvoire');
INSERT INTO "Address" ("Address_ID", "Postcode", "Street", "Street_number", "City_ID") VALUES (1, '38388', 'Chad Lights', 158, 1);
INSERT INTO "Address" ("Address_ID", "Postcode", "Street", "Street_number", "City_ID") VALUES (2, '12988', 'Pollard Run', 121, 2);
INSERT INTO "Address" ("Address_ID", "Postcode", "Street", "Street_number", "City_ID") VALUES (3, '93152', 'Williams Inlet', 84, 3);
INSERT INTO "Address" ("Address_ID", "Postcode", "Street", "Street_number", "City_ID") VALUES (4, '55067', 'Oconnell Square', 178, 4);
INSERT INTO "Address" ("Address_ID", "Postcode", "Street", "Street_number", "City_ID") VALUES (5, '15204', 'Bradley Manors', 52, 5);
INSERT INTO "Car_condition" ("Condition_ID", "Condition") VALUES (1, 'New');
INSERT INTO "Car_condition" ("Condition_ID", "Condition") VALUES (2, 'Used');
INSERT INTO "Car_condition" ("Condition_ID", "Condition") VALUES (3, 'Damaged');
INSERT INTO "Car_dealer" ("Car_dealer_ID", "Name", "Address_ID") VALUES (1, 'Randolph PLC', 1);
INSERT INTO "Car_dealer" ("Car_dealer_ID", "Name", "Address_ID") VALUES (2, 'Perez, Brock and Ward', 2);
INSERT INTO "Car_dealer" ("Car_dealer_ID", "Name", "Address_ID") VALUES (3, 'Kemp-Mccullough', 3);
INSERT INTO "Employee_status" ("Employee_status_ID", "Status_name") VALUES (1, 'Active');
INSERT INTO "Employee_status" ("Employee_status_ID", "Status_name") VALUES (2, 'On Leave');
INSERT INTO "Login_credentials" ("Login_credentials_ID", "Login", "Password") VALUES (1, 'admin', 'scrypt:32768:8:1$Pq1rpiPhKce7y1yA$a1f05c2896846128e181cb48c634e673aafec41268f33d666fb944dc0b71a019f3a826ba25467473bb06e0209cafbccad93ff976eb2df57dd7589f50c35102ce');
INSERT INTO "Login_credentials" ("Login_credentials_ID", "Login", "Password") VALUES (2, 'worker1', 'scrypt:32768:8:1$lAC4VNNEsfi2RIbO$b0582f8152be45a8e2ad0a047dd991e12f3837a998785f2b8784722f9bf2e44a6a91438665098d66858756acad5a7e3ad01ee5d436f946b1040aaa402c1cb382');
INSERT INTO "Login_credentials" ("Login_credentials_ID", "Login", "Password") VALUES (3, 'worker2', 'scrypt:32768:8:1$lAC4VNNEsfi2RIbO$b0582f8152be45a8e2ad0a047dd991e12f3837a998785f2b8784722f9bf2e44a6a91438665098d66858756acad5a7e3ad01ee5d436f946b1040aaa402c1cb382');
INSERT INTO "Login_credentials" ("Login_credentials_ID", "Login", "Password") VALUES (4, 'worker3', 'scrypt:32768:8:1$lAC4VNNEsfi2RIbO$b0582f8152be45a8e2ad0a047dd991e12f3837a998785f2b8784722f9bf2e44a6a91438665098d66858756acad5a7e3ad01ee5d436f946b1040aaa402c1cb382');
INSERT INTO "Login_credentials" ("Login_credentials_ID", "Login", "Password") VALUES (5, 'worker4', 'scrypt:32768:8:1$lAC4VNNEsfi2RIbO$b0582f8152be45a8e2ad0a047dd991e12f3837a998785f2b8784722f9bf2e44a6a91438665098d66858756acad5a7e3ad01ee5d436f946b1040aaa402c1cb382');
INSERT INTO "Employee" ("Employee_ID", "Name", "Surname", "Gender", "Salary", "Date_of_birth", "Phone_number", "Employee_status_ID", "Car_dealer_ID", "Login_credentials_ID") VALUES (1, 'Douglas', 'Thompson', 'M', 4043, '1974-08-23', '001-185-847-0477x8052', 2, 1, 1);
INSERT INTO "Employee" ("Employee_ID", "Name", "Surname", "Gender", "Salary", "Date_of_birth", "Phone_number", "Employee_status_ID", "Car_dealer_ID", "Login_credentials_ID") VALUES (2, 'Gabriel', 'Chapman', 'F', 7032, '1971-07-08', '(482)317-1067', 1, 2, 2);
INSERT INTO "Employee" ("Employee_ID", "Name", "Surname", "Gender", "Salary", "Date_of_birth", "Phone_number", "Employee_status_ID", "Car_dealer_ID", "Login_credentials_ID") VALUES (3, 'Robin', 'Munoz', 'M', 7259, '1997-08-28', '(780)229-0358', 2, 1, 3);
INSERT INTO "Employee" ("Employee_ID", "Name", "Surname", "Gender", "Salary", "Date_of_birth", "Phone_number", "Employee_status_ID", "Car_dealer_ID", "Login_credentials_ID") VALUES (4, 'Lisa', 'Perez', 'F', 3629, '1968-06-08', '001-091-504-7466x780', 2, 3, 4);
INSERT INTO "Employee" ("Employee_ID", "Name", "Surname", "Gender", "Salary", "Date_of_birth", "Phone_number", "Employee_status_ID", "Car_dealer_ID", "Login_credentials_ID") VALUES (5, 'Paul', 'Greene', 'M', 4799, '1993-09-03', '+1-034-809-1829x4614', 1, 2, 5);
INSERT INTO "Client" ("Client_ID", "Name", "Surname", "Gender", "Mail", "Phone") VALUES (1, 'Katherine', 'Stewart', 'F', 'unovak@stanley.com', '991-633-1956x6760');
INSERT INTO "Client" ("Client_ID", "Name", "Surname", "Gender", "Mail", "Phone") VALUES (2, 'Christine', 'Perez', 'M', 'james98@yahoo.com', '(633)152-2405x3069');
INSERT INTO "Client" ("Client_ID", "Name", "Surname", "Gender", "Mail", "Phone") VALUES (3, 'Jeffery', 'Johnson', 'F', 'blackjill@guerrero.info', '279-221-2846x017');
INSERT INTO "Client" ("Client_ID", "Name", "Surname", "Gender", "Mail", "Phone") VALUES (4, 'Timothy', 'Wilson', 'M', 'nathan66@griffin-rodriguez.biz', '001-716-896-3841x7393');
INSERT INTO "Client" ("Client_ID", "Name", "Surname", "Gender", "Mail", "Phone") VALUES (5, 'Catherine', 'Spencer', 'F', 'hkelly@cochran.com', '659-968-6878');
INSERT INTO "Position" ("Position_ID", "Name", "Min_salary", "Max_salary") VALUES (1, 'Salesperson', 4100, 5174);
INSERT INTO "Position" ("Position_ID", "Name", "Min_salary", "Max_salary") VALUES (2, 'Manager', 4115, 6320);
INSERT INTO "Position" ("Position_ID", "Name", "Min_salary", "Max_salary") VALUES (3, 'Technician', 3791, 5169);
INSERT INTO "Position_history" ("Position_history_ID", "Date_start", "Date_end", "Position_ID", "Employee_ID") VALUES (1, '2023-01-01', '2024-12-06', 2, 2);
INSERT INTO "Position_history" ("Position_history_ID", "Date_start", "Date_end", "Position_ID", "Employee_ID") VALUES (2, '2023-04-06', '2025-04-23', 1, 4);
INSERT INTO "Position_history" ("Position_history_ID", "Date_start", "Date_end", "Position_ID", "Employee_ID") VALUES (3, '2022-06-07', '2024-09-04', 3, 2);
INSERT INTO "Position_history" ("Position_history_ID", "Date_start", "Date_end", "Position_ID", "Employee_ID") VALUES (4, '2023-09-03', '2025-01-30', 3, 2);
INSERT INTO "Position_history" ("Position_history_ID", "Date_start", "Date_end", "Position_ID", "Employee_ID") VALUES (5, '2023-10-21', '2024-06-28', 3, 2);
INSERT INTO "Transaction_type" ("Transaction_type_ID", "Name") VALUES (1, 'Purchase');
INSERT INTO "Transaction_type" ("Transaction_type_ID", "Name") VALUES (2, 'Lease');
INSERT INTO "Invoice" ("Invoice_ID", "Status", "Issue_date", "NIP") VALUES (1, 'Issued', '2024-07-24', 2242422);
INSERT INTO "Invoice" ("Invoice_ID", "Status", "Issue_date", "NIP") VALUES (2, 'Issued', '2021-08-24', 6361226);
INSERT INTO "Invoice" ("Invoice_ID", "Status", "Issue_date", "NIP") VALUES (3, 'Issued', '2020-04-13', 3812601);
INSERT INTO "Invoice" ("Invoice_ID", "Status", "Issue_date", "NIP") VALUES (4, 'Issued', '2023-07-18', 3334724);
INSERT INTO "Invoice" ("Invoice_ID", "Status", "Issue_date", "NIP") VALUES (5, 'Issued', '2021-07-04', 1823918);
INSERT INTO "Transaction" ("Transaction_ID", "Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID") VALUES (1, '2025-01-11', 9143, 5, 5, 1, 1);
INSERT INTO "Transaction" ("Transaction_ID", "Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID") VALUES (2, '2025-01-05', 14904, 1, 3, 1, 2);
INSERT INTO "Transaction" ("Transaction_ID", "Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID") VALUES (3, '2025-04-10', 19186, 5, 2, 2, 3);
INSERT INTO "Transaction" ("Transaction_ID", "Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID") VALUES (4, '2025-03-12', 11830, 2, 4, 1, 4);
INSERT INTO "Transaction" ("Transaction_ID", "Date", "Value", "Client_ID", "Employee_ID", "Transaction_type_ID", "Invoice_ID") VALUES (5, '2025-04-23', 6646, 4, 1, 1, 5);
INSERT INTO "Car" ("Car_ID", "Brand", "Model", "Color", "Mileage", "Price", "Condition_ID", "Dealer_ID") VALUES (1, 'Mercedes', 'alone', 'Snow', 116045, 44559, 2, 2);
INSERT INTO "Car" ("Car_ID", "Brand", "Model", "Color", "Mileage", "Price", "Condition_ID", "Dealer_ID") VALUES (2, 'Toyota', 'get', 'LightYellow', 9192, 49448, 2, 3);
INSERT INTO "Car" ("Car_ID", "Brand", "Model", "Color", "Mileage", "Price", "Condition_ID", "Dealer_ID") VALUES (3, 'Moore-Lewis', 'build', 'Wheat', 137246, 37922, 2, 1);
INSERT INTO "Car" ("Car_ID", "Brand", "Model", "Color", "Mileage", "Price", "Condition_ID", "Dealer_ID") VALUES (4, 'BMW', 'data', 'DarkGoldenRod', 28953, 25562, 2, 2);
INSERT INTO "Car" ("Car_ID", "Brand", "Model", "Color", "Mileage", "Price", "Condition_ID", "Dealer_ID") VALUES (5, 'Long Inc', 'region', 'Crimson', 160760, 18506, 2, 2);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 1, 1, 9);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 1, 2, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 1, 3, 4);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 1, 4, 5);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 1, 5, 1);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 2, 1, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 2, 2, 10);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 2, 3, 8);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 2, 4, 8);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 2, 5, 4);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 3, 1, 8);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 3, 2, 9);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 3, 3, 4);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 3, 4, 3);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2023, 3, 5, 3);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 1, 1, 8);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 1, 2, 3);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 1, 3, 8);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 1, 4, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 1, 5, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 2, 1, 9);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 2, 2, 10);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 2, 3, 9);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 2, 4, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 2, 5, 5);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 3, 1, 6);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 3, 2, 9);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 3, 3, 10);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 3, 4, 0);
INSERT INTO "Employee_stats" ("Year", "Month", "Employee_ID", "Sales_sum") VALUES (2024, 3, 5, 8);