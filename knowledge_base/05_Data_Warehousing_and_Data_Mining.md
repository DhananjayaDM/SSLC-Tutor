# Data Warehousing and Data Mining
## Data Modelling for Data Warehouse
Data Modeling for a Data Warehouse is the process of designing the structure of data so that it can support efficient reporting, analysis, and decision-making.

Unlike operational databases (OLTP), data warehouses are designed for:

Historical data analysis
Business intelligence
Data mining
Decision support systems
Objectives of Data Warehouse Data Modeling
Organize large amounts of historical data.
Improve query performance.
Support analytical processing.
Simplify reporting.
Enable easy data integration from multiple sources.
Components of Data Warehouse Modeling
Fact Table

A Fact Table contains quantitative data (measures) about business operations.

Examples:

Plain Text
1
Sales Amount
2
Profit
3
Quantity Sold
4
Revenue
Show more lines

Example:

ProductID	CustomerID	DateID	Sales101	201	1	5000
Dimension Table

A Dimension Table contains descriptive information about facts.

Examples:

Plain Text
1
Customer
2
Product
3
Location
4
Time
Show more lines

Product Dimension:

ProductID	ProductName	Category101	Laptop	Electronics
Data Warehouse Schemas
1. Star Schema

The most common data warehouse model.

Structure
Plain Text
1
Customer
2
|
3
Product --- Sales --- Time
4
|
5
Location
Show more lines
One central Fact Table.
Multiple Dimension Tables.
Simple and fast queries.
Advantages
Easy to understand.
High query performance.
Less complex joins.
Disadvantages
Data redundancy in dimension tables.
2. Snowflake Schema

An extension of the Star Schema.

Structure
Plain Text
1
Product
2
|
3
Category
4
|
5
Sales
Show more lines

Dimension tables are normalized.

Advantages
Reduced redundancy.
Better data consistency.
Disadvantages
More joins required.
More complex design.
3. Fact Constellation Schema (Galaxy Schema)

Contains multiple fact tables sharing dimension tables.

Example
Plain Text
1
Sales Fact
2
|
3
Product
4
|
5
Inventory Fact
Show more lines
Advantages
Supports complex business environments.
Handles multiple business processes.
Disadvantages
Complex design and maintenance.
Star Schema vs Snowflake Schema
Feature	Star Schema	Snowflake SchemaStructure	Denormalized	Normalized
Complexity	Simple	Complex
Query Speed	Faster	Slower
Redundancy	Higher	Lower
Number of Joins	Fewer	More
Measures in Fact Tables
Additive Measures

Can be summed.

Example:

Plain Text
1
Sales
2
Profit
3
Quantity
Show more lines
Semi-Additive Measures

Can be summed across some dimensions.

Example:

Plain Text
1
Account Balance
Show more lines
Non-Additive Measures

Cannot be summed.

Example:

Plain Text
1
Percentage
2
Ratio
Show more lines
Steps in Data Warehouse Modeling
Identify business requirements.
Identify fact tables.
Identify dimension tables.
Define relationships.
Select schema type (Star, Snowflake, Galaxy).
Create warehouse structure.
Load and maintain warehouse data.
Advantages of Data Warehouse Modeling
Faster analytical queries.
Better decision support.
Historical data analysis.
Simplified reporting.
Improved business intelligence.
Applications
Banking and Finance
Sales Analysis
Retail Systems
Healthcare Analytics
Government Reporting
E-Commerce Analytics
Exam Point

Data Warehouse Modeling organizes data into Fact Tables and Dimension Tables. The primary schema models are Star Schema, Snowflake Schema, and Fact Constellation Schema. Star Schema is the most widely used because of its simplicity and fast query performance.

## Concept Hierarchy
A Concept Hierarchy is a hierarchical arrangement of data values from a higher level of abstraction (general concept) to a lower level of abstraction (specific concept).

It is widely used in:

Data Warehousing
Data Mining
OLAP (Online Analytical Processing)
Knowledge Discovery

Concept hierarchies help summarize and generalize data.

Purpose of Concept Hierarchy
Data summarization
Data generalization
Data analysis at different levels
Decision making
OLAP roll-up and drill-down operations
Example
Location Hierarchy
Plain Text
1
Country
2
↓
3
State
4
↓
5
District
6
↓
7
City
Show more lines

Example:

Plain Text
1
India
2
↓
3
Karnataka
4
↓
5
Bangalore Urban
6
↓
7
Bangalore
Show more lines
Time Hierarchy
Plain Text
1
Year
2
↓
3
Quarter
4
↓
5
Month
6
↓
7
Day
Show more lines

Example:

Plain Text
1
2025
2
↓
3
Q1
4
↓
5
January
6
↓
7
15
Show more lines
Product Hierarchy
Plain Text
1
Category
2
↓
3
Subcategory
4
↓
5
Product
Show more lines

Example:

Plain Text
1
Electronics
2
↓
3
Mobile Phones
4
↓
5
iPhone
Show more lines
Levels in Concept Hierarchy
High-Level Concept

Generalized information.

Example:

Plain Text
1
Country
Show more lines
Intermediate Level

Moderately detailed information.

Example:

Plain Text
1
State
Show more lines
Low-Level Concept

Highly detailed information.

Example:

Plain Text
1
City
Show more lines
Types of Concept Hierarchies
1. Schema-Based Concept Hierarchy

Built using database relationships.

Example:

Plain Text
1
Street → City → State → Country
Show more lines
2. Set-Grouping Hierarchy

Values grouped into categories.

Example:

Plain Text
1
Age
2
 
3
0–12 → Child
4
13–19 → Teenager
5
20–60 → Adult
6
60+ → Senior Citizen
Show more lines
3. Operation-Derived Hierarchy

Generated automatically through operations.

Example:

Plain Text
1
Day
2
↓
3
Month
4
↓
5
Year
Show more lines
Concept Hierarchy in Data Warehousing

Used in OLAP operations:

Roll-Up

Moves from detailed data to summarized data.

Example:

Plain Text
1
City → State → Country
Show more lines
Drill-Down

Moves from summarized data to detailed data.

Example:

Plain Text
1
Country → State → City
Show more lines
Advantages
Simplifies data analysis.
Supports data aggregation.
Improves decision making.
Reduces data complexity.
Enables multidimensional analysis.
Applications
Data Warehousing
Data Mining
Business Intelligence
OLAP Systems
Market Analysis
Sales Reporting
Concept Hierarchy vs Concept Generalization
Concept Hierarchy	Concept GeneralizationStructure of abstraction levels	Process of moving to higher abstraction
Provides hierarchy	Uses hierarchy
Static representation	Dynamic operation
Exam Point

Concept Hierarchy is a structured arrangement of data values from lower-level detailed concepts to higher-level generalized concepts. It is used in Data Warehousing and Data Mining for data summarization, roll-up, drill-down, and multidimensional analysis.

## OLAP and OLTP
OLAP (Online Analytical Processing) is a technology used for analyzing large volumes of historical data to support decision-making and business intelligence.

It is mainly used in:

Data Warehouses
Data Mining
Business Intelligence Systems
Reporting and Analytics
Characteristics
Supports complex queries.
Uses historical data.
Read-intensive operations.
Multidimensional analysis.
Helps in strategic decision making.
Example
Plain Text
1
Analyze sales performance for the last 5 years.
Show more lines
Operations in OLAP
Roll-Up

Data summarized to a higher level.

Plain Text
1
City → State → Country
Show more lines
Drill-Down

Data viewed in more detail.

Plain Text
1
Country → State → City
Show more lines
Slice

Selects a subset of data.

Dice

Selects data from multiple dimensions.

OLTP (Online Transaction Processing)
Definition

OLTP (Online Transaction Processing) is a system designed to manage day-to-day business transactions efficiently.

It is used for:

Banking transactions
Railway reservations
ATM transactions
Online shopping
Inventory management
Characteristics
Handles current operational data.
Supports large numbers of users.
Frequent INSERT, UPDATE, DELETE operations.
Fast transaction processing.
Focuses on data integrity.
Example
Plain Text
1
Deposit money into a bank account.
Show more lines
Plain Text
1
Book a railway ticket.
Show more lines
OLAP vs OLTP
Feature	OLAP	OLTPFull Form	Online Analytical Processing	Online Transaction Processing
Purpose	Data Analysis	Transaction Processing
Data Type	Historical Data	Current Data
Operations	Complex Queries	Insert, Update, Delete
Users	Managers, Analysts	End Users, Clerks
Query Complexity	High	Simple
Database Size	Very Large	Moderate
Response Time	Seconds or Minutes	Milliseconds or Seconds
Normalization	Less Normalized	Highly Normalized
Application	Decision Support	Operational Systems
Examples
OLTP Applications
Banking Systems
ATM Systems
Airline Reservation Systems
E-Commerce Websites
Hospital Management Systems
OLAP Applications
Sales Analysis
Market Analysis
Financial Forecasting
Data Warehousing
Business Intelligence
Advantages of OLTP
Fast transaction processing.
High data accuracy.
Supports many users.
Maintains data integrity.
Advantages of OLAP
Better decision making.
Fast analytical processing.
Trend analysis.
Multidimensional reporting.
Exam Point

OLTP is used for day-to-day transaction processing, while OLAP is used for analytical processing and decision support. OLTP works on current operational data, whereas OLAP works on historical data stored in data warehouses.

## Association Rules
Association Rules are data mining techniques used to discover relationships or associations between items in a large database.

They identify patterns of the form:

Plain Text
1
IF X occurs
2
THEN Y also occurs
Show more lines

Association rule mining is widely used in:

Market Basket Analysis
Retail Sales
Recommendation Systems
Customer Behavior Analysis
Basic Form
Plain Text
1
X → Y
Show more lines

Where:

X = Antecedent (IF part)
Y = Consequent (THEN part)
Example
Plain Text
1
Milk → Bread
Show more lines

Meaning:

Customers who buy milk also tend to buy bread.

Market Basket Analysis
Example Transaction Database
Transaction ID	Items PurchasedT1	Milk, Bread
T2	Milk, Bread, Butter
T3	Bread, Butter
T4	Milk, Butter

From these transactions:

Plain Text
1
Milk → Bread
Show more lines

may be discovered as an association rule.

Measures of Association Rules
1. Support
Definition

Support indicates how frequently an itemset appears in the database.







2. Confidence
Definition

Confidence measures how often Y appears when X appears.





3. Lift
Definition

Lift measures the strength of an association.


Interpretation
Plain Text
1
Lift > 1 → Positive association
2
Lift = 1 → Independent items
3
Lift < 1 → Negative association
Show more lines
Types of Association Rules
Single-Dimensional Association Rule

Uses one dimension.

Example:

Plain Text
1
Milk → Bread
Show more lines
Multi-Dimensional Association Rule

Uses multiple dimensions.

Example:

Plain Text
1
Age = 20-30 AND Buys = Laptop
2
→ Buys = Headphone
Show more lines
Mining Association Rules
Step 1

Find frequent itemsets.

Step 2

Generate association rules.

Step 3

Calculate support and confidence.

Step 4

Select rules satisfying minimum thresholds.

Apriori Algorithm
Definition

The Apriori Algorithm is the most common algorithm used for association rule mining.

Working
Find frequent 1-itemsets.
Generate candidate itemsets.
Prune infrequent itemsets.
Repeat until no more frequent itemsets exist.
Generate rules.
Apriori Property
Plain Text
1
If an itemset is frequent,
2
all its subsets must also be frequent.
3
``
Show more lines
Applications
Retail Industry
Plain Text
1
Milk → Bread
Show more lines
E-Commerce
Plain Text
1
Laptop → Mouse
Show more lines
Banking

Customer product recommendations.

Healthcare

Disease pattern discovery.

Web Usage Mining

User navigation pattern analysis.

Advantages
Discovers hidden relationships.
Helps in business decision making.
Improves product placement.
Supports recommendation systems.
Useful for customer behavior analysis.
Limitations
Generates large numbers of rules.
Computationally expensive for large datasets.
May generate uninteresting rules.
Exam Point

Association Rules are data mining techniques used to discover relationships among items in a database. A rule is represented as X → Y and evaluated using Support, Confidence, and Lift. The Apriori Algorithm is the most commonly used algorithm for association rule mining.

## Classification
Classification is a data mining technique used to assign data items to predefined classes or categories based on their attributes.

It is a supervised learning technique because the model is trained using already classified data.

Example
Plain Text
1
Student Result:
2
Marks > 40 → Pass
3
Marks ≤ 40 → Fail
Show more lines
Plain Text
1
Email:
2
Spam
3
Not Spam
Show more lines
Objective of Classification
Predict class labels.
Categorize data into predefined groups.
Support decision making.
Discover patterns in data.
Basic Process of Classification
Step 1: Training Phase

A classification model is built using training data.

Plain Text
1
Training Data
2
↓
3
Classification Model
4
 
Show more lines
Step 2: Testing Phase

The model classifies new data.

Plain Text
1
New Data
2
↓
3
Classification Model
4
↓
5
Predicted Class
Show more lines
Components of Classification
Training Dataset

Contains:

Plain Text
1
Input Attributes
2
+
3
Known Class Labels
Show more lines

Example:

Age	Income	Buy Product25	High	Yes
30	Low	No
Test Dataset

New records whose class must be predicted.

Class Label

Category to which a record belongs.

Examples:

Plain Text
1
Pass / Fail
2
Spam / Not Spam
3
Disease / No Disease
Show more lines
Classification Algorithms
1. Decision Tree

Creates a tree-like structure for classification.

Example:

Plain Text
1
Marks > 40
2
|
3
Yes → Pass
4
No → Fail
Show more lines
Advantages
Easy to understand.
Fast prediction.
Simple implementation.
2. Naïve Bayes Classification

Based on Bayes' Theorem.



Advantages
Fast execution.
Handles large datasets.
Good accuracy.
3. K-Nearest Neighbor (KNN)

Classifies data based on neighboring records.

Example
Plain Text
1
k = 3
Show more lines

Class determined from three nearest neighbors.

4. Neural Networks

Uses interconnected processing nodes.

Applications:

Pattern recognition
Image classification
Speech recognition
Applications of Classification
Education
Plain Text
1
Pass / Fail Prediction
Show more lines
Banking
Plain Text
1
Loan Approval
2
Credit Risk Analysis
Show more lines
Healthcare
Plain Text
1
Disease Prediction
Show more lines
Email Systems
Plain Text
1
Spam Detection
Show more lines
E-Commerce
Plain Text
1
Customer Classification
Show more lines
Advantages
Supports prediction.
Automates decision making.
Handles large data volumes.
Identifies hidden patterns.
Improves business intelligence.
Classification vs Clustering
Classification	ClusteringSupervised Learning	Unsupervised Learning
Uses predefined classes	No predefined classes
Predicts class labels	Groups similar objects
Requires training data	Does not require labeled data
Example

Classification

Plain Text
1
Student → Pass / Fail
Show more lines

Clustering

Plain Text
1
Students grouped by performance levels
Show more lines
Exam Point

Classification is a supervised data mining technique that assigns data items to predefined classes using training data. Common classification algorithms include Decision Trees, Naïve Bayes, K-Nearest Neighbor (KNN), and Neural Networks.

## Clustering
Clustering is a data mining technique used to group similar data objects into clusters such that:

Objects within the same cluster are highly similar.
Objects in different clusters are dissimilar.

It is an unsupervised learning technique because it does not require predefined class labels.

Objective of Clustering
Discover hidden patterns in data.
Group similar objects.
Reduce data complexity.
Support data analysis and decision-making.
Basic Concept
Plain Text
1
Data Objects
2
↓
3
Clustering Algorithm
4
↓
5
Clusters
Show more lines
Example

Student Marks:

Plain Text
1
90, 88, 85
Show more lines

may form:

Plain Text
1
High Performance Cluster
Show more lines

and

Plain Text
1
45, 50, 55
2
``
Show more lines

may form:

Plain Text
1
Average Performance Cluster
Show more lines
Characteristics of Clustering
Unsupervised learning.
No predefined class labels.
Groups similar records.
Helps identify natural groupings in data.
Types of Clustering
1. Partitioning Clustering

Divides data into a fixed number of clusters.

Example
Plain Text
1
K-Means Algorithm
Show more lines
2. Hierarchical Clustering

Creates a hierarchy of clusters.

Agglomerative Method
Plain Text
1
Small Clusters
2
↓
3
Large Clusters
Show more lines
Divisive Method
Plain Text
1
Large Cluster
2
↓
3
Small Clusters
Show more lines
3. Density-Based Clustering

Groups objects based on density.

Example:

Plain Text
1
DBSCAN
Show more lines

Useful for detecting irregularly shaped clusters.

K-Means Clustering
Definition

K-Means is one of the most popular clustering algorithms.

Steps
Select K cluster centers.
Assign each object to the nearest cluster.
Recalculate cluster centers.
Repeat until clusters stabilize.
Example
Plain Text
1
K = 3
Show more lines

Produces three clusters.

Advantages
Simple.
Fast.
Easy implementation.
Disadvantages
Requires K value in advance.
Sensitive to initial cluster selection.
Applications of Clustering
Education
Plain Text
1
Grouping students by performance
Show more lines
Marketing
Plain Text
1
Customer segmentation
Show more lines
Banking
Plain Text
1
Customer behavior analysis
Show more lines
Healthcare
Plain Text
1
Patient grouping
Show more lines
Data Mining
Plain Text
1
Pattern discovery
Show more lines
Clustering vs Classification
Clustering	ClassificationUnsupervised Learning	Supervised Learning
No predefined labels	Uses predefined labels
Groups similar objects	Predicts class labels
Discovers hidden patterns	Uses training data
Example

Clustering

Plain Text
1
Customers grouped by buying behavior
Show more lines

Classification

Plain Text
1
Customer classified as Good or Bad
Show more lines
Advantages
Finds hidden patterns.
No training data required.
Handles large datasets.
Useful for exploratory analysis.
Limitations
Choosing the number of clusters can be difficult.
Results may vary depending on algorithm.
Sensitive to noise and outliers.
Exam Point

Clustering is an unsupervised data mining technique used to group similar data objects into clusters. Popular clustering methods include K-Means, Hierarchical Clustering, and Density-Based Clustering.

## Regression
Regression is a supervised learning technique used to predict a continuous numeric value based on historical data.

Unlike classification, which predicts categories, regression predicts numerical values.

Examples
Predict house prices
Predict rainfall
Predict stock prices
Predict student marks
Predict sales revenue
Objective of Regression
Estimate future values.
Identify relationships between variables.
Analyze trends and patterns.
Support prediction and forecasting.
Basic Concept
Plain Text
1
Input Variables
2
↓
3
Regression Model
4
↓
5
Predicted Numeric Value
Show more lines
Example
Plain Text
1
Study Hours → Exam Marks
Show more lines
Study Hours	Marks2	40
4	60
6	80

Regression predicts marks for a new number of study hours.

Types of Regression
1. Simple Linear Regression

Uses one independent variable and one dependent variable.

Equation
Plain Text
1
Y = a + bX
Show more lines

Where:

Y = Dependent Variable
X = Independent Variable
a = Intercept
b = Slope
Example
Plain Text
1
Marks = 20 + 10 × StudyHours
Show more lines
2. Multiple Linear Regression

Uses multiple independent variables.

Equation
Plain Text
1
Y = a + b1X1 + b2X2 + ... + bnXn
Show more lines
Example
Plain Text
1
House Price =
2
f(Size, Location, Bedrooms)
Show more lines
Applications of Regression
Education
Plain Text
1
Predict student performance.
Show more lines
Banking
Plain Text
1
Predict loan repayment amount.
Show more lines
Business
Plain Text
1
Sales forecasting.
Show more lines
Healthcare
Plain Text
1
Predict patient health indicators.
Show more lines
Finance
Plain Text
1
Stock market prediction.
Show more lines
Regression vs Classification
Regression	ClassificationPredicts numeric values	Predicts categories
Continuous output	Discrete output
Example: House Price	Example: Pass/Fail
Supervised Learning	Supervised Learning
Example

Regression

Plain Text
1
Predict Salary = ₹50,000
Show more lines

Classification

Plain Text
1
Employee = Selected / Not Selected
Show more lines
Advantages
Useful for prediction.
Identifies relationships between variables.
Supports forecasting.
Easy to interpret in simple cases.
Limitations
Sensitive to outliers.
Assumes relationships between variables.
Accuracy depends on data quality.
Exam Point

Regression is a supervised learning technique used to predict continuous numerical values. The most common types are Simple Linear Regression and Multiple Linear Regression. Regression is widely used for prediction, forecasting, and trend analysis.
