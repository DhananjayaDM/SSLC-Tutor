# Database System concepts and Architecture
## Data Models
A Data Model is a collection of concepts used to describe the structure of a database, the relationships among data, and the operations that can be performed on the data.

It acts as a blueprint for designing a database.

Need for Data Models
Represent data in an organized manner.
Define relationships among data.
Simplify database design.
Improve data consistency.
Help users understand database structure.
Types of Data Models
1. Hierarchical Data Model
Definition

Data is organized in the form of a tree structure.

Parent-child relationship.
One parent can have many children.
One child can have only one parent.
Example
Plain Text
1
Company
2
|
3
+-- Department
4
|
5
+-- Employee
Show more lines
Advantages
Simple structure.
Fast data access.
Disadvantages
Difficult to represent many-to-many relationships.
Less flexible.
2. Network Data Model
Definition

Data is organized as a graph structure.

A record can have multiple parent records.
Supports many-to-many relationships.
Example
Plain Text
1
Student
2
|
3
Enrolls
4
|
5
Course
Show more lines

A student can enroll in many courses, and a course can have many students.

Advantages
Flexible.
Efficient relationship representation.
Disadvantages
Complex design.
Difficult maintenance.
3. Relational Data Model
Definition

Data is stored in the form of tables (relations).

Each table consists of:

Rows (Tuples)
Columns (Attributes)
Example

Student Table

ID	Name	Marks1	Rahul	90
2	Anita	85
Advantages
Easy to understand.
Easy querying using SQL.
Reduces data redundancy.
Disadvantages
Performance may decrease for very large databases.
4. Entity Relationship (ER) Model
Definition

A high-level conceptual model used for database design.

Components
Entity

Real-world object.

Example:

Plain Text
1
Student
2
Employee
3
Book
Show more lines
Attribute

Property of an entity.

Example:

Plain Text
1
Student → RollNo, Name, Age
Show more lines
Relationship

Association between entities.

Example:

Plain Text
1
Student ---- Enrolls ---- Course
Show more lines
Advantages
Easy database design.
Provides clear visualization.
5. Object-Oriented Data Model
Definition

Data is represented as objects, similar to Object-Oriented Programming.

Features
Objects
Classes
Inheritance
Encapsulation
Example
C++
1
class Student
2
{
3
int id;
4
string name;
5
};
Show more lines
Advantages
Handles complex data.
Reusability through inheritance.
Disadvantages
More complex than relational model.
6. Object-Relational Data Model
Definition

Combination of:

Relational Model
Object-Oriented Model
Features
Tables with object capabilities.
Supports complex data types.
Advantages
Flexibility.
Better handling of multimedia and complex data.
Comparison of Data Models
Data Model	StructureHierarchical	Tree
Network	Graph
Relational	Tables
ER Model	Entity-Relationship Diagram
Object-Oriented	Objects and Classes
Object-Relational	Tables + Objects
Advantages of Data Models
Better database organization.
Improved data consistency.
Easier database design.
Reduced redundancy.
Efficient data retrieval.
Exam Point

A Data Model is a collection of concepts used to describe the structure, relationships, and constraints of data in a database. Major data models are Hierarchical, Network, Relational, ER, Object-Oriented, and Object-Relational Data Models.

## Schemas
A Schema is the overall logical structure or design of a database. It describes how data is organized, the tables present, their attributes, relationships, and constraints.

A schema acts as a blueprint of the database.

Characteristics of Schema
Defines the structure of the database.
Changes very rarely.
Created during database design.
Describes tables, fields, relationships, and constraints.
Independent of actual data.
Example

Student Table:

RollNo	Name	Marks1	Rahul	90
2	Anita	85

Schema:

Plain Text
1
STUDENT
2
(
3
RollNo INT,
4
Name VARCHAR(30),
5
Marks INT
6
)
Show more lines
Types of Schemas
1. Physical Schema
Definition

Describes how data is actually stored in the storage device.

It includes:

Storage structure
File organization
Indexing methods
Access paths
Example
Plain Text
1
Student records stored in a B-Tree index
Show more lines
Characteristics
Lowest level schema.
Concerned with physical storage.
Visible mainly to database administrators.
2. Logical Schema (Conceptual Schema)
Definition

Describes the logical structure of the entire database.

It includes:

Tables
Attributes
Relationships
Constraints
Example
Plain Text
1
STUDENT
2
(
3
RollNo,
4
Name,
5
Marks
6
)
Show more lines
Characteristics
Most important schema.
Describes what data is stored.
Independent of physical storage.
3. View Schema (External Schema)
Definition

Describes how different users view the database.

Different users may see different parts of the database.

Example

Teacher View:

Plain Text
1
RollNo
2
Name
3
Marks
Show more lines

Accounts Section View:

Plain Text
1
RollNo
2
Name
3
Fee_Status
Show more lines
Characteristics
Highest level schema.
User-specific.
Improves security.
Three Schema Architecture
Plain Text
1
External Schema
2
↓
3
Conceptual Schema
4
↓
5
Internal Schema
Show more lines
External Schema
User view of data.
Conceptual Schema
Logical structure of database.
Internal Schema
Physical storage details.
Advantages of Schema Architecture
Data independence.
Better database organization.
Improved security.
Easier maintenance.
Supports multiple user views.
Schema vs Instance
Schema	InstanceStructure of database	Actual data in database
Changes rarely	Changes frequently
Blueprint	Current content
Defined during design	Exists during execution
Example

Schema:

Plain Text
1
Student(RollNo, Name, Marks)
Show more lines

Instance:

Plain Text
1
(1, Rahul, 90)
2
(2, Anita, 85)
Show more lines
Exam Point

A Schema is the logical design or blueprint of a database. The three types of schemas are Physical Schema (Internal), Logical Schema (Conceptual), and View Schema (External). The Three-Schema Architecture provides data abstraction and data independence.

## Instances
A Schema is the overall logical structure or design of a database. It describes how data is organized, the tables present, their attributes, relationships, and constraints.

A schema acts as a blueprint of the database.

Characteristics of Schema
Defines the structure of the database.
Changes very rarely.
Created during database design.
Describes tables, fields, relationships, and constraints.
Independent of actual data.
Example

Student Table:

RollNo	Name	Marks1	Rahul	90
2	Anita	85

Schema:

Plain Text
1
STUDENT
2
(
3
RollNo INT,
4
Name VARCHAR(30),
5
Marks INT
6
)
Show more lines
Types of Schemas
1. Physical Schema
Definition

Describes how data is actually stored in the storage device.

It includes:

Storage structure
File organization
Indexing methods
Access paths
Example
Plain Text
1
Student records stored in a B-Tree index
Show more lines
Characteristics
Lowest level schema.
Concerned with physical storage.
Visible mainly to database administrators.
2. Logical Schema (Conceptual Schema)
Definition

Describes the logical structure of the entire database.

It includes:

Tables
Attributes
Relationships
Constraints
Example
Plain Text
1
STUDENT
2
(
3
RollNo,
4
Name,
5
Marks
6
)
Show more lines
Characteristics
Most important schema.
Describes what data is stored.
Independent of physical storage.
3. View Schema (External Schema)
Definition

Describes how different users view the database.

Different users may see different parts of the database.

Example

Teacher View:

Plain Text
1
RollNo
2
Name
3
Marks
Show more lines

Accounts Section View:

Plain Text
1
RollNo
2
Name
3
Fee_Status
Show more lines
Characteristics
Highest level schema.
User-specific.
Improves security.
Three Schema Architecture
Plain Text
1
External Schema
2
↓
3
Conceptual Schema
4
↓
5
Internal Schema
Show more lines
External Schema
User view of data.
Conceptual Schema
Logical structure of database.
Internal Schema
Physical storage details.
Advantages of Schema Architecture
Data independence.
Better database organization.
Improved security.
Easier maintenance.
Supports multiple user views.
Schema vs Instance
Schema	InstanceStructure of database	Actual data in database
Changes rarely	Changes frequently
Blueprint	Current content
Defined during design	Exists during execution
Example

Schema:

Plain Text
1
Student(RollNo, Name, Marks)
Show more lines

Instance:

Plain Text
1
(1, Rahul, 90)
2
(2, Anita, 85)
Show more lines
Exam Point

A Schema is the logical design or blueprint of a database. The three types of schemas are Physical Schema (Internal), Logical Schema (Conceptual), and View Schema (External). The Three-Schema Architecture provides data abstraction and data independence.

## Three Schema Architecture and Data Independence
The Three-Schema Architecture was introduced to separate user applications from the physical database. It provides different levels of abstraction and helps achieve Data Independence.

Levels of Three-Schema Architecture
1. External Schema (View Level)
Highest level of abstraction.
Describes how individual users view the database.
Different users can have different views.
Provides security by hiding unnecessary data.

Example:

Teacher View:

Plain Text
1
RollNo
2
Name
3
Marks
Show more lines

Accounts Department View:

Plain Text
1
RollNo
2
Name
3
Fee_Status
Show more lines
2. Conceptual Schema (Logical Level)
Describes the overall logical structure of the entire database.
Specifies:
Entities
Attributes
Relationships
Constraints
Independent of physical storage details.

Example:

Plain Text
1
STUDENT
2
(
3
RollNo,
4
Name,
5
Marks
6
)
Show more lines
3. Internal Schema (Physical Level)
Lowest level of abstraction.
Describes how data is physically stored.
Includes:
File organization
Storage structures
Indexing methods
Access paths

Example:

Plain Text
1
Student records stored using B-Tree indexing.
2
 
Show more lines
Architecture Diagram
Plain Text
1
External Schema
2
(View Level)
3
↓
4
 
5
Conceptual Schema
6
(Logical Level)
7
↓
8
 
9
Internal Schema
10
(Physical Level)
11
↓
12
 
13
Physical Database
Show more lines
Data Independence
Definition

Data Independence is the ability to modify the schema at one level without affecting the schema at the next higher level.

It allows changes in database structure without changing application programs.

Types of Data Independence
1. Physical Data Independence
Definition

Ability to change the internal schema without affecting the conceptual schema.

Examples
Changing file organization.
Changing indexing techniques.
Moving data to different storage devices.
Plain Text
1
B-Tree Index
2
↓
3
Hash Index
Show more lines

Applications continue to work without modification.

Advantages
Easy database maintenance.
Improved performance tuning.
No effect on application programs.
2. Logical Data Independence
Definition

Ability to change the conceptual schema without affecting external schemas or application programs.

Examples

Adding a new attribute:

Before:

Plain Text
1
STUDENT
2
(RollNo, Name)
Show more lines

After:

Plain Text
1
STUDENT
2
(RollNo, Name, Email)
Show more lines

Existing user programs remain unchanged.

Advantages
Easier database expansion.
Supports changing business requirements.
Better flexibility.
Limitation
More difficult to achieve than physical data independence.
Physical vs Logical Data Independence
Physical Data Independence	Logical Data IndependenceChanges internal schema	Changes conceptual schema
Easier to achieve	Harder to achieve
No effect on conceptual schema	No effect on external schema
Example: Change indexing method	Example: Add new attribute
Advantages of Three-Schema Architecture
Data abstraction.
Data security.
Data independence.
Multiple user views.
Easier database maintenance.
Better database design.
Applications
Banking Systems
Hospital Management Systems
Library Management Systems
Educational Databases
Enterprise Applications
Cloud Databases
Exam Point

Three-Schema Architecture consists of External Schema, Conceptual Schema, and Internal Schema. It provides Data Independence, which allows changes at one schema level without affecting higher levels. Data Independence is of two types: Physical Data Independence and Logical Data Independence.

## Database Language and Interfaces
A Database Language is a language used to define, manipulate, control, and retrieve data from a database. It provides communication between users and the Database Management System (DBMS).

Types of Database Languages
1. Data Definition Language (DDL)

Used to define and modify the database structure.

Commands
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
RollNo INT,
4
Name VARCHAR(30)
5
);
Show more lines
Functions
Creates database objects.
Modifies table structure.
Deletes database objects.
2. Data Manipulation Language (DML)

Used to manipulate data stored in database tables.

Commands
SQL
1
INSERT
2
UPDATE
3
DELETE
Show more lines
Examples
SQL
1
INSERT INTO Student
2
VALUES(1, 'Rahul');
Show more lines
SQL
1
UPDATE Student
2
SET Name = 'Anita'
3
WHERE RollNo = 1;
Show more lines
SQL
1
DELETE FROM Student
2
WHERE RollNo = 1;
Show more lines
Functions
Insert records.
Modify records.
Delete records.
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
Retrieve records.
Filter information.
Generate reports.
4. Data Control Language (DCL)

Used to control access permissions.

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
Show more lines
Functions
Security management.
User privilege control.
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
Maintain data consistency.
Manage transactions.
Database Interfaces
Definition

A Database Interface is a medium through which users interact with the database system.

It provides communication between users and the DBMS.

Types of Database Interfaces
1. Command-Line Interface (CLI)

Users enter commands directly.

Example
SQL
1
SELECT * FROM Student;
Show more lines
Advantages
Flexible
Powerful
Disadvantages
Requires SQL knowledge
2. Menu-Based Interface

Users select options from menus.

Example
Plain Text
1
1. Insert Record
2
2. Delete Record
3
3. Search Record
Show more lines
Advantages
Easy to use
User-friendly
3. Forms-Based Interface

Data is entered through forms.

Example
Plain Text
1
Name: _______
2
Age : _______
Show more lines
Advantages
Easy data entry
Reduces user errors
4. Graphical User Interface (GUI)

Uses windows, buttons, icons, and menus.

Examples
MS Access
MySQL Workbench
Oracle Forms
Advantages
User-friendly
Visual interaction
5. Natural Language Interface

Allows interaction using natural language.

Example
Plain Text
1
Show all students with marks above 80.
Show more lines
Advantages
Easy for non-technical users
6. Web-Based Interface

Database accessed through web applications.

Examples
Online Banking
E-Commerce Websites
Student Portals
Advantages of Database Languages and Interfaces
Database Languages
Easy database management.
Efficient data retrieval.
Better security.
Supports transaction processing.
Database Interfaces
User-friendly interaction.
Reduced complexity.
Faster operations.
Improved accessibility.
Applications
Banking Systems
Library Management Systems
Hospital Systems
University Databases
E-commerce Applications
Government Information Systems
Exam Point

Database Languages are used to define, manipulate, retrieve, and control data in a database. The major database languages are DDL, DML, DQL, DCL, and TCL. Database Interfaces provide interaction between users and the DBMS through command-line, menu-based, forms-based, GUI, natural-language, and web-based interfaces.

## Centralized and Client/Server Architectures for DBMS
A Centralized Database Architecture is an architecture in which the entire database system, including the database, DBMS, and application programs, is located on a single central computer.

All users access the database through the central system.

Structure
Plain Text
1
Users
2
|
3
|
4
V
5
+----------------+
6
| Central System |
7
| DBMS + Database|
8
+----------------+
Show more lines
Features
Single database location.
Single DBMS controls all operations.
Data stored at one site.
Easy administration and security control.
Advantages
Easy to manage.
Better data consistency.
Strong security control.
Low maintenance complexity.
Disadvantages
Single point of failure.
Performance decreases with many users.
Limited scalability.
Applications
Small organizations
Educational institutions
Standalone business systems
Client/Server Architecture
Definition

Client/Server Architecture is a database architecture in which database services are divided between clients and a server.

Client sends requests.
Server processes requests and returns results.
Structure
Plain Text
1
Client 1
2
\
3
Client 2 -----> Database Server
4
/
5
Client 3
6
``
Show more lines
Working
Client sends a request.
Server processes the request.
Database is accessed.
Result is returned to the client.
Two-Tier Client/Server Architecture
Definition

A client communicates directly with the database server.

Structure
Plain Text
1
Client
2
|
3
|
4
Database Server
Show more lines
Example
Plain Text
1
Application ↔ MySQL Server
Show more lines
Advantages
Simple design.
Faster communication.
Disadvantages
Less secure.
Difficult to scale.
Three-Tier Client/Server Architecture
Definition

An intermediate application server is placed between client and database server.

Structure
Plain Text
1
Client
2
|
3
Application Server
4
|
5
Database Server
Show more lines
Components
Presentation Layer

Client interface.

Application Layer

Business logic processing.

Database Layer

Stores and manages data.

Advantages
Better security.
Improved scalability.
Easier maintenance.
Disadvantages
More complex implementation.
Higher cost.
Centralized vs Client/Server Architecture
Feature	Centralized Architecture	Client/Server ArchitectureDatabase Location	Single central system	Database server
Processing	Centralized	Distributed between client and server
Scalability	Limited	Higher
Performance	May become bottleneck	Better for multiple users
Security	Easy centralized control	Flexible security management
Fault Tolerance	Single point of failure	Better reliability
Advantages of Client/Server Architecture
Better resource sharing.
Supports multiple users.
Improved performance.
Easier expansion.
Distributed workload.
Applications
Centralized Architecture
Small databases
Standalone applications
Local business systems
Client/Server Architecture
Banking systems
E-commerce applications
Enterprise databases
Hospital management systems
University information systems
Exam Point

Centralized Architecture stores the database and DBMS at a single central location, whereas Client/Server Architecture distributes processing between clients and a database server. Client/Server Architecture may be implemented as Two-Tier or Three-Tier architecture and provides better scalability, performance, and flexibility.