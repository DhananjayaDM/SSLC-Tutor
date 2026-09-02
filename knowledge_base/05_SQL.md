# SQL
## Data Definition and Data Types
SQL Data Definition Language (DDL) is a part of SQL used to define, modify, and remove database structures such as tables, indexes, views, and schemas.

DDL commands deal with the structure of the database, not the data itself.

DDL Commands
1. CREATE

Used to create database objects.

Syntax
SQL
1
CREATE TABLE Student
2
(
3
StudentID INT,
4
Name VARCHAR(30),
5
Marks INT
6
);
Show more lines
Example
SQL
1
CREATE TABLE Employee
2
(
3
EmpID INT,
4
EmpName VARCHAR(50),
5
Salary FLOAT
6
);
Show more lines
2. ALTER

Used to modify the structure of an existing table.

Add Column
SQL
1
ALTER TABLE Student
2
ADD Email VARCHAR(50);
Show more lines
Modify Column
SQL
1
ALTER TABLE Student
2
MODIFY Name VARCHAR(100);
Show more lines
3. DROP

Deletes a database object permanently.

SQL
1
DROP TABLE Student;
Show more lines
4. TRUNCATE

Removes all records from a table.

SQL
1
TRUNCATE TABLE Student;
Show more lines
Structure remains.
Data is deleted.
5. RENAME

Changes the name of a table.

SQL
1
RENAME TABLE Student TO Learner;
Show more lines
SQL Data Types
Definition

A Data Type specifies the type of data that can be stored in a column.

It determines:

Storage size
Valid values
Operations allowed
Numeric Data Types
INTEGER (INT)

Stores whole numbers.

SQL
1
Age INT
Show more lines

Examples:

Plain Text
1
10
2
25
3
100
4
 
Show more lines
SMALLINT

Stores smaller integer values.

SQL
1
Code SMALLINT
Show more lines
BIGINT

Stores very large integers.

SQL
1
Population BIGINT
Show more lines
DECIMAL(p,s)

Stores fixed-point numbers.

SQL
1
Salary DECIMAL(10,2)
Show more lines

Example:

Plain Text
1
25000.75
Show more lines
FLOAT

Stores floating-point values.

SQL
1
Percentage FLOAT
Show more lines

Example:

Plain Text
1
85.5
Show more lines
Character Data Types
CHAR

Fixed-length character string.

SQL
1
Gender CHAR(1)
Show more lines

Example:

Plain Text
1
M
2
F
3
``
Show more lines
VARCHAR

Variable-length character string.

SQL
1
Name VARCHAR(50)
Show more lines

Example:

Plain Text
1
Rahul
2
Anita
Show more lines
TEXT

Stores large text values.

SQL
1
Description TEXT
Show more lines
Date and Time Data Types
DATE

Stores date values.

SQL
1
DOB DATE
Show more lines

Example:

Plain Text
1
2025-01-15
Show more lines
TIME

Stores time values.

SQL
1
LoginTime TIME
Show more lines

Example:

Plain Text
1
10:30:45
Show more lines
DATETIME

Stores both date and time.

SQL
1
CreatedOn DATETIME
Show more lines

Example:

Plain Text
1
2025-01-15 10:30:45
Show more lines
Boolean Data Type

Stores logical values.

SQL
1
Active BOOLEAN
Show more lines

Values:

Plain Text
1
TRUE
2
FALSE
Show more lines
Example Table Using Different Data Types
SQL
1
CREATE TABLE Student
2
(
3
StudentID INT,
4
Name VARCHAR(50),
5
Age INT,
6
Marks FLOAT,
7
DOB DATE,
8
Active BOOLEAN
9
);
Show more lines
Advantages of Proper Data Types
Efficient storage management.
Improved query performance.
Better data validation.
Reduced data errors.
Improved database integrity.
DDL vs DML
DDL	DMLDefines database structure	Manipulates data
CREATE, ALTER, DROP	INSERT, UPDATE, DELETE
Works on schema	Works on records
Exam Point

SQL Data Definition Language (DDL) is used to create and modify database structures using commands such as CREATE, ALTER, DROP, TRUNCATE, and RENAME. SQL Data Types define the kind of data stored in columns and include Numeric (INT, FLOAT, DECIMAL), Character (CHAR, VARCHAR), Date/Time (DATE, TIME, DATETIME), and Boolean data types.

## Types of data base  Languages
Database languages are used to define, manipulate, retrieve, and control data in a database.

1. Data Definition Language (DDL)

Used to define and modify the structure of database objects.

Common Commands
SQL
1
CREATE
2
ALTER
3
DROP
4
TRUNCATE
5
RENAME
Show more lines
Example
SQL
1
CREATE TABLE Student
2
(
3
StudentID INT,
4
Name VARCHAR(30)
5
);
Show more lines
Functions
Create tables
Modify table structure
Delete database objects
Define database schema
2. Data Manipulation Language (DML)

Used to insert, update, and delete data in tables.

Common Commands
SQL
1
INSERT
2
UPDATE
3
DELETE
Show more lines
Example
SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul');
Show more lines
SQL
1
UPDATE Student
2
SET Name = 'Anita'
3
WHERE StudentID = 1;
Show more lines
SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
3
 
Show more lines
Functions
Add records
Modify records
Remove records
3. Data Query Language (DQL)

Used to retrieve data from the database.

Command
SQL
1
SELECT
Show more lines
Example
SQL
1
SELECT * FROM Student;
Show more lines
Functions
Retrieve records
Filter data
Generate reports
4. Data Control Language (DCL)

Used to control user access and permissions.

Commands
SQL
1
GRANT
2
REVOKE
Show more lines
Example
SQL
1
GRANT SELECT
2
ON Student
3
TO User1;
4
 
Show more lines
Functions
Security management
User authorization
Access control
5. Transaction Control Language (TCL)

Used to manage database transactions.

Commands
SQL
1
COMMIT
2
ROLLBACK
3
SAVEPOINT
Show more lines
Example
SQL
1
COMMIT;
Show more lines
Functions
Maintain data consistency
Recover from errors
Manage transactions
Summary Table
Language	Purpose	CommandsDDL	Defines database structure	CREATE, ALTER, DROP, TRUNCATE
DML	Manipulates data	INSERT, UPDATE, DELETE
DQL	Retrieves data	SELECT
DCL	Controls permissions	GRANT, REVOKE
TCL	Manages transactions	COMMIT, ROLLBACK, SAVEPOINT
Exam Point

The five types of database languages are:

DDL (Data Definition Language) – Defines database structure.
DML (Data Manipulation Language) – Inserts, updates, and deletes data.
DQL (Data Query Language) – Retrieves data using SELECT.
DCL (Data Control Language) – Manages access permissions.
TCL (Transaction Control Language) – Controls transactions.

## aggregate functions
Aggregate Functions are SQL functions used to perform calculations on a group of rows and return a single result.

They are commonly used with numerical data and often combined with the GROUP BY clause.

Common Aggregate Functions
1. COUNT()

Returns the number of rows.

Syntax
SQL
1
SELECT COUNT(*) FROM Student;
Show more lines
Example
StudentID	Name1	Rahul
2	Anita
3	Ravi
SQL
1
SELECT COUNT(*) FROM Student;
Show more lines
Output
Plain Text
1
3
Show more lines
2. SUM()

Returns the total sum of a column.

Syntax
SQL
1
SELECT SUM(Marks)
2
FROM Student;
Show more lines
Example
Marks80
90
70

Output:

Plain Text
1
240
Show more lines
3. AVG()

Returns the average value.

Syntax
SQL
1
SELECT AVG(Marks)
2
FROM Student;
Show more lines
Example
Marks80
90
70

Output:

Plain Text
1
80
Show more lines
4. MAX()

Returns the highest value.

Syntax
SQL
1
SELECT MAX(Marks)
2
FROM Student;
Show more lines

Output:

Plain Text
1
90
Show more lines
5. MIN()

Returns the smallest value.

Syntax
SQL
1
SELECT MIN(Marks)
2
FROM Student;
Show more lines

Output:

Plain Text
1
70
2
 
Show more lines
Aggregate Functions with GROUP BY
Example
SQL
1
SELECT DeptID,
2
AVG(Salary)
3
FROM Employee
4
GROUP BY DeptID;
Show more lines

This displays the average salary department-wise.

Aggregate Functions with WHERE Clause
SQL
1
SELECT AVG(Marks)
2
FROM Student
3
WHERE Marks > 50;
Show more lines

Calculates the average only for students scoring more than 50.

Aggregate Functions with HAVING Clause
SQL
1
SELECT DeptID,
2
AVG(Salary)
3
FROM Employee
4
GROUP BY DeptID
5
HAVING AVG(Salary) > 50000;
Show more lines

Displays departments whose average salary exceeds 50000.

Summary Table
Function	PurposeCOUNT()	Counts rows
SUM()	Calculates total
AVG()	Calculates average
MAX()	Finds largest value
MIN()	Finds smallest value
Advantages
Fast data summarization.
Useful for statistical calculations.
Works with GROUP BY.
Helps in report generation.
Reduces manual calculations.
Exam Point

Aggregate Functions perform calculations on multiple rows and return a single value. The major aggregate functions are COUNT(), SUM(), AVG(), MAX(), and MIN().

## Constraints
Constraints are rules applied to database tables to maintain the accuracy, consistency, and integrity of data.

They prevent invalid data from being inserted, updated, or deleted.

Types of Constraints
1. Domain Constraint

Restricts the values that can be stored in a column.

Example
SQL
1
Marks INT CHECK(Marks >= 0 AND Marks <= 100)
2
``
Show more lines

Valid:

Plain Text
1
85
Show more lines

Invalid:

Plain Text
1
150
2
 
Show more lines
2. Key Constraint

Ensures uniqueness of records.

Primary Key
Uniquely identifies each record.
Cannot contain NULL values.
SQL
1
StudentID INT PRIMARY KEY
Show more lines

Example:

StudentID	Name1	Rahul
2	Anita

Invalid:

StudentID	Name1	Rahul
1	Anita
3. Entity Integrity Constraint

States that:

Plain Text
1
Primary Key cannot be NULL
Show more lines

Example:

SQL
1
StudentID = NULL
Show more lines

Not allowed.

4. Referential Integrity Constraint

Maintains consistency between related tables.

Example
SQL
1
Department
2
(
3
DeptID PRIMARY KEY
4
)
5
 
6
Employee
7
(
8
EmpID PRIMARY KEY,
9
DeptID REFERENCES Department(DeptID)
10
)
Show more lines

A foreign key value must exist in the referenced table.

5. NOT NULL Constraint

Ensures a column cannot contain NULL values.

SQL
1
Name VARCHAR(30) NOT NULL
2
``
Show more lines
6. UNIQUE Constraint

Ensures all values in a column are unique.

SQL
1
Email VARCHAR(50) UNIQUE
Show more lines

Example:

Plain Text
1
abc@gmail.com
2
xyz@gmail.com
Show more lines

Duplicates are not allowed.

7. CHECK Constraint

Restricts values based on a condition.

SQL
1
CHECK(Age >= 18)
Show more lines

Valid:

Plain Text
1
25
Show more lines

Invalid:

Plain Text
1
15
Show more lines
8. DEFAULT Constraint

Assigns a default value when no value is provided.

SQL
1
Status VARCHAR(10) DEFAULT 'Active'
Show more lines
Constraint Summary
Constraint	PurposeDomain Constraint	Restricts valid values
Key Constraint	Ensures uniqueness
Entity Integrity	Primary key cannot be NULL
Referential Integrity	Maintains table relationships
NOT NULL	Prevents NULL values
UNIQUE	Prevents duplicate values
CHECK	Enforces conditions
DEFAULT	Assigns default values
Advantages of Constraints
Maintain data integrity.
Prevent invalid data entry.
Improve database reliability.
Enforce business rules.
Ensure consistency among related tables.
Exam Point

Constraints are rules that enforce data integrity in a database. Major constraints are Domain Constraint, Key Constraint, Entity Integrity Constraint, Referential Integrity Constraint, NOT NULL, UNIQUE, CHECK, and DEFAULT Constraints.

## Queries
A Query is a request made to a database to retrieve, insert, update, delete, or manipulate data.

Queries are written using SQL (Structured Query Language) and allow users to interact with the database.

Purpose of Queries
Retrieve specific data.
Insert new records.
Update existing records.
Delete records.
Generate reports.
Filter and analyze data.
Types of Queries
1. Select Query

Used to retrieve data from a table.

Syntax
SQL
1
SELECT column_name
2
FROM table_name;
Show more lines
Example
SQL
1
SELECT * FROM Student;
Show more lines

Displays all records from the Student table.

2. Insert Query

Used to add new records.

Syntax
SQL
1
INSERT INTO table_name
2
VALUES (...);
Show more lines
Example
SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul', 90);
Show more lines
3. Update Query

Used to modify existing records.

Syntax
SQL
1
UPDATE table_name
2
SET column_name = value
3
WHERE condition;
4
``
Show more lines
Example
SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
Show more lines
4. Delete Query

Used to remove records.

Syntax
SQL
1
DELETE FROM table_name
2
WHERE condition;
Show more lines
Example
SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
Show more lines
Query Clauses
WHERE Clause

Filters records based on a condition.

SQL
1
SELECT * FROM Student
2
WHERE Marks > 80;
Show more lines
ORDER BY Clause

Sorts records.

SQL
1
SELECT * FROM Student
2
ORDER BY Marks DESC;
3
 
Show more lines
GROUP BY Clause

Groups records based on a column.

SQL
1
SELECT DeptID, AVG(Salary)
2
FROM Employee
3
GROUP BY DeptID;
Show more lines
HAVING Clause

Applies conditions on groups.

SQL
1
SELECT DeptID, AVG(Salary)
2
FROM Employee
3
GROUP BY DeptID
4
HAVING AVG(Salary) > 50000;
Show more lines
Aggregate Queries
COUNT()
SQL
1
SELECT COUNT(*)
2
FROM Student;
Show more lines
SUM()
SQL
1
SELECT SUM(Marks)
2
FROM Student*
Show more lines
AVG()
SQL
1
SELECT AVG*Marks)
2
FROM Student;
Show more lines
MAX()
SQL
1
SELECT MAX(Marks)
2
FROM St*dent;
Show more lines
MIN()
SQL
1
SELECT MIN(Marks)
2
FR*M Student;
Show more lines
Join Queries

Used to combine data from multiple tables.

Example
SQL
1
SE*ECT Student.Name,
2
Course.Co*rseName
3
FROM Student
4
JOIN Course
5
O* Student.CourseID = Course.CourseI*;
Show more lines
Nested Queries (Subqueries)

A query inside another query.

Example
SQL
1
SELECT Name
2
FROM Student
3
WHERE Mar*s >
4
(
5
SELECT AVG(Marks)
6
FR*M Student
7
);
Show more lines

Returns students scoring above average.

Advantages of Queries
Fast data retrieval.
Easy data manipulation.
Supports complex searches.
Generates useful reports.
Improves decision making.
Applications
Banking systems
Hospital databases
Library management
Student information systems
Inventory systems
E-commerce applications
Exam Point

A Query is a request made to a database to retrieve or manipulate data. Common query types are SELECT, INSERT, UPDATE, and DELETE. SQL clauses such as WHERE, ORDER BY, GROUP BY, and HAVING are used to filter, sort, group, and analyze data.

## Insert
The INSERT statement is used to add new records (rows) into a database table.

Syntax
Insert All Values
SQL
1
INSERT INTO table_name
2
VALUES (value1, value2, value3);
Show more lines
Example
SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul', 90);
Show more lines

Result:

StudentID	Name	Marks1	Rahul	90
Insert Specific Columns
Syntax
SQL
1
INSERT INTO table_name
2
(column1, column2, column3)
3
VALUES
4
(value1, value2, value3);
5
``
Show more lines
Example
SQL
1
INSERT INTO Student
2
(StudentID, Name)
3
VALUES
4
(2, 'Anita');
Show more lines
Insert Multiple Records
SQL
1
INSERT INTO Student
2
VALUES
3
(3, 'Ravi', 85),
4
(4, 'Priya', 92);
Show more lines
Constraints Checked During INSERT

Before inserting a record, DBMS verifies:

Domain Constraint
Primary Key Constraint
Entity Integrity Constraint
Referential Integrity Constraint
NOT NULL Constraint
UNIQUE Constraint
Example
SQL
1
StudentID INT PRIMARY KEY
Show more lines

Invalid:

SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul', 90);
3
 
4
INSERT INTO Student
5
VALUES (1, 'Anita', 85);
Show more lines

Reason:

Plain Text
1
Duplicate Primary Key
Show more lines
Advantages
Adds new records to tables.
Supports bulk data entry.
Maintains data integrity through constraints.
Easy and efficient data insertion.
Exam Point

INSERT is a DML (Data Manipulation Language) command used to add new records into a database table. It can insert complete rows, selected columns, or multiple rows at once.

## Delete
The DELETE statement is used to remove one or more records (rows) from a database table.

It is a Data Manipulation Language (DML) command.

Syntax
Delete Specific Record(s)
SQL
1
DELETE FROM table_name
2
WHERE condition;
Show more lines
Example
SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
Show more lines

Result:

The record with StudentID = 1 is removed.

Example Table

Before Deletion:

StudentID	Name	Marks1	Rahul	90
2	Anita	85
3	Ravi	80

Query:

SQL
1
DELETE FROM Student
2
WHERE StudentID = 2;
Show more lines

After Deletion:

StudentID	Name	Marks1	Rahul	90
3	Ravi	80
Delete All Records
SQL
1
DELETE FROM Student;
Show more lines
Result
All rows are removed.
Table structure remains unchanged.
DELETE with Multiple Conditions
SQL
1
DELETE FROM Employee
2
WHERE Salary < 20000;
Show more lines

Removes all employees whose salary is less than 20000.

Constraints During DELETE
Referential Integrity Constraint

Deleting a row may fail if it is referenced by a foreign key in another table.

Example

Department Table

SQL
1
DeptID
Show more lines

Employee Table

SQL
1
DeptID REFERENCES Department(DeptID)
Show more lines

If employees still belong to a department:

SQL
1
DELETE FROM Department
2
WHERE DeptID = 10;
Show more lines

may be rejected to maintain referential integrity.

DELETE vs TRUNCATE
DELETE	TRUNCATEDeletes selected rows or all rows	Deletes all rows
Can use WHERE clause	Cannot use WHERE clause
Slower	Faster
DML Command	DDL Command
Can be rolled back (depending on DBMS)	Usually cannot be rolled back
Example

DELETE:

SQL
1
DELETE FROM Student
2
WHERE Marks < 40;
Show more lines

TRUNCATE:

SQL
1
TRUNCATE TABLE Student;
Show more lines
Advantages
Removes unnecessary records.
Supports conditional deletion.
Maintains integrity through constraints.
More flexible than TRUNCATE.
Applications
Removing outdated records
Deleting terminated employee records
Cleaning unwanted data
Database maintenance
Exam Point

DELETE is a DML command used to remove records from a table. It can delete specific records using a WHERE clause or all records without affecting the table structure.

## Update Statements
The UPDATE statement is used to modify existing records in a database table.

It is a Data Manipulation Language (DML) command.

Syntax
Update Specific Record(s)
SQL
1
UPDATE table_name
2
SET column_name = value
3
WHERE condition;
Show more lines
Example
SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
Show more lines

This updates the marks of the student whose StudentID is 1.

Example Table
Before Update
StudentID	Name	Marks1	Rahul	90
2	Anita	85
3	Ravi	80

Query:

SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
4
 
Show more lines
After Update
StudentID	Name	Marks1	Rahul	95
2	Anita	85
3	Ravi	80
Update Multiple Columns
SQL
1
UPDATE Employee
2
SET Salary = 50000,
3
Department = 'IT'
4
WHERE EmpID = 101;
Show more lines

Updates both salary and department.

Update All Rows
SQL
1
UPDATE Student
2
SET Marks = 100;
Show more lines
Result

All students receive marks = 100.

⚠️ Use carefully because every record is modified.

UPDATE with Arithmetic Operations
SQL
1
UPDATE Employee
2
SET Salary = Salary + 5000
3
WHERE EmpID = 101;
Show more lines

Increases salary by 5000.

Constraints Checked During UPDATE

The DBMS verifies:

Domain Constraint
SQL
1
UPDATE Student
2
SET Marks = 150;
Show more lines

May fail if marks are restricted to:

Plain Text
1
0 – 100
Show more lines
Key Constraint
SQL
1
UPDATE Student
2
SET StudentID = 1;
3
 
Show more lines

Cannot create duplicate primary keys.

Entity Integrity Constraint

Primary key cannot become NULL.

SQL
1
UPDATE Student
2
SET StudentID = NULL;
Show more lines

Not allowed.

Referential Integrity Constraint

Foreign key references must remain valid.

Example:

SQL
1
UPDATE Employee
2
SET DeptID = 50;
3
``
Show more lines

Fails if Department 50 does not exist.

UPDATE vs INSERT vs DELETE
Command	PurposeINSERT	Add new records
UPDATE	Modify existing records
DELETE	Remove records
Example
SQL
1
INSERT → Add Student
2
UPDATE → Change Student Marks
3
DELETE → Remove Student
Show more lines
Advantages
Modifies existing data.
Supports conditional updates.
Allows updating multiple columns.
Maintains data integrity through constraints.
Applications
Updating employee salaries
Changing customer information
Modifying inventory records
Correcting database entries
Maintaining student records
Exam Point

UPDATE is a DML command used to modify existing records in a table. The SET clause specifies new values, while the WHERE clause determines which records are updated. Constraints such as Domain, Key, Entity Integrity, and Referential Integrity are checked during updates.

## Views
A View is a virtual table in a database whose contents are derived from one or more base tables. A view does not store data permanently; it displays data retrieved from underlying tables.

Views are used to simplify data access and improve security.

Syntax
Create a View
SQL
1
CREATE VIEW view_name AS
2
SELECT column1, column2
3
FROM table_name
4
WHERE condition;
Show more lines
Example
SQL
1
CREATE VIEW Student_View AS
2
SELECT StudentID, Name
3
FROM Student;
Show more lines
Example
Student Table
StudentID	Name	Marks1	Rahul	90
2	Anita	85

View:

SQL
1
CREATE VIEW Student_View AS
2
SELECT StudentID, Name
3
FROM Student;
Show more lines

Result:

StudentID	Name1	Rahul
2	Anita

Only selected columns are visible.

Types of Views
1. Simple View

Created from a single table.

SQL
1
CREATE VIEW Student_View AS
2
SELECT Name, Marks
3
FROM Student;
Show more lines
Characteristics
Based on one table.
Easier to maintain.
Often updatable.
2. Complex View

Created using multiple tables, joins, or aggregate functions.

SQL
1
CREATE VIEW Employee_Department AS
2
SELECT E.EmpName, D.DeptName
3
FROM Employee E
4
JOIN Department D
5
ON E.DeptID = D.DeptID;
Show more lines
Characteristics
Uses multiple tables.
May contain joins and aggregates.
Usually not updatable.
Updating a View

Example:

SQL
1
UPDATE Student_View
2
SET Name = 'Ravi'
3
WHERE StudentID = 1;
4
``
Show more lines

If the view is updatable, changes affect the original table.

Dropping a View
SQL
1
DROP VIEW Student_View;
Show more lines

Removes the view definition but does not affect the underlying table.

Advantages of Views
Provides data security.
Hides unnecessary information.
Simplifies complex queries.
Provides customized data presentation.
Supports data abstraction.
Applications
Restricting user access.
Report generation.
Data abstraction.
Presenting customized information to different users.
Example

Teacher View:

SQL
1
StudentID
2
Name
3
Marks
4
``
Show more lines

Accounts View:

SQL
1
StudentID
2
Name
3
FeeStatus
Show more lines

Different users see different data through views.

View vs Table
View	TableVirtual table	Physical table
Stores query definition	Stores actual data
Occupies little storage	Occupies storage space
Derived from tables	Contains data permanently
Exam Point

A View is a virtual table created from one or more database tables using a SELECT query. Views improve security, simplify queries, and provide customized access to data without storing duplicate information.

## Stored Procedures and Functions
Stored Procedure

A Stored Procedure is a collection of SQL statements stored in the database and executed as a single unit to perform a specific task.

Function

A Function is a database object that accepts parameters, performs operations, and returns a value.

Both are stored in the database and can be reused multiple times.

Stored Procedure
Characteristics
Stored permanently in the database.
Can contain multiple SQL statements.
Can accept input parameters.
Can return output parameters.
Improves performance and code reusability.
Syntax
SQL
1
CREATE PROCEDURE procedure_name
2
AS
3
BEGIN
4
SQL statements;
5
END;
6
 
Show more lines
Example
SQL
1
CREATE PROCEDURE ShowStudents
2
AS
3
BEGIN
4
SELECT * FROM Student;
5
END;
Show more lines
Execute Procedure
SQL
1
EXEC ShowStudents;
Show more lines
Advantages of Stored Procedures
Reduces code duplication.
Faster execution.
Improved security.
Easy maintenance.
Reusable business logic.
Function
Characteristics
Returns a value.
Can accept parameters.
Can be used inside SQL queries.
Suitable for calculations and validations.
Syntax
SQL
1
CREATE FUNCTION function_name(parameter)
2
RETURNS datatype
3
AS
4
BEGIN
5
RETURN value;
6
END;
Show more lines
Example
SQL
1
CREATE FUNCTION SquareNum(@x INT)
2
RETURNS INT
3
AS
4
BEGIN
5
RETURN @x * @x;
6
END;
7
``
Show more lines
Calling Function
SQL
1
SELECT dbo.SquareNum(5);
Show more lines
Output
Plain Text
1
25
Show more lines
Types of Functions
Scalar Function

Returns a single value.

Example:

SQL
1
SELECT dbo.SquareNum(5);
Show more lines

Output:

Plain Text
1
25
Show more lines
Aggregate Function

Performs calculations on multiple rows.

Examples:

SQL
1
COUNT()
2
SUM()
3
AVG()
4
MIN()
5
MAX()
Show more lines

Example:

SQL
1
SELECT AVG(Marks)
2
FROM Student;
Show more lines
Stored Procedure vs Function
Feature	Stored Procedure	FunctionReturns Value	Optional	Mandatory
Can Return Multiple Values	Yes	No
Used in SELECT Statement	No	Yes
Supports Output Parameters	Yes	No
Purpose	Complex operations	Calculations and value generation
Example Comparison
Stored Procedure
SQL
1
CREATE PROCEDURE GetStudents
2
AS
3
BEGIN
4
SELECT * FROM Student;
5
END;
Show more lines

Execution:

SQL
1
EXEC GetStudents;
Show more lines
Function
SQL
1
CREATE FUNCTION GetBonus(@salary INT)
2
RETURNS INT
3
AS
4
BEGIN
5
RETURN @salary * 10 / 100;
6
END;
Show more lines

Execution:

SQL
1
SELECT dbo.GetBonus(50000);
Show more lines
Applications
Stored Procedures
Banking systems
Payroll systems
Inventory management
Student management systems
Functions
Mathematical calculations
Data validation
Business rule implementation
Report generation
Advantages
Stored Procedures
Faster execution
Better security
Reduced network traffic
Centralized business logic
Functions
Reusable code
Easy calculations
Can be used inside queries
Simplifies SQL statements
Exam Point

Stored Procedure is a collection of SQL statements stored in the database and executed as a unit. Function is a database object that accepts parameters and returns a value. Stored Procedures are used for complex operations, whereas Functions are mainly used for calculations and value generation.

## Database Triggers
A Trigger is a special type of stored procedure that is automatically executed (fired) when a specified event occurs on a table or view.

Triggers are commonly used to:

Enforce business rules
Maintain data integrity
Audit database activities
Automatically update related tables
Characteristics of Triggers
Executed automatically by the DBMS.
Associated with a table or view.
Fired when an event occurs.
Cannot be called directly like a procedure.
Used for maintaining consistency and security.
Events that Activate Triggers
INSERT Trigger

Activated when a new record is inserted.

SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul', 90);
Show more lines
UPDATE Trigger

Activated when records are modified.

SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
Show more lines
DELETE Trigger

Activated when records are deleted.

SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
Show more lines
Syntax
SQL
1
CREATE TRIGGER trigger_name
2
ON table_name
3
AFTER INSERT
4
AS
5
BEGIN
6
SQL Statements
7
END;
Show more lines
Example: INSERT Trigger
SQL
1
CREATE TRIGGER Student_Insert
2
ON Student
3
AFTER INSERT
4
AS
5
BEGIN
6
PRINT 'New Student Record Added'
7
END;
Show more lines

When a new student record is inserted, the trigger executes automatically.

Example: UPDATE Trigger
SQL
1
CREATE TRIGGER Student_Update
2
ON Student
3
AFTER UPDATE
4
AS
5
BEGIN
6
PRINT 'Student Record Updated'
7
END;
Show more lines
Example: DELETE Trigger
SQL
1
CREATE TRIGGER Student_Delete
2
ON Student
3
AFTER DELETE
4
AS
5
BEGIN
6
PRINT 'Student Record Deleted'
7
END;
Show more lines
Types of Triggers
1. BEFORE Trigger
Executes before the operation.
Used for validation.
Plain Text
1
BEFORE INSERT
2
BEFORE UPDATE
3
BEFORE DELETE
Show more lines
2. AFTER Trigger
Executes after the operation is completed.
Plain Text
1
AFTER INSERT
2
AFTER UPDATE
3
AFTER DELETE
4
 
Show more lines
3. INSTEAD OF Trigger
Executes in place of the actual operation.
Commonly used with views.
Plain Text
1
INSTEAD OF INSERT
2
INSTEAD OF UPDATE
3
INSTEAD OF DELETE
Show more lines
Applications of Triggers
Audit Logging

Track database changes.

Plain Text
1
Insert Log
2
Update Log
3
Delete Log
Show more lines
Maintaining Integrity

Enforce business rules automatically.

Security

Monitor unauthorized operations.

Automatic Updates

Update related tables when changes occur.

Trigger vs Stored Procedure
Trigger	Stored ProcedureExecutes automatically	Executed explicitly
Event-driven	User/application driven
Associated with table or view	Independent database object
Cannot be called directly	Can be called directly
Advantages of Triggers
Automatic execution.
Improves data integrity.
Enforces business rules.
Supports auditing.
Reduces application code.
Disadvantages of Triggers
Difficult to debug.
Additional processing overhead.
Complex trigger chains may affect performance.
Exam Point

A Trigger is a database object that automatically executes when an INSERT, UPDATE, or DELETE operation occurs on a table or view. Triggers are used for enforcing business rules, maintaining data integrity, auditing, and automating database operations.

## SQL Injection
SQL Injection (SQLi) is a security attack in which an attacker inserts malicious SQL statements into user input fields to manipulate a database.

It occurs when user input is not properly validated before being used in SQL queries.

How SQL Injection Works

Consider a login query:

SQL
1
SELECT *
2
FROM Users
3
WHERE Username = 'admin'
4
AND Password = '1234';
Show more lines

If the application directly accepts user input, an attacker may enter:

Plain Text
1
Username : admin
2
Password : ' OR '1'='1
Show more lines

Resulting query:

SQL
1
SELECT *
2
FROM Users
3
WHERE Username = 'admin'
4
AND Password = '' OR '1'='1';
Show more lines

Since:

SQL
1
'1'='1'
Show more lines

is always true, authentication may be bypassed.

Causes of SQL Injection
Improper input validation.
Dynamic SQL query construction.
Lack of parameterized queries.
Poor database security practices.
Weak application design.
Types of SQL Injection
1. Authentication Bypass

Used to bypass login pages.

Example:

SQL
1
' OR '1'='1
Show more lines
2. Union-Based SQL Injection

Uses the UNION operator to retrieve data from other tables.

Example:

SQL
1
UNION SELECT username, password FROM Users
Show more lines
3. Error-Based SQL Injection

Uses database error messages to obtain information about database structure.

4. Blind SQL Injection

The attacker does not see database errors directly but infers information from application responses.

Boolean-Based Blind SQLi
SQL
1
AND 1=1
2
``
Show more lines

vs

SQL
1
AND 1=2
Show more lines
Time-Based Blind SQLi

Uses delays to infer information.

Effects of SQL Injection
Unauthorized access to data.
Data theft.
Data modification.
Data deletion.
Bypass of authentication.
Complete database compromise.
Example
Vulnerable Code
PHP
1
$query =
2
"SELECT * FROM Users
3
WHERE username = '$user'
4
AND password = '$pass'";
Show more lines

An attacker can modify the query through input.

Prevention Techniques
1. Parameterized Queries (Prepared Statements)

Use placeholders instead of directly inserting user input.

Example:

SQL
1
SELECT *
2
FROM Users
3
WHERE Username = ?
4
AND Password = ?
Show more lines
2. Input Validation

Accept only valid input.

Example:

Plain Text
1
Allow letters and digits only.
2
``
Show more lines
3. Stored Procedures

Use predefined procedures instead of dynamic SQL.

4. Least Privilege Principle

Grant minimum database permissions required.

5. Escape Special Characters

Handle characters such as:




properly.

Advantages of Prevention
Improved security.
Protection of sensitive data.
Reduced risk of database compromise.
Improved application reliability.
SQL Injection vs Normal Query
Normal Query	SQL InjectionValid user input	Malicious input
Intended database operation	Unauthorized database manipulation
Safe execution	Security vulnerability
Applications of SQL Injection Awareness
Secure web development
Banking systems
E-commerce websites
Government applications
Healthcare systems
Enterprise software
Exam Point

SQL Injection is a database security attack in which malicious SQL code is inserted through user input to manipulate a database. It can be prevented using parameterized queries, input validation, stored procedures, and proper access control.
