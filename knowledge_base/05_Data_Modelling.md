# Data Modelling
## Entity-Relationship Diagram
An Entity-Relationship (ER) Diagram is a graphical representation of entities, attributes, and relationships in a database. It is used during database design to model the data requirements of an organization.

The ER Model was proposed by Peter Chen in 1976.

Purpose of ER Diagram
Helps in database design.
Represents real-world objects and their relationships.
Simplifies database development.
Provides a clear visual representation of data.
Components of ER Diagram
1. Entity

An Entity is a real-world object, person, place, or thing about which data is stored.

Examples
Plain Text
1
Student
2
Employee
3
Department
4
Book
5
Customer
Show more lines
Representation
Plain Text
1
Rectangle
Show more lines

Example:

Plain Text
1
+---------+
2
| Student |
3
+---------+
Show more lines
2. Attribute

An Attribute describes the properties of an entity.

Example

For Student:

Plain Text
1
RollNo
2
Name
3
Age
4
Marks
Show more lines
Representation
Plain Text
1
Oval
Show more lines

Example:

Plain Text
1
Name
2
|
3
Student
Show more lines
Types of Attributes
Simple Attribute

Cannot be divided further.

Example:

Plain Text
1
Age
2
Gender
Show more lines
Composite Attribute

Can be divided into sub-parts.

Example:

Plain Text
1
Name
2
├─ First Name
3
└─ Last Name
Show more lines
Single-Valued Attribute

Contains only one value.

Example:

Plain Text
1
Roll Number
Show more lines
Multi-Valued Attribute

Can have multiple values.

Example:

Plain Text
1
Phone Numbers
Show more lines
Derived Attribute

Obtained from another attribute.

Example:

Plain Text
1
Age derived from Date of Birth
Show more lines
3. Relationship

A Relationship represents an association between entities.

Example
Plain Text
1
Student Enrolls Course
Show more lines
Representation
Plain Text
1
Diamond Shape
Show more lines

Example:

Plain Text
1
Student ◇ Enrolls ◇ Course
Show more lines
Types of Relationships
One-to-One (1:1)

One entity is related to only one entity.

Example:

Plain Text
1
Person ↔ Passport
Show more lines
One-to-Many (1:M)

One entity is related to many entities.

Example:

Plain Text
1
Department → Employees
Show more lines

One department can have many employees.

Many-to-One (M:1)

Many entities related to one entity.

Example:

Plain Text
1
Employees → Department
Show more lines
Many-to-Many (M:N)

Many entities related to many entities.

Example:

Plain Text
1
Students ↔ Courses
Show more lines

A student can study many courses and a course can have many students.

ER Diagram Example
Student-Course Database
Plain Text
1
+---------+ Enrolls +---------+
2
| Student | --------------------- | Course |
3
+---------+ +---------+
4
| |
5
RollNo CourseID
6
| |
7
Name CourseName
Show more lines
Cardinality
Definition

Cardinality specifies the number of entities participating in a relationship.

Types
Plain Text
1
1:1
2
1:M
3
M:1
4
M:N
Show more lines

Example:

Plain Text
1
Student ↔ Course = M:N
Show more lines
Participation Constraints
Total Participation

Every entity must participate.

Example:

Plain Text
1
Every employee belongs to a department.
Show more lines
Partial Participation

Participation is optional.

Example:

Plain Text
1
Some employees may not manage projects.
Show more lines
Advantages of ER Diagram
Easy to understand.
Provides visual database design.
Reduces design errors.
Improves communication between users and developers.
Helps create relational database schemas.
Applications
Database Design
Banking Systems
Hospital Management Systems
Library Systems
University Databases
Inventory Management
ER Diagram vs Relational Model
ER Model	Relational ModelGraphical representation	Table representation
Used during design	Used during implementation
Entities and relationships	Tables and keys
High-level model	Logical model
Exam Point

An Entity-Relationship (ER) Diagram is a graphical representation of entities, attributes, and relationships used for database design. The main components are Entity, Attribute, and Relationship. Common relationship types are 1:1, 1:M, M:1, and M:N.

## Relational Model – Constraints, Languages, Design, and Programming
The Relational Model is a database model in which data is stored in the form of tables (relations) consisting of rows and columns. It was proposed by E. F. Codd.

Components
Relation (Table)

A table used to store data.

Example:

StudentID	Name	Marks1	Rahul	90
2	Anita	85
Tuple

A row in a table.

Example:

Plain Text
1
(1, Rahul, 90)
Show more lines
Attribute

A column in a table.

Example:

Plain Text
1
StudentID
2
Name
3
Marks
4
 
Show more lines
Domain

A set of permitted values for an attribute.

Example:

Plain Text
1
Marks → 0 to 100
Show more lines
Constraints in Relational Model

Constraints enforce data correctness and integrity.

1. Domain Constraint

Values must belong to the specified domain.

Example:

SQL
1
Marks INT CHECK(Marks >= 0 AND Marks <= 100)
2
 
Show more lines
2. Key Constraint

A key uniquely identifies a record.

Primary Key
SQL
1
StudentID
2
 
Show more lines

Properties:

Unique
Not NULL

Example:

SQL
1
StudentID INT PRIMARY KEY
Show more lines
Candidate Key

A minimal set of attributes that uniquely identifies tuples.

Example:

Plain Text
1
StudentID
2
Email
Show more lines
Alternate Key

Candidate keys not chosen as primary key.

Super Key

Any set of attributes that uniquely identifies tuples.

Example:

Plain Text
1
StudentID
2
StudentID + Name
Show more lines
3. Entity Integrity Constraint

Primary key values cannot be NULL.

Example:

SQL
1
StudentID INT PRIMARY KEY
Show more lines

Valid:

Plain Text
1
1
2
2
3
3
Show more lines

Invalid:

Plain Text
1
NULL
Show more lines
4. Referential Integrity Constraint

Ensures consistency between related tables.

Example:

SQL
1
Department(
2
DeptID PRIMARY KEY
3
)
4
 
5
Employee(
6
EmpID PRIMARY KEY,
7
DeptID REFERENCES Department(DeptID)
8
)
Show more lines

A foreign key value must exist in the referenced table.

Relational Database Languages
Data Definition Language (DDL)

Used to define database structures.

Commands:

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
``
Show more lines

Example:

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
Data Manipulation Language (DML)

Used to modify data.

Commands:

SQL
1
INSERT
2
UPDATE
3
DELETE
Show more lines

Example:

SQL
1
INSERT INTO Student
2
VALUES(1,'Rahul');
Show more lines
Data Query Language (DQL)

Used to retrieve data.

Command:

SQL
1
SELECT
Show more lines

Example:

SQL
1
SELECT * FROM Student;
Show more lines
Data Control Language (DCL)

Used for permissions and security.

Commands:

SQL
1
GRANT
2
REVOKE
Show more lines
Transaction Control Language (TCL)

Used to manage transactions.

Commands:

SQL
1
COMMIT
2
ROLLBACK
3
SAVEPOINT
Show more lines
Relational Database Design
Definition

Database design is the process of organizing data into tables to minimize redundancy and improve integrity.

Design Steps
1. Requirement Analysis

Identify:

Entities
Attributes
Relationships

Example:

Plain Text
1
Student
2
Course
3
Faculty
Show more lines
2. ER Modeling

Create Entity-Relationship Diagram.

Example:

Plain Text
1
Student ---- Enrolls ---- Course
Show more lines
3. Convert ER Model to Relations

Example:

SQL
1
STUDENT
2
(
3
StudentID,
4
Name
5
)
6
 
7
COURSE
8
(
9
CourseID,
10
CourseName
11
)
Show more lines
4. Normalization

Used to remove redundancy and anomalies.

First Normal Form (1NF)
No repeating groups.
Atomic values.
Second Normal Form (2NF)
Remove partial dependency.
Third Normal Form (3NF)
Remove transitive dependency.
Relational Database Programming
Definition

Relational Database Programming involves writing SQL statements to create, manipulate, and retrieve data.

SQL Programming Examples
Create Table
SQL
1
CREATE TABLE Student
2
(
3
StudentID INT PRIMARY KEY,
4
Name VARCHAR(30),
5
Marks INT
6
);
Show more lines
Insert Data
SQL
1
INSERT INTO Student
2
VALUES(1,'Rahul',90);
Show more lines
Retrieve Data
SQL
1
SELECT * FROM Student;
Show more lines
Update Data
SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
Show more lines
Delete Data
SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
3
 
Show more lines
Advantages of Relational Model
Simple table structure.
Easy querying using SQL.
Data independence.
Reduced redundancy.
High data integrity.
Flexible database design.
Applications
Banking Systems
University Databases
Hospital Management Systems
Inventory Systems
E-Commerce Applications
Government Information Systems
Exam Point

The Relational Model stores data in tables called relations. Data integrity is maintained using Domain, Key, Entity Integrity, and Referential Integrity constraints. Database operations are performed using DDL, DML, DQL, DCL, and TCL commands, while good database design uses ER modeling and normalization techniques.

## Relational Database Schemes
A Relational Database Schema is the logical structure of a relational database. It describes:

Relations (tables)
Attributes (columns)
Domains
Keys
Relationships among tables

A schema acts as the blueprint of a relational database.

General Representation

A relation schema is written as:

Plain Text
1
Relation_Name(Attribute1, Attribute2, Attribute3, ...)
2
``
Show more lines
Example
Plain Text
1
STUDENT(StudentID, Name, Age, Marks)
Show more lines

Where:

STUDENT → Relation Schema
StudentID, Name, Age, Marks → Attributes
Relation Schema vs Relation Instance
Relation Schema

Defines the structure.

Example:

Plain Text
1
STUDENT(StudentID, Name, Marks)
Show more lines
Relation Instance

Actual data stored in the table.

StudentID	Name	Marks1	Rahul	90
2	Anita	85
Types of Schemas in Relational Databases
Student Schema
Plain Text
1
STUDENT(
2
StudentID,
3
Name,
4
Age,
5
Marks
6
)
Show more lines
Course Schema
Plain Text
1
COURSE(
2
CourseID,
3
CourseName,
4
Credits
5
)
Show more lines
Enrollment Schema
Plain Text
1
ENROLLMENT(
2
StudentID,
3
CourseID
4
)
Show more lines
Components of Relational Schema
Relation Name

Name of the table.

Example:

Plain Text
1
STUDENT
Show more lines
Attributes

Columns of the table.

Example:

Plain Text
1
StudentID
2
Name
3
Marks
4
 
Show more lines
Domain

Allowed values of an attribute.

Example:

Plain Text
1
Marks : 0–100
2
 
Show more lines
Keys

Used to uniquely identify tuples.

Primary Key
Plain Text
1
StudentID
Show more lines
Foreign Key
Plain Text
1
CourseID
Show more lines

references another table.

Example Database Schema
Department Relation
Plain Text
1
DEPARTMENT(
2
DeptID,
3
DeptName
4
)
Show more lines
Employee Relation
Plain Text
1
EMPLOYEE(
2
EmpID,
3
EmpName,
4
DeptID
5
)
Show more lines

Relationship:

Plain Text
1
DeptID in EMPLOYEE
2
references
3
DeptID in DEPARTMENT
4
 
Show more lines
Mapping ER Diagram to Relational Schema
ER Model
Plain Text
1
Student ---- Enrolls ---- Course
Show more lines
Relational Schema
Plain Text
1
STUDENT(
2
StudentID,
3
Name
4
)
5
 
6
COURSE(
7
CourseID,
8
CourseName
9
)
10
 
11
ENROLLMENT(
12
StudentID,
13
CourseID
14
)
Show more lines
Schema Notation

A schema is often represented as:

Plain Text
1
R(A1, A2, A3, ..., An)
Show more lines

Where:

R = Relation Name
A1, A2, A3 ... = Attributes

Example:

Plain Text
1
EMPLOYEE(EmpID, Name, Salary)
Show more lines
Advantages of Relational Schemas
Clear database design.
Easy data organization.
Supports normalization.
Reduces redundancy.
Improves integrity and consistency.
Simplifies database maintenance.
Applications
Banking databases
Library management systems
Student information systems
Hospital databases
Inventory management systems
E-commerce databases
Example
Plain Text
1
STUDENT(
2
StudentID PRIMARY KEY,
3
Name,
4
Age
5
)
6
 
7
COURSE(
8
CourseID PRIMARY KEY,
9
CourseName
10
)
11
 
12
ENROLLMENT(
13
StudentID,
14
CourseID
15
)
Show more lines

This schema represents:

Students
Courses
Student-course enrollment relationship
Schema vs Instance
Schema	InstanceStructure of database	Actual data
Changes rarely	Changes frequently
Blueprint	Current database contents
Defined during design	Exists during operation
Exam Point

A Relational Database Schema is the logical design of a relational database that defines tables, attributes, domains, keys, and relationships. It serves as a blueprint for storing and organizing data in a relational database system.

## Update Operations and  constraints
Update Operations are operations used to modify the contents of a database. They allow insertion, deletion, and modification of data stored in tables.

Types of Update Operations
1. Insert Operation

Used to add new records (tuples) to a relation.

Example:

SQL
1
INSERT INTO Student
2
VALUES (1, 'Rahul', 90);
3
``
Show more lines

Result:

StudentID	Name	Marks1	Rahul	90
Constraint Check During Insertion
Domain constraints must be satisfied.
Primary key must be unique.
Foreign key must reference an existing tuple.
2. Delete Operation

Used to remove records from a relation.

Example:

SQL
1
DELETE FROM Student
2
WHERE StudentID = 1;
Show more lines
Constraint Issues

Deleting a record may violate:

Referential Integrity Constraints
Foreign Key Constraints

Example:

Plain Text
1
Department(DeptID)
2
Employee(DeptID)
3
 
Show more lines

Deleting a Department record while employees still reference it may cause an integrity violation.

3. Update (Modify) Operation

Used to change existing data.

Example:

SQL
1
UPDATE Student
2
SET Marks = 95
3
WHERE StudentID = 1;
Show more lines
Constraint Issues

Updates must maintain:

Domain validity
Key uniqueness
Referential integrity
Constraints
Definition

Constraints are rules enforced on database data to maintain accuracy, consistency, and integrity.

Types of Constraints
1. Domain Constraint

Restricts attribute values to a valid domain.

Example:

SQL
1
Marks INT CHECK(Marks >= 0 AND Marks <= 100)
Show more lines

Valid:

Plain Text
1
Marks = 85
Show more lines

Invalid:

Plain Text
1
Marks = 150
Show more lines
2. Key Constraint

Ensures uniqueness of records.

Primary Key
SQL
1
StudentID INT PRIMARY KEY
Show more lines

Properties:

Unique
Cannot be NULL

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
2
 
Show more lines

Not allowed.

4. Referential Integrity Constraint

Maintains consistency between related tables.

Department Table

Plain Text
1
DeptID
Show more lines

Employee Table

Plain Text
1
EmpID
2
DeptID
Show more lines

Foreign key:

SQL
1
DeptID REFERENCES Department(DeptID)
Show more lines

An employee cannot reference a department that does not exist.

5. NOT NULL Constraint

Ensures a field cannot contain NULL values.

SQL
1
Name VARCHAR(30) NOT NULL
Show more lines
6. UNIQUE Constraint

Ensures all values in a column are different.

SQL
1
Email VARCHAR(50) UNIQUE
2
 
Show more lines
7. CHECK Constraint

Restricts values according to a condition.

SQL
1
CHECK (Age >= 18)
Show more lines
8. DEFAULT Constraint

Assigns a default value.

SQL
1
Status VARCHAR(10) DEFAULT 'Active'
Show more lines
Update Anomalies

Poor database design may cause anomalies.

1. Insertion Anomaly

Unable to insert data without inserting unrelated information.

2. Deletion Anomaly

Deleting one record may unintentionally remove useful information.

3. Update Anomaly

Updating data in one place but not others causes inconsistency.

Constraint Enforcement During Updates
Operation	Constraints CheckedINSERT	Domain, Key, Entity Integrity, Referential Integrity
DELETE	Referential Integrity
UPDATE	Domain, Key, Referential Integrity
Advantages of Constraints
Maintain data accuracy.
Improve consistency.
Prevent invalid data entry.
Enforce business rules.
Improve database reliability.
Exam Point

Update Operations include INSERT, DELETE, and UPDATE. Constraints are rules that enforce database integrity. The main constraints are Domain Constraint, Key Constraint, Entity Integrity Constraint, Referential Integrity Constraint, NOT NULL, UNIQUE, CHECK, and DEFAULT Constraints.

## Relational Algebra and Relational Calculus
Relational Algebra is a procedural query language used in relational databases. It specifies how to retrieve data from one or more relations (tables).

Procedural language
Operates on relations
Produces a relation as output
Foundation of SQL
Basic Operations of Relational Algebra
1. Selection (σ)

Selects rows that satisfy a condition.

Syntax
Plain Text
1
σ condition (Relation)
Show more lines
Example
Plain Text
1
σ Marks > 80 (Student)
Show more lines

Returns students with marks greater than 80.

2. Projection (π)

Selects specific columns.

Syntax
Plain Text
1
π Attribute_List (Relation)
Show more lines
Example
Plain Text
1
π Name, Marks (Student)
Show more lines

Returns only Name and Marks columns.

3. Union (∪)

Combines tuples from two relations.

Syntax
Plain Text
1
R ∪ S
Show more lines

Conditions:

Same number of attributes
Compatible domains
4. Set Difference (-)

Returns tuples present in one relation but not in another.

Example
Plain Text
1
R - S
Show more lines
5. Intersection (∩)

Returns common tuples.

Plain Text
1
R ∩ S
Show more lines
6. Cartesian Product (×)

Combines each tuple of one relation with all tuples of another.

Plain Text
1
R × S
2
 
Show more lines
7. Join (⨝)

Combines related tuples from two tables.

Example
Plain Text
1
Student ⨝ Enrollment
Show more lines

Types:

Theta Join
Equi Join
Natural Join
8. Division (÷)

Used for “for all” type queries.

Example:

Plain Text
1
Student ÷ Course
2
``
Show more lines
Advantages of Relational Algebra
Mathematical foundation of DBMS.
Easy query optimization.
Forms the basis of SQL.
Simple and precise.
Relational Calculus
Definition

Relational Calculus is a non-procedural query language that specifies what data is required rather than how to retrieve it.

Non-procedural language
Based on predicate logic
Describes desired result
User specifies conditions
Types of Relational Calculus
1. Tuple Relational Calculus (TRC)

Variables represent tuples.

Syntax
Plain Text
1
{ t | Condition(t) }
Show more lines
Example
Plain Text
1
{ t | t ∈ Student AND t.Marks > 80 }
Show more lines

Returns students with marks above 80.

2. Domain Relational Calculus (DRC)

Variables represent attribute values.

Syntax
Plain Text
1
{ <x, y> | Condition(x, y) }
Show more lines
Example
Plain Text
1
{ <Name, Marks> |
2
Student(Name, Marks)
3
AND Marks > 80 }
Show more lines
Relational Algebra vs Relational Calculus
Relational Algebra	Relational CalculusProcedural language	Non-procedural language
Specifies how to retrieve data	Specifies what data is required
Uses operations like Selection and Projection	Uses logical predicates
Easier for query optimization	Easier for expressing conditions
Foundation for execution strategies	Foundation for query specification
Example Comparison
Find students with marks above 80

Relational Algebra

Plain Text
1
σ Marks > 80 (Student)
Show more lines

Tuple Relational Calculus

Plain Text
1
{ t | t ∈ Student AND t.Marks > 80 }
Show more lines

Domain Relational Calculus

Plain Text
1
{ <Name, Marks> |
2
Student(Name, Marks)
3
AND Marks > 80 }
Show more lines
Advantages of Relational Calculus
Easier query expression.
Based on mathematical logic.
Flexible query formulation.
Useful in theoretical database studies.
Exam Point

Relational Algebra is a procedural query language that specifies how data is retrieved using operations such as Selection, Projection, Union, Difference, Join, and Division. Relational Calculus is a non-procedural query language that specifies what data is required using logical predicates. Relational Calculus is of two types: Tuple Relational Calculus (TRC) and Domain Relational Calculus (DRC).
