# Normalization for Relational Databases
## Anomalies in relational data base design data
Database Anomalies are problems that occur in a poorly designed relational database due to data redundancy. These anomalies can lead to inconsistent, inaccurate, or difficult-to-maintain data.

Anomalies are one of the main reasons for performing Normalization.

Types of Anomalies
1. Insertion Anomaly
Definition

An Insertion Anomaly occurs when certain information cannot be inserted into the database without adding some other unrelated information.

Example
StudentID	StudentName	Course1	Rahul	DBMS
2	Anita	OS

Suppose a new course:

Plain Text
1
Computer Networks
Show more lines

is introduced but no student has enrolled yet.

The course cannot be inserted because the table requires student data.

Problem
Inability to store some information independently.
2. Update Anomaly
Definition

An Update Anomaly occurs when the same data is stored in multiple rows and must be updated in all places.

Example
StudentID	StudentName	Department1	Rahul	CSE
2	Anita	CSE

If the department name changes:

Plain Text
1
CSE → Computer Science
2
 
Show more lines

all rows must be updated.

If one row is missed:

StudentID	StudentName	Department1	Rahul	Computer Science
2	Anita	CSE
Problem
Data inconsistency occurs.
3. Deletion Anomaly
Definition

A Deletion Anomaly occurs when deleting one record unintentionally removes other valuable information.

Example
StudentID	StudentName	Course1	Rahul	DBMS
2	Anita	OS

If Rahul's record is deleted:

Plain Text
1
DELETE StudentID = 1
2
``
Show more lines

information about the DBMS course may also be lost.

Problem
Important data is removed accidentally.
Causes of Anomalies
Poor database design.
Data redundancy.
Multiple facts stored in a single table.
Lack of normalization.
Solution: Normalization

Normalization reduces anomalies by dividing data into properly related tables.

Example

Instead of:

Plain Text
1
Student(StudentID, Name, Course)
Show more lines

Create:

Plain Text
1
Student(StudentID, Name)
2
 
3
Course(CourseID, CourseName)
4
 
5
Enrollment(StudentID, CourseID)
Show more lines

This minimizes redundancy and anomalies.

Comparison of Anomalies
Anomaly	ProblemInsertion Anomaly	Cannot add data independently
Update Anomaly	Same data updated in multiple places
Deletion Anomaly	Deleting one record removes other information
Advantages of Eliminating Anomalies
Improved data consistency.
Reduced redundancy.
Easier maintenance.
Better database integrity.
Efficient storage utilization.
Exam Point

Relational database anomalies are unwanted problems caused by data redundancy. The three main anomalies are:

Insertion Anomaly – Difficulty adding data.
Update Anomaly – Inconsistent updates.
Deletion Anomaly – Unintended loss of data.

Normalization is used to eliminate these anomalies.

## Functional Dependencies and Normalizations
A Functional Dependency is a relationship between two attributes in a relation where the value of one attribute uniquely determines the value of another attribute.

Notation
Plain Text
1
A → B
Show more lines

Meaning:

Plain Text
1
A determines B
Show more lines

If two rows have the same value of A, they must have the same value of B.

Example
STUDENT Table
StudentID	Name	Department101	Rahul	CSE
102	Anita	ECE

Functional Dependencies:

Plain Text
1
StudentID → Name
2
StudentID → Department
3
 
Show more lines

Because each StudentID uniquely determines Name and Department.

Types of Functional Dependencies
1. Trivial Functional Dependency

Occurs when:

Plain Text
1
Y ⊆ X
Show more lines

Example:

Plain Text
1
(StudentID, Name) → Name
Show more lines
2. Non-Trivial Functional Dependency

Occurs when:

Plain Text
1
Y ⊄ X
Show more lines

Example:

Plain Text
1
StudentID → Name
Show more lines
3. Completely Functional Dependency

An attribute depends on the whole key.

Example:

Plain Text
1
(StudentID, CourseID) → Grade
Show more lines

Grade depends on both StudentID and CourseID.

4. Partial Dependency

A non-key attribute depends on only part of a composite key.

Example:

Plain Text
1
(StudentID, CourseID) → StudentName
Show more lines

StudentName depends only on StudentID.

5. Transitive Dependency

Occurs when:

Plain Text
1
A → B
2
B → C
3
 
4
Therefore
5
 
6
A → C
Show more lines

Example:

Plain Text
1
StudentID → DeptID
2
DeptID → DeptName
3
 
4
StudentID → DeptName
Show more lines
Normalization
Definition

Normalization is the process of organizing database tables to reduce redundancy and eliminate anomalies.

Objectives
Eliminate duplicate data.
Remove insertion anomalies.
Remove update anomalies.
Remove deletion anomalies.
Improve data integrity.
Normal Forms
First Normal Form (1NF)
Rule
Every attribute must contain atomic values.
No repeating groups.
Not in 1NF
StudentID	Subjects101	DBMS, OS
In 1NF
StudentID	Subject101	DBMS
101	OS
Second Normal Form (2NF)
Rule
Must be in 1NF.
No partial dependency.
Example
StudentID	CourseID	StudentName101	C1	Rahul

FD:

Plain Text
1
StudentID → StudentName
Show more lines

Partial dependency exists.

Convert to 2NF

Student

StudentID	StudentName101	Rahul

Enrollment

StudentID	CourseID101	C1
Third Normal Form (3NF)
Rule
Must be in 2NF.
No transitive dependency.
Example
StudentID	DeptID	DeptName

FD:

Plain Text
1
StudentID → DeptID
2
DeptID → DeptName
Show more lines

Transitive dependency exists.

Convert to 3NF

Student

StudentID	DeptID

Department

DeptID	DeptName
Boyce-Codd Normal Form (BCNF)
Rule

For every FD:

Plain Text
1
X → Y
Show more lines

X must be a super key.

BCNF is a stronger version of 3NF.

Anomalies Removed
Insertion Anomaly

Cannot insert data independently.

Update Anomaly

Same information updated in multiple places.

Deletion Anomaly

Deleting one record removes unrelated information.

Normalization helps eliminate these anomalies.

Functional Dependency vs Normalization
Functional Dependency	NormalizationIdentifies attribute relationships	Removes redundancy
Basis for normalization	Uses FDs for decomposition
Expressed as X → Y	Organized into normal forms
Advantages of Normalization
Reduced data redundancy.
Improved consistency.
Better integrity.
Easier maintenance.
Efficient storage utilization.
Exam Point
Functional Dependency: Relationship where one attribute determines another.
Plain Text
1
StudentID → Name
Show more lines
Normalization: Process of organizing data to eliminate redundancy and anomalies.
Normal Forms
Plain Text
1
1NF → Atomic values
2
2NF → Remove partial dependency
3
3NF → Remove transitive dependency
4
BCNF → Every determinant must be a super key

## algorithms for Query Processing and Optimization
Query Processing is the process of converting a high-level query (usually SQL) into an efficient sequence of operations that can be executed by the DBMS to retrieve the required data.

Stages of Query Processing
Query Parsing
Query Translation
Query Optimization
Query Evaluation
Process
Plain Text
1
SQL Query
2
↓
3
Parser
4
↓
5
Relational Algebra Expression
6
↓
7
Optimizer
8
↓
9
Execution Plan
10
↓
11
Result
Show more lines
Query Processing Algorithms
1. Sequential Search
Definition

The entire table is scanned row by row until the required record is found.

Example
SQL
1
SELECT *
2
FROM Student
3
WHERE StudentID = 101;
Show more lines
Characteristics
Simple implementation.
No index required.
Slow for large databases.
Time Complexity
Plain Text
1
O(n)
2
``
Show more lines
2. Binary Search
Definition

Used when records are sorted on the search attribute.

Process
Find middle record.
Compare key value.
Search left or right half.
Time Complexity
Plain Text
1
O(log n)
Show more lines
Advantage
Faster than sequential search.
3. Index-Based Search
Definition

Uses an index structure to locate records.

Example
Plain Text
1
B-Tree Index
2
Hash Index
Show more lines
Advantages
Faster retrieval.
Avoids full table scanning.
Join Processing Algorithms
1. Nested Loop Join
Definition

For each record in one relation, all records in the other relation are checked.

Example
Plain Text
1
Student × Course
2
 
Show more lines
Characteristics
Simple algorithm.
High execution cost.
Complexity
Plain Text
1
O(m × n)
Show more lines
2. Sort-Merge Join
Definition

Relations are sorted on join attributes and then merged.

Steps
Sort both tables.
Merge matching tuples.
Advantages
Efficient for large relations.
Suitable for sorted data.
3. Hash Join
Definition

Uses a hash table on the join attribute.

Steps
Build hash table.
Probe matching tuples.
Advantages
Fast join operation.
Very efficient for equi-joins.
Query Optimization
Definition

Query Optimization is the process of selecting the most efficient strategy for executing a query.

The objective is to reduce:

Execution time
Disk I/O
CPU usage
Memory usage
Query Optimization Techniques
1. Selection Pushdown

Apply selection as early as possible.

Example

Instead of:

Plain Text
1
Join → Selection
Show more lines

Use:

Plain Text
1
Selection → Join
Show more lines
Advantage
Reduces intermediate results.
2. Projection Pushdown

Retrieve only required columns.

Example
SQL
1
SELECT Name
2
FROM Student;
Show more lines

Instead of retrieving all columns.

Advantage
Reduces memory usage.
3. Join Reordering

Choose the most efficient join sequence.

Advantage
Reduces processing cost.
4. Use of Indexes

Indexes improve search speed.

Example
Plain Text
1
B-Tree
2
Hash Index
Show more lines
Advantage
Faster retrieval.
Cost-Based Optimization
Definition

The optimizer evaluates multiple execution plans and selects the one with the lowest estimated cost.

Cost Factors
Number of disk accesses.
CPU usage.
Memory requirements.
Number of tuples processed.
Rule-Based Optimization
Definition

Uses predefined rules instead of cost calculations.

Example Rules
Push selections downward.
Push projections downward.
Replace Cartesian product with joins.
Query Processing vs Query Optimization
Query Processing	Query OptimizationExecutes the query	Chooses best execution plan
Converts SQL into operations	Improves efficiency
Produces result	Reduces execution cost
Advantages of Query Optimization
Faster query execution.
Reduced disk access.
Better resource utilization.
Improved database performance.
Reduced response time.
Applications
DBMS Systems
Banking Databases
E-Commerce Systems
Data Warehouses
Enterprise Applications
Cloud Databases
Exam Point

Query Processing converts SQL queries into executable operations, while Query Optimization selects the most efficient execution plan. Important algorithms include Sequential Search, Binary Search, Nested Loop Join, Sort-Merge Join, and Hash Join. Optimization techniques include Selection Pushdown, Projection Pushdown, Join Reordering, and Index Usage.

## Transaction Processing
A Transaction is a sequence of one or more database operations treated as a single logical unit of work. A transaction must be completed entirely or not executed at all.

Example

Bank Transfer:

Plain Text
1
Step 1: Debit ₹1000 from Account A
2
Step 2: Credit ₹1000 to Account B
3
``
Show more lines

Both operations must succeed together.

Transaction Processing

Transaction Processing is the mechanism used by a DBMS to ensure that transactions are executed correctly, consistently, and reliably.

Objectives
Maintain data consistency.
Ensure data integrity.
Handle concurrent users.
Recover from failures.
Prevent data loss.
States of a Transaction
Active

Transaction is executing.

Partially Committed

Final statement executed.

Committed

Transaction completed successfully.

Failed

Execution cannot continue.

Aborted

Transaction is rolled back.

Terminated

Transaction leaves the system.

Plain Text
1
Active
2
↓
3
Partially Committed
4
↓
5
Committed
6
``
Show more lines

or

Plain Text
1
Active
2
↓
3
Failed
4
↓
5
Aborted
6
``
Show more lines
ACID Properties
1. Atomicity

"All or Nothing"

Either all operations execute or none execute.

Example
Plain Text
1
Debit Account A
2
Credit Account B
Show more lines

If credit fails, debit must also be cancelled.

2. Consistency

Database must move from one valid state to another valid state.

Example
Plain Text
1
Total balance remains unchanged after transfer.
Show more lines
3. Isolation

Transactions execute independently.

Example

One transaction should not interfere with another transaction.

4. Durability

Once committed, changes are permanent.

Example

Data remains saved even after power failure.

Transaction Control Commands (TCL)
COMMIT

Permanently saves changes.

SQL
1
COMMIT;
Show more lines
ROLLBACK

Undoes changes since the last commit.

SQL
1
ROLLBACK;
Show more lines
SAVEPOINT

Creates a point to which rollback can occur.

SQL
1
SAVEPOINT SP1;
Show more lines
Concurrency Control
Definition

Concurrency control ensures correct execution when multiple transactions occur simultaneously.

Techniques
Locking
Timestamp Ordering
Validation Protocol
Problems in Concurrent Transactions
Lost Update

One update overwrites another.

Dirty Read

Reading uncommitted data.

Unrepeatable Read

Reading the same data twice gives different results.

Incorrect Summary

Aggregate calculations produce incorrect results.

Serializability
Definition

A schedule is serializable if the result is equivalent to some serial execution of transactions.

Types
Conflict Serializability
View Serializability
Recovery Management

Used to restore the database after system failure.

Techniques
Log-based Recovery
Checkpointing
Rollback
Shadow Copying
Advantages of Transaction Processing
Ensures data integrity.
Supports multi-user access.
Provides failure recovery.
Prevents inconsistent data.
Improves reliability.
Applications
Banking Systems
Railway Reservation Systems
E-Commerce Applications
Hospital Management Systems
Inventory Systems
Online Payment Systems
Exam Point

Transaction Processing is the mechanism used by a DBMS to execute database transactions reliably. A transaction follows the ACID properties: Atomicity, Consistency, Isolation, and Durability. Transaction control commands include COMMIT, ROLLBACK, and SAVEPOINT.

## Concurrency Control Techniques
Concurrency Control is a DBMS mechanism that ensures multiple transactions execute simultaneously without affecting the consistency and integrity of the database.

It prevents conflicts when several users access the same data at the same time.

Example
Plain Text
1
Transaction T1:
2
Withdraw ₹1000
3
 
4
Transaction T2:
5
Deposit ₹500
Show more lines

Both transactions may access the same account simultaneously. Concurrency control ensures correct results.

Need for Concurrency Control
Maintain database consistency.
Prevent data corruption.
Support multi-user access.
Avoid transaction conflicts.
Ensure isolation property of ACID.
Problems Caused by Concurrent Transactions
1. Lost Update Problem

Occurs when one transaction overwrites another transaction's update.

Example
Plain Text
1
T1 reads Account = 1000
2
T2 reads Account = 1000
3
 
4
T1 updates to 900
5
T2 updates to 1200
Show more lines

T1's update is lost.

2. Dirty Read Problem

Occurs when a transaction reads uncommitted data from another transaction.

Example
Plain Text
1
T1 updates salary
2
T2 reads salary before T1 commits
3
T1 rolls back
Show more lines

T2 used invalid data.

3. Unrepeatable Read

The same record produces different results during a transaction.

Example
Plain Text
1
T1 reads Marks = 80
2
T2 updates Marks = 90
3
T1 reads again = 90
Show more lines
4. Incorrect Summary

Occurs when aggregate calculations are performed while updates are taking place.

Concurrency Control Techniques
1. Lock-Based Protocol
Definition

A transaction must acquire a lock before accessing data.

Types of Locks
Shared Lock (S-Lock)
Used for reading.
Multiple transactions can hold shared locks simultaneously.
Plain Text
1
Read Only
Show more lines
Exclusive Lock (X-Lock)
Used for writing.
Only one transaction can hold it.
Plain Text
1
Read + Write
Show more lines
Two-Phase Locking (2PL)
Definition

Transactions proceed in two phases:

Growing Phase
Plain Text
1
Acquire locks
2
No lock release
Show more lines
Shrinking Phase
Plain Text
1
Release locks
2
No new locks acquired
Show more lines
Advantage
Ensures conflict serializability.
Disadvantage
Can cause deadlocks.
2. Timestamp-Based Protocol
Definition

Each transaction receives a unique timestamp.

Transactions execute according to timestamp order.

Working
Plain Text
1
Older Transaction
2
↓
3
Higher Priority
4
↓
5
Executed First
Show more lines
Advantages
Deadlock-free.
Simple ordering.
Disadvantages
Possible transaction rollback.
3. Validation-Based Protocol
Definition

Also called Optimistic Concurrency Control.

Transactions execute without locks.

Validation is performed before commit.

Phases
Read Phase
Validation Phase
Write Phase
Advantages
No deadlocks.
Suitable for low-conflict environments.
Disadvantages
Frequent rollbacks under heavy contention.
4. Multiversion Concurrency Control (MVCC)
Definition

Maintains multiple versions of data.

Read operations access older versions while updates create new versions.

Advantages
High concurrency.
Reduced blocking.
Better performance.
Applications
PostgreSQL
Oracle
MySQL (InnoDB)
Deadlock
Definition

A deadlock occurs when two or more transactions wait indefinitely for each other to release locks.

Example
Plain Text
1
T1 holds Lock A, waits for Lock B
2
 
3
T2 holds Lock B, waits for Lock A
Show more lines

Neither can proceed.

Deadlock Handling
Prevention

Avoid deadlock conditions.

Detection

Detect deadlocks and abort one transaction.

Recovery

Rollback selected transactions.

Comparison of Techniques
Technique	Uses Locks	Deadlock Possible	PerformanceLock-Based	Yes	Yes	Good
Timestamp-Based	No	No	Good
Validation-Based	No	No	Good for low conflicts
MVCC	Multiple Versions	No	Very High
Advantages of Concurrency Control
Maintains consistency.
Prevents anomalies.
Supports multiple users.
Improves database reliability.
Ensures transaction isolation.
Exam Point

Concurrency Control is used to ensure correct execution of simultaneous transactions. Major techniques are Lock-Based Protocols (Shared Lock, Exclusive Lock, Two-Phase Locking), Timestamp-Based Protocols, Validation-Based Protocols, and Multiversion Concurrency Control (MVCC). It prevents Lost Updates, Dirty Reads, Unrepeatable Reads, and other transaction anomalies.

## Database Recovery Techniques
Database Recovery is the process of restoring a database to a correct and consistent state after a failure such as:

System crash
Power failure
Hardware failure
Software error
Transaction failure

The main goal of recovery is to ensure that committed transactions are preserved and incomplete transactions do not affect database consistency.

Need for Recovery
Protects data from failures.
Maintains database consistency.
Ensures transaction durability (ACID property).
Prevents data loss.
Restores the database after unexpected crashes.
Types of Failures
1. Transaction Failure

Occurs when a transaction cannot complete.

Example:

Plain Text
1
Division by zero
2
Invalid input
3
Deadlock
Show more lines
2. System Failure

Occurs due to:

Plain Text
1
Power failure
2
Operating system crash
3
Hardware malfunction
Show more lines
3. Media Failure

Occurs when storage devices fail.

Example:

Plain Text
1
Disk crash
2
Corrupted storage
Show more lines
Recovery Techniques
1. Log-Based Recovery
Definition

The DBMS maintains a log file containing all transaction activities.

The log record stores:

Plain Text
1
Transaction ID
2
Operation
3
Old Value
4
New Value
Show more lines
Example
Plain Text
1
T1:
2
A = 100
3
 
4
Update A = 200
5
``
Show more lines

Log:

Plain Text
1
<T1, A, 100, 200>
Show more lines
Advantages
Reliable recovery.
Supports rollback and redo operations.
Types of Log-Based Recovery
Deferred Update
Database is updated only after transaction commits.
Requires only REDO operations.

Process:

Plain Text
1
Execute Transaction
2
↓
3
Commit
4
↓
5
Write to Database
Show more lines
Immediate Update
Database updated before transaction commits.
Requires both UNDO and REDO operations.

Process:

Plain Text
1
Execute Transaction
2
↓
3
Update Database
4
↓
5
Commit
Show more lines
2. Checkpointing
Definition

A Checkpoint is a recovery point where all updated data and log records are written to stable storage.

Working
Plain Text
1
Transactions
2
↓
3
Checkpoint
4
↓
5
Continue Execution
Show more lines

After a crash, recovery starts from the latest checkpoint rather than from the beginning of the log.

Advantages
Faster recovery.
Reduces recovery time.
3. Shadow Paging
Definition

Shadow Paging maintains two page tables:

Current Page Table
Shadow Page Table

The shadow page table remains unchanged during transaction execution.

Working
Plain Text
1
Shadow Page Table
2
|
3
Unchanged Copy
4
 
5
Current Page Table
6
|
7
Modified Copy
Show more lines

After successful commit:

Plain Text
1
Current Page Table
2
becomes
3
Shadow Page Table
Show more lines
Advantages
No UNDO required.
Simple recovery.
Disadvantages
Extra storage required.
Page table management overhead.
4. Undo Operation
Definition

UNDO restores data to its previous state.

Example

Before update:

Plain Text
1
Balance = 5000
Show more lines

After update:

Plain Text
1
Balance = 4000
Show more lines

Transaction fails:

Plain Text
1
UNDO
Show more lines

Restores:

Plain Text
1
Balance = 5000
Show more lines
5. Redo Operation
Definition

REDO repeats completed operations after a crash.

Example

Transaction committed:

Plain Text
1
Balance = 5000
Show more lines

Updated:

Plain Text
1
Balance = 6000
Show more lines

Crash occurs.

REDO:

Plain Text
1
Balance = 6000
Show more lines

is restored.

Recovery Concepts
Transaction Log

Stores:

Plain Text
1
BEGIN TRANSACTION
2
UPDATE
3
COMMIT
4
ROLLBACK
Show more lines

Used during recovery.

Rollback

Cancels a transaction.

SQL
1
ROLLBACK;
Show more lines

Returns database to previous consistent state.

Commit

Permanently saves changes.

SQL
1
COMMIT;
Show more lines

Ensures changes survive failures.

Undo vs Redo
Undo	RedoReverses operation	Repeats operation
Used for incomplete transactions	Used for committed transactions
Restores old values	Restores new values
Comparison of Recovery Techniques
Technique	Main IdeaLog-Based Recovery	Uses transaction logs
Checkpointing	Creates recovery points
Shadow Paging	Uses shadow page tables
Undo Recovery	Restores previous values
Redo Recovery	Reapplies committed changes
Advantages of Database Recovery
Prevents data loss.
Maintains consistency.
Supports ACID properties.
Improves reliability.
Ensures business continuity.
Applications
Banking Systems
Airline Reservation Systems
E-Commerce Websites
Hospital Management Systems
Enterprise Databases
Exam Point

Database Recovery Techniques are methods used to restore a database after failures. Major techniques include Log-Based Recovery, Checkpointing, Shadow Paging, Undo Recovery, and Redo Recovery. Recovery mechanisms ensure database consistency and support the Atomicity and Durability properties of transactions.

