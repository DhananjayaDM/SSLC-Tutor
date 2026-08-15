# Programming in C
## Tokens
Tokens are the smallest individual units of a C program that have meaningful significance to the compiler.

A C program consists of a collection of tokens.

Example
C
1
int sum = a + b;
Show more lines

Tokens are:





8
 
Show more lines
Types of Tokens in C
1. Keywords

Keywords are reserved words that have predefined meanings in C.

Examples:

C
1
int
2
float
3
if
4
else
5
for
6
while
7
return
Show more lines

Example:

C
1
int age;
2
 
Show more lines

Here, int is a keyword.

2. Identifiers

Identifiers are names given to variables, functions, arrays, structures, etc.

Examples:

C
1
student
2
total_marks
3
sum
4
calculate
Show more lines

Example:

C
1
int total;
Show more lines

Here, total is an identifier.

Rules for Identifiers
Must begin with a letter or underscore (_).
Can contain letters, digits, and underscores.
Cannot be a keyword.
No special characters allowed.

Valid:

C
1
total
2
_marks
3
num1
Show more lines

Invalid:

C
1
1num
2
float
3
total@
Show more lines
3. Constants

Constants are fixed values that do not change during program execution.

Integer Constants
C
1
10
2
25
3
-5
Show more lines
Floating Constants
C
1
3.14
2
2.5
Show more lines
Character Constants
C
1
'A'
2
'B'
Show more lines
String Constants
C
1
"Hello"
2
"Programming"
Show more lines

Example:

C
1
int x = 100;
Show more lines

Here, 100 is a constant.

4. Operators

Operators perform specific operations on operands.



Logical Operators
C
1
&&
2
||
3
!
Show more lines

Example:

C
1
c = a + b;
Show more lines

Here, = and + are operators.

5. Special Symbols (Separators)

Special symbols are used to separate program elements.

Examples:

C
1
;
2
,
3
()
4
{}
5
[]
6

7
 
Show more lines

Example:

C
1
printf("Hello");
Show more lines

Symbols used:

C
1
(
2
)
3
;
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
int main()
4
{
5
int a = 10;
6
int b = 20;
7
int sum = a + b;
8
 
9
printf("%d", sum);
10
 
11
return 0;
12
}
Show more lines
Tokens Present

Keywords

C
1
int
2
return
Show more lines

Identifiers

C
1
main
2
a
3
b
4
sum
5
printf
Show more lines

Constants

C
1
10
2
20
3
0
4
"%d"
Show more lines

Operators



Special Symbols

C
1

2
<>
3
()
4
{}
5
;
Show more lines
Importance of Tokens
Basic building blocks of a C program.
Help the compiler analyze source code.
Used during lexical analysis.
Essential for program compilation.
Exam Point

Tokens are the smallest meaningful units of a C program. The five types of C tokens are: Keywords, Identifiers, Constants, Operators, and Special Symbols (Separators).

## Identifiers
Identifiers are user-defined names used to identify program elements such as:

Variables
Functions
Arrays
Structures
Pointers
Constants

They help programmers refer to memory locations and program components by meaningful names.

Examples
C
1
int age;
2
float salary;
3
int totalMarks;
Show more lines

Here:

C
1
age
2
salary
3
totalMarks
4
``
Show more lines

are identifiers.

Rules for Naming Identifiers
Must begin with a letter (A-Z, a-z) or underscore (_).
Can contain letters, digits, and underscores.
Cannot start with a digit.
Cannot be a keyword.
No special characters such as @, #, $, %, etc.
C is case-sensitive.
Valid Identifiers
C
1
age
2
_marks
3
student1
4
totalMarks
5
count
Show more lines

Example:

C
1
int student1;
2
float totalMarks;
Show more lines
Invalid Identifiers
C
1
1student
2
total@
3
float
4
student-name
Show more lines

Reasons:

C
1
1student // starts with digit
2
total@ // special character
3
float // keyword
4
student-name // contains hyphen
Show more lines
Types of Identifiers
Variable Identifier
C
1
int count;
Show more lines

count is a variable identifier.

Function Identifier
C
1
int add()
2
{
3
return 0;
4
}
Show more lines

add is a function identifier.

Array Identifier
C
1
int marks[5];
Show more lines

marks is an array identifier.

Structure Identifier
C
1
struct Student
2
{
3
int id;
4
};
Show more lines

Student is a structure identifier.

Case Sensitivity

C treats uppercase and lowercase letters differently.

Example:

C
1
int total;
2
int TOTAL;
Show more lines

These are two different identifiers.

Good Naming Practices

Use meaningful names:

C
1
int studentCount;
2
float averageMarks;
Show more lines

Avoid:

C
1
int a;
2
int x1;
3
 
Show more lines

unless used for temporary purposes.

Example Program
C
1
#include <stdio.h>
2
 
3
int main()
4
{
5
int age = 20;
6
float salary = 25000.50;
7
 
8
printf("%d\n", age);
9
printf("%f", salary);
10
 
11
return
Show more lines

Identifiers used:

C
1
main
2
age
3
salary
4
printf
Show more lines
Exam Point

Identifiers are user-defined names used to represent variables, functions, arrays, structures, and other program elements. They must begin with a letter or underscore, cannot be keywords, and may contain letters, digits, and underscores.

## Data Types
A Data Type specifies the type of data that a variable can store. It determines:

The kind of values that can be stored.
The amount of memory required.
The range of values.
The operations that can be performed.
Example
C
1
int age = 20;
2
float salary = 25000.50;
3
char grade = 'A';
Show more lines
Types of Data Types in C
1. Basic (Primary) Data Types
Integer (int)

Used to store whole numbers.

C
1
int count = 100;
Show more lines

Examples:

Plain Text
1
10
2
25
3
-50
4
1000
Show more lines
Character (char)

Used to store a single character.

C
1
char grade = 'A';
2
 
Show more lines

Examples:

Plain Text
1
'A'
2
'B'
3
'Z'
Show more lines
Floating Point (float)

Used to store decimal numbers.

C
1
float pi = 3.14;
Show more lines

Examples:

Plain Text
1
2.5
2
3.14
3
99.99
Show more lines
Double (double)

Used to store large decimal numbers with greater precision.

C
1
double amount = 12345.6789;
Show more lines
Void (void)

Represents the absence of a value.

Example:

C
1
void display()
2
{
3
}
Show more lines
2. Derived Data Types

These are derived from basic data types.

Array

Collection of similar elements.

C
1
int marks[5];
Show more lines
Pointer

Stores the address of another variable.

C
1
int x = 10;
2
int *p = &x;
Show more lines
Function

A block of code that performs a specific task.

C
1
int add(int a, int *)
2
{
3
return a + b;
4
}
Show more lines
3. User-Defined Data Types

Created by the programmer.

Structure (struct)

Groups different data types together.

C
1
struct Stud*nt
2
{
3
int id;
4
char name[20]*
5
};
Show more lines
Union (union)

Allows different members to share the same memory location.

C
1
uni*n Data
2
{
3
int i;
4
float f;
5
}*
Show more lines
Enumeration (enum)

Used to define a set of named constants.

C
1
enum Day
2
{
3
MON,
4
* TUE,
5
WED
6
};
Show more lines
Typedef

Creates a new name for an existing data type.

C
1
typedef in* Integer;
Show more lines
Size of Common Data Types
Data Type	Typical Sizechar	1 byte
int	4 bytes
float	4 bytes
double	8 bytes
Example Program
C
1
#include <stdio.h>
2
 
3
int main*)
4
{
5
int age = 20;
6
float ma*ks = 85.5;
7
char grade = 'A';
8
 
9
* printf("%d\n", age);
10
printf*"%f\n", marks);
11
printf("%c\n",*grade);
12
 
13
return 0;
14
}
Show more lines
Importance of Data Types
Efficient memory utilization.
Error detection during compilation.
Type safety.
Better program readability.
Faster program execution.
Exam Point

A Data Type specifies the type of value a variable can store. C data types are classified into Basic Data Types (int, char, float, double, void), Derived Data Types (arrays, pointers, functions), and User-Defined Data Types (structure, union, enum, typedef).

## Sequence Control
Sequence Control refers to the mechanism that determines the order in which program instructions are executed by the CPU.

Normally, instructions are executed sequentially, but sequence control allows the flow of execution to change based on conditions, loops, function calls, or branch instructions.

Need for Sequence Control
Controls the flow of program execution.
Supports decision-making.
Enables repetition of instructions.
Allows subroutine and function calls.
Facilitates efficient program design.
Types of Sequence Control
1. Sequential Execution

Instructions are executed one after another in the order they appear.

Example:

C
1
a = 10;
2
b = 20;
3
c = a + b;
Show more lines

Execution order:

Plain Text
1
Statement 1
2
↓
3
Statement 2
4
↓
5
Statement 3
Show more lines
2. Selection Control

Used to choose among different execution paths based on a condition.

if Statement
C
1
if (marks >= 40)
2
{
3
printf("Pass");
4
}
Show more lines
if-else Statement
C
1
if (marks >= 40)
2
{
3
printf("Pass");
4
}
5
else
6
{
7
printf("Fail");
8
}
Show more lines
3. Iteration Control (Loops)

Used to execute a set of statements repeatedly.

for Loop
C
1
for(int i = 1; i <= 5; i++)
2
{
3
printf("%d", i);
4
}
5
 
Show more lines
while Loop
C
1
while(i <= 5)
2
{
3
printf("%d", i);
4
i++;
5
}
Show more lines
do-while Loop
C
1
do
2
{
3
printf("%d", i);
4
i++;
5
}
6
while(i <= 5);
Show more lines
4. Branching Control

Transfers control from one part of a program to another.

break
C
1
break;
Show more lines

Terminates a loop or switch statement.

continue
C
1
continue;
Show more lines

Skips the current iteration and proceeds to the next iteration.

goto
C
1
goto label;
Show more lines

Transfers control to a labeled statement.

Example:

C
1
goto end;
2
 
3
end:
4
printf("Done");
Show more lines
5. Function Call Control

Transfers execution to a function and returns control after execution.

Example:

C
1
int add(int a, int b)
2
{
3
return a + b;
4
}
5
 
6
int result = add(10, 20);
Show more lines
Sequence Control in Basic Computer

Common instructions used for sequence control:

BUN (Branch Unconditionally)
Plain Text
1
PC ← Address
Show more lines

Transfers control unconditionally.

BSA (Branch and Save Return Address)
Plain Text
1
Used for subroutine calls.
Show more lines
ISZ (Increment and Skip if Zero)
Plain Text
1
Increment memory word and skip next instruction if result is zero.
Show more lines

Used in loop control.

Advantages
Provides flexibility in program execution.
Supports decision-making and repetition.
Enables modular programming.
Improves program efficiency.
Applications
Looping operations
Decision-making programs
Subroutines and functions
Operating systems
Embedded systems
Exam Point

Sequence Control is the mechanism that determines the order of instruction execution in a program. It includes sequential execution, selection, iteration, branching, and function/subroutine control. In a basic computer, sequence control is achieved using instructions such as BUN, BSA, and ISZ.

## Subprogram Control
Subprogram Control refers to the mechanism used to transfer program execution from the main program to a subprogram (subroutine/function/procedure) and then return control back to the calling program after the subprogram finishes execution.

Subprograms help divide a large program into smaller, manageable modules.

Need for Subprogram Control
Reduces code duplication.
Improves program modularity.
Simplifies debugging and maintenance.
Encourages code reusability.
Makes programs easier to understand.
Subprogram

A Subprogram is a self-contained block of instructions designed to perform a specific task.

Examples:

Function
Procedure
Subroutine
Operation of Subprogram Control
1. Call the Subprogram

Control is transferred from the main program to the subprogram.

2. Execute the Subprogram

The instructions in the subprogram are executed.

3. Return Control

Execution returns to the instruction immediately following the call.

Example
C
1
#include <stdio.h>
2
 
3
int add(int a, int b)
4
{
5
return a + b;
6
}
7
 
8
int main()
9
{
10
int sum = add(10, 20);
11
printf("%d", sum);
12
return 0;
13
}
Show more lines

Here:

main() is the calling program.
add() is the subprogram.
Control returns to main() after execution.
Subprogram Control in Basic Computer
BSA (Branch and Save Return Address)

Used to call a subroutine.

Plain Text
1
BSA SUBR
Show more lines

Operation:

Plain Text
1
M[SUBR] ← PC
2
PC ← SUBR + 1
Show more lines
Saves the return address.
Transfers control to the subroutine.
Return from Subroutine
Plain Text
1
BUN I SUBR
Show more lines

Operation:

Plain Text
1
PC ← M[SUBR]
Show more lines
Retrieves the saved return address.
Returns control to the calling program.
Advantages
Code reusability.
Reduced program size.
Easier testing and debugging.
Better program organization.
Simplified maintenance.
Applications
Mathematical computations
Input/Output processing
Operating systems
Embedded systems
Library functions
Exam Point

Subprogram Control is the process of transferring execution from a main program to a subprogram and returning back after completion. In a Basic Computer, subprogram control is achieved using the BSA (Branch and Save Return Address) instruction for calling a subroutine and BUN I for returning from it.

## Arrays
An Array is a collection of elements of the same data type stored in contiguous memory locations and accessed using a common name with an index.

Arrays are used to store multiple values in a single variable.

Example
C
1
int marks[5] = {70, 80, 90, 85, 75};
Show more lines

Here:

marks is the array name.
5 is the size of the array.
marks[0] to marks[4] are the elements.
Features of Arrays
Stores multiple values of the same type.
Elements are stored in consecutive memory locations.
Accessed using an index.
Index starts from 0 in C.
Fixed size once declared.
Declaration of an Array
Syntax
C
1
data_type array_name[size];
Show more lines
Example
C
1
int num[10];
Show more lines

Declares an array capable of storing 10 integers.

Array Initialization
At Declaration Time
C
1
int num[5] = {10, 20, 30, 40, 50};
Show more lines
Partial Initialization
C
1
int num[5] = {10, 20};
Show more lines

Remaining elements become 0.

Accessing Array Elements
Syntax
C
1
array_name[index]
Show more lines
Example
C
1
int marks[3] = {70, 80, 90};
2
 
3
printf("%d", marks[1]);
Show more lines

Output:

Plain Text
1
80
Show more lines
Memory Representation
Plain Text
1
marks[0] = 70
2
marks[1] = 80
3
marks[2] = 90
4
marks[3] = 85
5
marks[4] = 75
Show more lines

Elements are stored in continuous memory locations.

Types of Arrays
1. One-Dimensional Array

Stores data in a single list.

C
1
int a[5] = {1, 2, 3, 4, 5};
Show more lines
2. Two-Dimensional Array

Stores data in rows and columns.

C
1
int matrix[2][3] = {
2
{1, 2, 3},
3
{4, 5, 6}
4
};
Show more lines

Representation:

Plain Text
1
1 2 3
2
4 5 6
Show more lines
3. Multi-Dimensional Array

Array with more than two dimensions.

C
1
int arr[2][3][4];
Show more lines
Operations on Arrays
Traversal

Accessing each element.

C
1
for(int i = 0; i < 5; i++)
2
{
3
printf("%d ", marks[i]);
4
}
Show more lines
Insertion

Adding an element at a specified position.

Deletion

Removing an element from an array.

Searching

Finding an element.

Example:

C
1
if(marks[i] == 80)
Show more lines
Sorting

Arranging elements in ascending or descending order.

Advantages
Stores multiple values using one variable.
Easy processing using loops.
Fast access using index values.
Efficient memory organization.
Disadvantages
Fixed size.
Can store only similar data types.
Insertion and deletion are costly.
Applications
Storing student marks.
Matrix operations.
Searching and sorting algorithms.
Data processing applications.
Scientific and engineering computations.
Exam Point

An Array is a collection of elements of the same data type stored in contiguous memory locations and accessed using an index. Arrays may be one-dimensional, two-dimensional, or multidimensional.

## Structures
A Structure is a user-defined data type in C that allows grouping of different types of data under a single name.

Unlike arrays, which store only similar data types, a structure can store variables of different data types.

Example
C
1
struct Student
2
{
3
int id;
4
char name[20];
5
float marks;
6
};
Show more lines

Here, Student contains:

Integer (id)
Character array (name)
Float (marks)
Need for Structures
Store related data together.
Represent real-world entities.
Improve program organization.
Simplify handling of complex data.
Declaration of a Structure
Syntax
C
1
struct structure_name
2
{
3
data_type member1;
4
data_type member2;
5
};
Show more lines
Example
C
1
struct Employee
2
{
3
int empId;
4
char name[30];
5
float salary;
6
};
Show more lines
Creating Structure Variables
C
1
struct Employee emp1;
Show more lines

Or

C
1
struct Employee emp1, emp2;
Show more lines
Accessing Structure Members

The dot operator (.) is used to access members.

Example
C
1
emp1.empId = 101;
2
emp1.salary = 25000.50;
Show more lines
Complete Example
C
1
#include <stdio.h>
2
 
3
struct Student
4
{
5
int rollNo;
6
char grade;
7
float marks;
8
};
9
 
10
int main()
11
{
12
struct Student s1;
13
 
14
s1.rollNo = 1;
15
s1.grade = 'A';
16
s1.marks = 89.5;
17
 
18
printf("%d\n", s1.rollNo);
19
printf("%c\n", s1.grade);
20
printf("%.2f\n", s1.marks);
21
 
22
return 0;
23
}
Show more lines
Initialization of Structure
C
1
struct Student s1 = {1, 'A', 89.5};
Show more lines
Array of Structures

Used to store multiple records.

C
1
struct Student s[3];
Show more lines

Example:

C
1
s[0].rollNo = 1;
2
s[1].rollNo = 2;
Show more lines
Nested Structures

A structure can contain another structure.

C
1
struct Address
2
{
3
char city[20];
4
};
5
 
6
struct Student
7
{
8
int id;
9
struct Address addr;
10
};
Show more lines
Structure and Functions
Passing Structure to Function
C
1
void display(struct Student s)
2
{
3
printf("%d", s.id);
4
}
Show more lines
Structure vs Array
Feature	Structure	ArrayData Type	Different types allowed	Same type only
Access	Using member names	Using index
Purpose	Represents records	Represents list of values
Advantages
Groups related data together.
Supports complex data representation.
Improves readability.
Facilitates record management.
Applications
Student records
Employee records
Banking systems
Database applications
Inventory management systems
Exam Point

A Structure is a user-defined data type in C that groups variables of different data types under a single name. Members of a structure are accessed using the dot (.) operator.

## Union
A Union is a user-defined data type in C that allows different data members to share the same memory location.

Unlike a structure, where each member gets separate memory, all members of a union use the same memory space.

Syntax
C
1
union union_name
2
{
3
data_type member1;
4
data_type member2;
5
...
6
};
Show more lines
Example
C
1
union Data
2
{
3
int i;
4
float f;
5
char ch;
6
};
Show more lines
Creating Union Variables
C
1
union Data d1;
Show more lines
Accessing Union Members

Use the dot (.) operator.

C
1
d1.i = 100;
2
printf("%d", d1.i);
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
union Data
4
{
5
int i;
6
float f;
7
char ch;
8
};
9
 
10
int main()
11
{
12
union Data d;
13
 
14
d.i = 100;
15
printf("i = %d\n", d.i);
16
 
17
d.f = 10.5;
18
printf("f = %.2f\n", d.f);
19
 
20
return 0;
21
}
Show less
Memory Allocation
C
1
union Data
2
{
3
int i; // 4 bytes
4
float f; // 4 bytes
5
char ch; // 1 byte
6
};
Show more lines

The union size equals the size of its largest member.

Plain Text
1
Union Size = 4 bytes
Show more lines

because int and float require 4 bytes.

Important Feature

Since all members share the same memory:

C
1
union Data d;
2
 
3
d.i = 100;
4
d.f = 5.5;
Show more lines

After assigning d.f, the value of d.i is overwritten.

Only one member can contain a valid value at a time.

Union vs Structure
Feature	Union	StructureMemory Allocation	Shared memory	Separate memory
Size	Size of largest member	Sum of all member sizes
Simultaneous Storage	One member at a time	All members at a time
Memory Usage	Efficient	More memory required
Example

Structure

C
1
struct Student
2
{
3
int id;
4
float marks;
5
};
6
 
Show more lines

Memory:

Plain Text
1
id -> separate memory
2
marks -> separate memory
Show more lines

Union

C
1
union Student
2
{
3
int id;
4
float marks;
5
};
Show more lines

Memory:

Plain Text
1
id and marks share same memory
Show more lines
Advantages
Efficient memory utilization.
Useful when only one value is needed at a time.
Reduces memory requirements.
Suitable for embedded systems.
Disadvantages
Only one member can store a valid value at a time.
Can lead to data overwriting.
More difficult to debug.
Applications
Memory-efficient programming.
Embedded systems.
Device drivers.
Communication protocols.
Hardware interfacing.
Exam Point

A Union is a user-defined data type in C in which all members share the same memory location. The size of a union is equal to the size of its largest member, and only one member can hold a valid value at a time.

## String
A String is a collection of characters stored in a character array and terminated by a special null character '\0'.

In C, strings are not a separate data type; they are represented using character arrays.

Example
C
1
char name[] = "Hello";
Show more lines

Memory representation:

Plain Text
1
H e l l o \0
Show more lines

The null character '\0' indicates the end of the string.

String Declaration
Method 1
C
1
char name[10];
Show more lines
Method 2
C
1
char name[] = "Hello";
Show more lines
Method 3
C
1
char name[6] = {'H','e','l','l','o','\0'};
Show more lines
Reading and Displaying Strings
Using scanf()
C
1
char name[20];
2
 
3
scanf("%s", name);
4
printf("%s", name);
Show more lines
Using gets() and puts()
C
1
gets(name);
2
puts(name);
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
int main()
4
{
5
char name[] = "Programming";
6
 
7
printf("%s", name);
8
 
9
return 0;
10
}
Show more lines

Output:

Plain Text
1
Programming
Show more lines
Common String Functions

The header file used is:

C
1
#include <string.h>
Show more lines
strlen()

Returns the length of a string.

C
1
strlen("Hello")
Show more lines

Output:

Plain Text
1
5
Show more lines
strcpy()

Copies one string into another.

C
1
strcpy(str2, str1);
Show more lines

Example:

C
1
strcpy(name, "John");
Show more lines
strcat()

Concatenates two strings.

C
1
strcat(str1, str2);
2
 
Show more lines

Example:

C
1
strcat("Hello", "World");
Show more lines

Result:

Plain Text
1
HelloWorld
Show more lines
strcmp()

Compares two strings.

C
1
strcmp(str1, str2);
Show more lines

Returns:

Plain Text
1
0 -> Strings are equal
2
<0 -> First string is smaller
3
>0 -> First string is greater
Show more lines
String vs Character Array
Feature	String	Character ArrayContains	Characters + '\0'	Characters
End Marker	Null character	May not have null character
Library Support	Yes	Limited
Advantages
Easy storage of text data.
Supported by many library functions.
Easy manipulation and processing.
Applications
Storing names
Messages and text processing
Password handling
File processing
Database applications
Exam Point

A String in C is a sequence of characters terminated by the null character '\0'. Strings are stored in character arrays and manipulated using functions available in the <string.h> library.

## Functions
A Function is a self-contained block of code that performs a specific task. Functions help divide a large program into smaller, manageable, and reusable modules.

Advantages of Functions
Code reusability
Reduced program size
Easier debugging
Improved readability
Modular programming
Syntax
C
1
return_type function_name(parameters)
2
{
3
// statements
4
return value;
5
}
Show more lines
Example
C
1
int add(int a, int b)
2
{
3
return a + b;
4
}
Show more lines
Function Components
Function Declaration (Prototype)

Informs the compiler about the function.

C
1
int add(int, int);
Show more lines
Function Definition

Contains the actual code.

C
1
int add(int a, int b)
2
{
3
return a + b;
4
}
Show more lines
Function Call

Invokes the function.

C
1
sum = add(10, 20);
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
int add(int, int);
4
 
5
int main()
6
{
7
int sum;
8
 
9
sum = add(10, 20);
10
 
11
printf("Sum = %d", sum);
12
 
13
return 0;
14
}
15
 
16
int add(int a, int b)
17
{
18
return a + b;
19
}
Show less

Output:

Plain Text
1
Sum = 30
Show more lines
Types of Functions
1. Library Functions

Predefined functions provided by C libraries.

Examples:

C
1
printf()
2
scanf()
3
strlen()
4
sqrt()
Show more lines

Example:

C
1
printf("Hello");
Show more lines
2. User-Defined Functions

Functions created by the programmer.

Example:

C
1
int square(int n)
2
{
3
return n * n;
4
}
Show more lines
Categories of Functions
No Arguments, No Return Value
C
1
void display()
2
{
3
printf("Hello");
4
}
Show more lines
Arguments, No Return Value
C
1
void add(int a, int b)
2
{
3
printf("%d", a + b);
4
}
Show more lines
No Arguments, Return Value
C
1
int getNumber()
2
{
3
return 100;
4
}
Show more lines
Arguments and Return Value
C
1
int add(int a, int b)
2
{
3
return a + b;
4
}
Show more lines
Parameter Types
Formal Parameters

Parameters in function definition.

C
1
int add(int a, int b)
Show more lines

a and b are formal parameters.

Actual Parameters

Values passed during function call.

C
1
add(10, 20);
Show more lines

10 and 20 are actual parameters.

Call by Value

A copy of the variable is passed.

C
1
void fun(int x)
2
{
3
x = 100;
4
}
Show more lines

Original variable remains unchanged.

Call by Reference

Address of the variable is passed using pointers.

C
1
void fun(int *x)
2
{
3
*x = 100;
4
}
Show more lines

Original variable is modified.

Recursive Function

A function that calls itself.

Example
C
1
int factorial(int n)
2
{
3
if(n == 1)
4
return 1;
5
 
6
return n * factorial(n - 1);
7
}
Show more lines

For:

C
1
factorial(5)
Show more lines

Output:

Plain Text
1
120
Show more lines
Function vs Library Function
User-Defined Function	Library FunctionCreated by programmer	Predefined
Written as needed	Available in libraries
Example: add()	Example: printf()
Applications
Mathematical calculations
Sorting and searching
String processing
File handling
Modular software development
Exam Point

A Function is a named block of code that performs a specific task. Functions may be library functions or user-defined functions and help achieve modularity, code reusability, and easier program maintenance.

## File Handling
File Handling is the process of storing, retrieving, and manipulating data in files using a C program. It allows data to be stored permanently on secondary storage devices such as hard disks and SSDs.

Need for File Handling
Permanent data storage.
Large data storage.
Data sharing between program executions.
Backup and record maintenance.
File Pointer

In C, a file is handled through a pointer of type FILE.

Declaration
C
1
FILE *fp;
Show more lines
Opening a File
Syntax
C
1
fp = fopen("filename", "mode");
Show more lines
Example
C
1
FILE *fp;
2
 
3
fp = fopen("data.txt", "r");
Show more lines
File Opening Modes
Mode	Meaning"r"	Read
"w"	Write
"a"	Append
"r+"	Read and Write
"w+"	Read and Write (overwrite file)
"a+"	Read and Append
Closing a File
Syntax
C
1
fclose(fp);
Show more lines
Example
C
1
fclose(fp);
Show more lines
Writing to a File
Using fprintf()
C
1
FILE *fp;
2
 
3
fp = fopen("data.txt",*"w");
4
 
5
fprintf(fp, "Hello World");*
6
fclose(fp);
Show more lines
Reading from a File
Using fscanf()
C
1
FILE *fp;
2
char name[20];
3
 
4
fp =*fopen("data.txt", "r");
5
 
6
fscanf(fp* "%s", name);
7
 
8
printf("%s", name);*
9
fclose(fp);
Show more lines
Character-Oriented File Functions
fputc()

Writes a character to a file.

C
1
fputc('A', fp);
Show more lines
fgetc()

Reads a character from a file.

C
1
ch = fgetc(fp);
Show more lines
String-Oriented File Functions
fputs()

Writes a string to a file.

C
1
fputs("Hello", fp);
2
*
Show more lines
fgets()

Reads a string from a file.

C
1
fgets(str, 50, f*);
Show more lines
End of File (EOF)

EOF indicates the end of a file.

Example:

C
1
while((ch = fgetc(fp*) != EOF)
2
{
3
printf("%c", ch);
4
*
Show more lines
Example Program: Writing to a File
C
1
#include <stdi*.h>
2
 
3
int main()
4
{
5
FILE *fp;
6
 
7
* fp = fopen("data.txt", "w");
8
 
9
* fprintf(fp, "Welcome to C Program*ing");
10
 
11
fclose(fp);
12
 
13
retur* 0;
14
}
Show more lines
Example Program: Reading from a File
C
1
#includ* <stdio.h>
2
 
3
int main()
4
{
5
FILE *fp;
6
char str[100];
7
 
8
fp = f*pen("data.txt", "r");
9
 
10
fgets(s*r, 100, fp);
11
 
12
printf("%s", str*;
13
 
14
fclose(fp);
15
 
16
return 0;
17
*
Show less
File Operations
Create File
C
1
fopen("data.txt"* "w");
Show more lines
Read File
C
1
fo*en("data.txt", "r");
Show more lines
Write File
C
1
fprintf(fp, "...");
2
`*
Show more lines
Append Data
C
1
fopen("da*a.txt", "a");
Show more lines
Close File
C
1
fclose(fp);
Show more lines
Advantages of File Handling
Permanent storage of data.
Large data capacity.
Easy data retrieval.
Data sharing between programs.
Backup and record maintenance.
Applications
Student record systems
Banking applications
Inventory management
Employee databases
Library management systems
Exam Point

File Handling in C is the process of storing and retrieving data from files using file pointers and file functions. The main functions are fopen(), fclose(), fprintf(), fscanf(), fgetc(), fputc(), fgets(), and fputs().

## Command Line Arguments
Command Line Arguments are values passed to a program at the time of execution through the command line.

They allow users to provide input to a program without using scanf() or other input functions.

Syntax

Command line arguments are received through the main() function:

C
1
int main(int argc, char *argv[])
2
{
3
// statements
4
}
Show more lines

or

C
1
int main(int argc, char **argv)
2
{
3
// statements
4
}
5
 
Show more lines
Parameters
argc (Argument Count)
Stores the number of command line arguments.
Includes the program name.

Example:

Plain Text
1
program hello world
Show more lines
C
1
argc = 3
Show more lines
argv (Argument Vector)
Array of pointers to strings.
Stores the command line arguments.

Example:

Plain Text
1
program hello world
Show more lines
C
1
argv[0] = "program"
2
argv[1] = "hello"
3
argv[2] = "world"
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
int main(int argc, char *argv[])
4
{
5
printf("Number of Arguments = %d\n", argc);
6
 
7
for(int i = 0; i < argc; i++)
8
{
9
printf("%s\n", argv[i]);
10
}
11
 
12
return 0;
13
}
Show more lines
Execution
Plain Text
1
program India Karnataka
Show more lines
Output
Plain Text
1
Number of Arguments = 3
2
 
3
program
4
India
5
Karnataka
Show more lines
Example: Addition of Two Numbers
C
1
#include <stdio.h>
2
#include <stdlib.h>
3
 
4
int main(int argc, char *argv[])
5
{
6
int a = atoi(argv[1]);
7
int b = atoi(argv[2]);
8
 
9
printf("Sum = %d", a + b);
10
 
11
return 0;
12
}
Show more lines
Execution
Plain Text
1
program 10 20
Show more lines
Output
Plain Text
1
Sum = 30
Show more lines
Advantages
Input can be provided during execution.
Avoids repeated input statements.
Useful for automation and scripting.
Convenient for batch processing.
Applications
Compiler commands
Operating system utilities
Batch processing programs
Script execution
File processing utilities
Exam Point

Command Line Arguments are parameters passed to a program during execution. They are received through main(int argc, char *argv[]), where argc stores the number of arguments and argv stores the argument values as strings.

## Preprocessors
A Preprocessor is a program that processes the source code before actual compilation begins. Preprocessor directives start with the # symbol and are executed before the compiler translates the program.

Features of Preprocessors
Executed before compilation.
Begin with #.
Do not end with a semicolon (;).
Used for file inclusion, macros, and conditional compilation.
Common Preprocessor Directives
1. #include

Used to include header files in a program.

Syntax

C
1
#include <stdio.h>
Show more lines

or

C
1
#include "myfile.h"
Show more lines

Example

C
1
#include <stdio.h>
2
 
3
int main()
4
{
5
printf("Hello");
6
return 0;
7
}
Show more lines
2. #define

Used to define constants or macros.

Syntax

C
1
#define PI 3.14
2
 
Show more lines

Example

C
1
#include <stdio.h>
2
#define PI 3.14
3
 
4
int main()
5
{
6
printf("%f", PI);
7
return 0;
8
}
Show more lines
3. Macro with Arguments

Macros can accept parameters.

Example

C
1
#define SQUARE(x) ((x) * (x))
Show more lines

Usage:

C
1
int result = SQUARE(5);
Show more lines

Output:

Plain Text
1
25
Show more lines
4. #undef

Used to remove a previously defined macro.

Example

C
1
#define SIZE 100
2
#undef SIZE
Show more lines
5. Conditional Compilation

Used to compile selected parts of a program.

#if
C
1
#define NUM 10
2
 
3
#if NUM > 5
4
printf("Greater");
5
#endif
Show more lines
#ifdef

Checks whether a macro is defined.

C
1
#define TEST
2
 
3
#ifdef TEST
4
printf("Defined");
5
#endif
Show more lines
#ifndef

Checks whether a macro is not defined.

C
1
#ifndef TEST
2
printf("Not Defined");
3
#endif
Show more lines
#else
C
1
#ifdef TEST
2
printf("Defined");
3
#else
4
printf("Not Defined");
5
#endif
Show more lines
6. #error

Generates a compilation error.

C
1
#error Invalid Configuration
2
 
Show more lines
7. #pragma

Provides special instructions to the compiler.

C
1
#pragma warning(disable:4996)
Show more lines

Compiler-specific behavior may vary.

Example Program
C
1
#include <stdio.h>
2
 
3
#define PI 3.14159
4
 
5
int main()
6
{
7
float radius = 5;
8
 
9
printf("Area = %f", PI * radius * radius);
10
 
11
return 0;
12
}
Show more lines
Advantages of Preprocessors
Code reusability.
Easier maintenance.
Reduces repetition.
Supports conditional compilation.
Simplifies constant definition.
Applications
Header file inclusion.
Macro creation.
Debugging.
Platform-specific programming.
Library development.
Exam Point

A Preprocessor is a program that processes source code before compilation. Common preprocessor directives are #include, #define, #undef, #if, #ifdef, #ifndef, #else, and #pragma.


## Pointers
A Pointer is a variable that stores the memory address of another variable.

Instead of storing a value directly, a pointer stores the location where the value is stored.

Example
C
1
int x = 10;
2
int *p = &x;
Show more lines

Here:

x stores the value 10
&x gives the address of x
p stores the address of x
Pointer Declaration
Syntax
C
1
data_type *pointer_name;
Show more lines
Example
C
1
int *p;
2
float *f;
3
char *c;
Show more lines
Pointer Initialization
C
1
int x = 10;
2
int *p = &x;
Show more lines

Memory representation:

Plain Text
1
x = 10
2
 
3
p ------> x
4
```*
Show more lines
Address Operator (&)

Used to obtain the address of a variable.

C
1
int x = 10;
2
 
3
printf("%p", &x);
4
```*
Show more lines
Indirection Operator (*)

Used to access the value stored at the address contained in the pointer.

C
1
*nt x = 10;
2
int *p = &**
3
 
4
printf("%d", *p);
Show more lines

Output:

Plain Text
1
10
Show more lines
Example Program
C
1
#include <stdio.h>
2
 
3
int *ain()
4
{
5
int x = 10;
6
int *p*= &x;
7
 
8
printf("Value of x = %d*n", x);
9
printf("Address of x =*%p\n", &x);
10
printf("Value stor*d in p = %p\n", p);
11
printf("Va*ue pointed by p = %d\n", *p);
12
 
13
*
Show more lines
Pointer and Variable Relationship
C
1
int * = 50;
2
int *p = &x;
Show more lines
Plain Text
1
x*= 50
2
p = address of x
3
*p = 50
Show more lines
Changing Value Using Pointer
C
1
int x = 10;
2
int *p = &x;
3
 
4
*p = 20;
Show more lines

Now:

Plain Text
1
x = 20
2
*
Show more lines

because the pointer modified the original variable.

Null Pointer

A pointer that does not point to any valid memory location.

C
1
int *p = NULL;
Show more lines

Used to indicate an empty pointer.

Pointer Arithmetic
Increment
C
1
p++;
Show more lines

Moves the pointer to the next memory location of its type.

Decrement
C
1
p--;
Show more lines

Moves the pointer to the previous memory location.

Pointers and Arrays

Array name itself acts as a pointer to the first element.

C
1
int arr[3] = {10, 20, 30};
2
 
3
in* *p = arr;
Show more lines

Access elements:

C
1
printf("%d", *(p + 1));
Show more lines

Output:

Plain Text
1
20
Show more lines
Pointer to Pointer

A pointer can store the address of another pointer.

C
1
int x = 10;
2
int *p = &x;
3
int **q = &p;
Show more lines
Plain Text
1
q → p → x
2
```*
Show more lines

Access value:

C
1
printf("%d", **q);
Show more lines

Output:

Plain Text
1
10
Show more lines
Advantages of Pointers
Dynamic memory allocation.
Efficient array handling.
Function parameter passing.
Supports data structures.
Reduces memory usage in some applications.
Applications
Dynamic memory management
Arrays and strings
Linked lists
Trees and graphs
Function arguments
System programming
Pointer vs Variable
Feature	Variable	PointerStores	Value	Address
Access	Direct	Indirect
Example	int x = 10;	int *p = &x;
Exam Point

A Pointer is a variable that stores the memory address of another variable. The address operator (&) is used to obtain an address, and the indirection operator (*) is used to access the value stored at that address.
Functions.



