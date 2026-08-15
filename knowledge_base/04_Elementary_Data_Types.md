# Elementary Data Types
## Properties of Types and Objects
Elementary Data Types are the basic built-in data types provided by a programming language to represent simple values.

Examples:

Integer (int)
Real/Floating Point (float, double)
Character (char)
Boolean (bool)
Data Type

A Data Type defines:

The kind of values that can be stored.
The operations that can be performed on those values.
The memory required for storing them.

Example:

C
1
int age = 25;
2
float salary = 45000.50;
3
char grade = 'A';
Show more lines
Object

An Object is a memory location that stores a value of a particular data type.

Example:

C
1
int count = 10;
Show more lines
Type → int
Object → count
Value → 10
Properties of Data Types
1. Domain

The set of values that a type can store.

Example:

Plain Text
1
Boolean → {True, False}
Show more lines
Plain Text
1
Integer → {-∞ ... +∞} (within implementation limits)
Show more lines
2. Range

The minimum and maximum values allowed.

Example:

Plain Text
1
8-bit signed integer:
2
-128 to +127
3
 
Show more lines
3. Size

Amount of memory required.

Example:

Plain Text
1
char → 1 byte
2
int → 4 bytes
3
float → 4 bytes
4
double → 8 bytes
5
`
Show more lines
4. Operations

Permitted operations on the type.

For integers:

Plain Text
1
+
2
-
3
*
4
/
5
%
Show more lines

For Boolean values:

Plain Text
1
AND
2
OR
3
NOT
Show more lines
Properties of Objects
1. Name

Identifier used to access the object.

Example:

C
1
int marks;
Show more lines

marks is the object name.

2. Type

Determines the kind of data stored.

Example:

C
1
float price;
Show more lines

Type = float

3. Value

Current data stored in the object.

Example:

C
1
int x = 50;
Show more lines

Value = 50

4. Address

Memory location where the object is stored.

Example:

C
1
int x = 10;
Show more lines

x occupies a specific memory address.

5. Lifetime

Duration for which the object exists in memory.

Example:

Local variables exist until a function ends.
Global variables exist throughout program execution.
6. Scope

Region of the program where the object can be accessed.

Example:

C
1
void fun() {
2
int x = 5;
3
}
Show more lines

x is accessible only inside fun().

Common Elementary Data Types
Integer

Stores whole numbers.

Example:

C
1
int age = 25;
Show more lines
Floating Point

Stores decimal numbers.

Example:

C
1
float pi = 3.14;
Show more lines
Character

Stores a single character.

Example:

C
1
char grade = 'A';
Show more lines
Boolean

Stores logical values.

Example:

C
1
bool result = true;
Show more lines
Importance of Data Types
Efficient memory usage.
Error detection.
Type safety.
Better program reliability.
Faster execution.
Exam Point

Elementary Data Types are the basic data types such as Integer, Float, Character, and Boolean. A data type defines the set of values, operations, size, and range, while an object is a memory location characterized by properties such as name, type, value, address, lifetime, and scope.

##  Scalar and Composite Data Types
Scalar Data Types

A Scalar Data Type is a data type that can store only a single value at a time.

Characteristics
Represents one value.
Cannot be divided into smaller components.
Simple and basic data types.
Directly operated upon by the processor.
Examples

Integer

C
1
int age = 25;
Show more lines

Float

C
1
float price = 99.5;
2
 
Show more lines

Character

C
1
char grade = 'A';
Show more lines

Boolean

C
1
bool result = true;
2
 
Show more lines
Advantages
Simple to use.
Fast processing.
Requires less memory management.
Composite Data Types

A Composite Data Type is a data type that is formed by combining two or more scalar data items into a single unit.

Characteristics
Can store multiple values.
Consists of different or similar data types.
Used to represent complex data structures.
Examples
Array

Collection of similar data elements.

C
1
int marks[5] = {70, 80, 90, 85, 75};
Show more lines
Structure

Collection of different data types.

C
1
struct Student {
2
int id;
3
char name[20];
4
float marks;
5
};
Show more lines
Record

Stores related fields together.

Example:

Plain Text
1
Student Record
2
- Roll Number
3
- Name
4
- Marks
Show more lines
Class

Used in Object-Oriented Programming.

Java
1
class Student {
2
int id;
3
String name;
4
}
5
 
Show more lines
Scalar vs Composite Data Types
Feature	Scalar Data Type	Composite Data TypeValues Stored	Single value	Multiple values
Complexity	Simple	Complex
Components	Cannot be subdivided	Composed of multiple elements
Examples	int, float, char, bool	Array, Structure, Record, Class
Memory Requirement	Less	More
Examples
Scalar
C
1
int x = 10;
Show more lines

Stores only one value: 10

Composite
C
1
int numbers[4] = {10, 20, 30, 40};
Show more lines

Stores multiple values in a single variable.

Exam Point

Scalar Data Types store a single value at a time, such as Integer, Float, Character, and Boolean. Composite Data Types are formed by combining multiple data items into a single structure, such as Arrays, Structures, Records, and Classes.
