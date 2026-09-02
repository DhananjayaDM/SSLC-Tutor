# Programming in C++
## Tokens
Tokens are the smallest meaningful units of a program that are recognized by the compiler.

A C program is made up of tokens.

Example
C
1
int sum = a + b;
Show more lines

Tokens:







Types of Tokens in C
1. Keywords

Reserved words with predefined meanings.

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
while
6
return
Show more lines

Example:

C
1
int age;
Show more lines

int is a keyword.

2. Identifiers

Names given to variables, functions, arrays, etc.

Example:

C
1
int totalMarks;
Show more lines

totalMarks is an identifier.

3. Constants

Fixed values that do not change during program execution.

Examples:

C
1
10
2
3.14
3
'A'
4
"Hello"
Show more lines

Example:

C
1
int x = 100;
Show more lines

100 is a constant.

4. Operators

Symbols used to perform operations.

Examples:



Example:

C
1
c = a + b;
Show more lines

= and + are operators.

5. Special Symbols (Separators)

Used to separate program elements.

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

Example
C
1
int a = 10;
Show more lines

Tokens are:

Plain Text
1
int → Keyword
2
a → Identifier
3
= → Operator
4
10 → Constant
5
; → Special Symbol
Show more lines
Exam Point

Tokens are the smallest meaningful units of a C program. The five types of tokens are Keywords, Identifiers, Constants, Operators, and Special Symbols.

## Identifiers
Identifiers are user-defined names used to identify variables, functions, arrays, structures, classes, objects, etc., in a program.

They help programmers refer to program elements using meaningful names.

Example
C
1
int age;
2
float salary;
Show more lines

Here:

Plain Text
1
age
2
salary
Show more lines

are identifiers.

Rules for Naming Identifiers
Must start with a letter or underscore (_).
Can contain letters, digits, and underscores.
Cannot start with a digit.
Cannot be a keyword.
Cannot contain special characters such as @, #, %, -.
C is case-sensitive.
Valid Identifiers
C
1
count
2
student1
3
_total
4
marks
5
employeeName
Show more lines

Example:

C
1
int student1;
2
float employeeSalary;
Show more lines
Invalid Identifiers
C
1
1count
2
float
3
student-name
4
total@
Show more lines

Reasons:

Plain Text
1
1count → Starts with a digit
2
float → Keyword
3
student-name → Contains '-'
4
total@ → Contains '@'
Show more lines
Examples
Variable Identifier
C
1
int age;
Show more lines

age is an identifier.

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
5
 
Show more lines

add is an identifier.

Array Identifier
C
1
int marks[5];
Show more lines

marks is an identifier.

Structure Identifier
C
1
struct Student
2
{
3
};
Show more lines

Student is an identifier.

Case Sensitivity
C
1
int total;
2
int TOTAL;
Show more lines

These are treated as different identifiers.

Good Naming Practices
C
1
int studentCount;
2
float averageMarks;
3
char grade;
Show more lines

Use meaningful names that describe the purpose of the variable or function.

Exam Point

Identifiers are user-defined names used to represent variables, functions, arrays, structures, and other program elements. An identifier must begin with a letter or underscore, may contain digits, and cannot be a keyword.

## variables and Constants
A Variable is a named memory location used to store data whose value can change during program execution.

Syntax
C
1
data_type variable_name;
Show more lines
Example
C
1
int age = 20;
2
float salary = 25000.50;
Show more lines

Here:

age and salary are variables.
Their values can be changed later.
C
1
age = 25;
Show more lines
Rules for Variable Names
Must start with a letter or underscore (_).
Cannot start with a digit.
Cannot be a keyword.
May contain letters, digits, and underscores.

Valid:

C
1
total
2
_marks
3
count1
Show more lines

Invalid:

C
1
1count
2
float
3
student-name
Show more lines
Types of Variables
Integer Variable
C
1
int num = 10;
Show more lines
Float Variable
C
1
float price = 99.5;
Show more lines
Character Variable
C
1
char grade = 'A';
Show more lines
Constants
Definition

A Constant is a fixed value that cannot be changed during program execution.

Examples
C
1
10
2
3.14
3
'A'
4
"Hello"
Show more lines
Types of Constants
Integer Constants
C
1
100
2
-25
3
0
Show more lines
Floating Point Constants
C
1
3.14
2
25.5
3
0.75
Show more lines
Character Constants
C
1
'A'
2
'B'
3
'Z'
Show more lines
String Constants
C
1
"Hello"
2
"Programming"
Show more lines
Symbolic Constants

Defined using #define.

C
1
#define PI 3.14159
Show more lines

Example:

C
1
float area = PI * r * r;
Show more lines
Constant Variables

Defined using the const keyword.

C
1
const int MAX = 100;
Show more lines

Attempting to change it will cause an error:

C
1
MAX = 200; // Error
Show more lines
Difference Between Variables and Constants
Variable	ConstantValue can change	Value cannot change
Memory contents may be modified	Fixed throughout execution
Example: int age = 20;	Example: const int MAX = 100;
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
const int MAX = 100;
7
 
8
age = 25;
9
 
10
printf("%d\n", age);
11
printf("%d", MAX);
12
 
13
return 0;
14
}
Show more lines
Output
Plain Text
1
25
2
100
Show more lines
Exam Point

A Variable is a named memory location whose value can change during program execution, whereas a Constant is a fixed value that remains unchanged throughout the execution of the program.

## Data types
A Data Type specifies the type of data that a variable can store. It determines:

Type of values stored
Memory required
Range of values
Operations that can be performed
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
int

Stores whole numbers.

C
1
int num = 100;
Show more lines

Example values:

Plain Text
1
10, -5, 250
Show more lines
char

Stores a single character.

C
1
char grade = 'A';
Show more lines

Example values:

Plain Text
1
'A', 'B', 'Z'
Show more lines
float

Stores decimal numbers.

C
1
float pi = 3.14;
Show more lines

Example values:

Plain Text
1
3.14, 25.5, 0.75
Show more lines
double

Stores decimal numbers with higher precision.

C
1
double amount = 12345.6789;
Show more lines
void

Represents no value.

C
1
void display()
2
{
3
}
Show more lines
2. Derived Data Types

Created from basic data types.

Array
C
1
int marks[5];
Show more lines
Pointer
C
1
int *p;
Show more lines
Function
C
1
int add(int a, int b);
Show more lines
3. User-Defined Data Types
Structure
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
};
Show more lines
Union
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
};
6
 
Show more lines
Enumeration
C
1
enum Day
2
{
3
MON,
4
TUE,
5
WED
6
};
Show more lines
typedef
C
1
typedef int Integer;
Show more lines
Size of Common Data Types
Data Type	Sizechar	1 byte
int	4 bytes
float	4 bytes
double	8 bytes
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
float marks = 85.5;
7
char grade = 'A';
8
 
9
printf("%d\n", age);
10
printf("%f\n", marks);
11
printf("%c\n", grade);
12
 
13
return 0;
14
}
Show more lines
Advantages of Data Types
Efficient memory usage
Type safety
Error detection
Better readability
Improved program performance
Exam Point

Data Types specify the kind of data a variable can store. In C, data types are classified into Basic Data Types (int, char, float, double, void), Derived Data Types (arrays, pointers, functions), and User-Defined Data Types (structure, union, enum, typedef).

## Operators
Operators are special symbols used to perform operations on variables, constants, and expressions.

Example
C
1
int a = 10, b = 5;
2
 
3
int sum = a + b;
Show more lines

Here, + is an operator used for addition.

Types of Operators in C
1. Arithmetic Operators

Used to perform mathematical calculations.

Operator	Operation+	Addition
-	Subtraction
*	Multiplication
/	Division
%	Modulus (Remainder)
Example
C
1
int a = 10, b = 3;
2
 
3
printf("%d", a + b);
4
printf("%d", a % b);
Show more lines
2. Relational Operators

Used to compare two values.

Operator	Meaning==	Equal to
!=	Not equal to
>	Greater than
	Less than
>=	Greater than or equal to
<=	Less than or equal to
Example
C
1
if(a > b)
2
{
3
printf("A is greater");
4
}
Show more lines
3. Logical Operators

Used to combine conditions.

Operator	Meaning&&	Logical AND
`	
!	Logical NOT
Example
C
1
if(a > 0 && b > 0)
2
{
3
printf("Both positive");
4
}
Show more lines
4. Assignment Operators

Used to assign values to variables.

Operator	Example=	a = 10
+=	a += 5
-=	a -= 5
*=	a *= 5
/=	a /= 5
%=	a %= 5
Example
C
1
int a = 10;
2
 
3
a += 5;
Show more lines

Result:

Plain Text
1
a = 15
Show more lines
5. Increment and Decrement Operators
Increment (++)
C
1
a++;
Show more lines

Increases value by 1.

Decrement (--)
C
1
a--;
Show more lines

Decreases value by 1.

6. Bitwise Operators

Operate on binary bits.

Operator	Meaning&	Bitwise AND
`	`
^	Bitwise XOR
~	Bitwise NOT
<	Left Shift
>>	Right Shift
Example
C
1
int a = 5;
2
int b = 3;
3
 
4
printf("%d", a & b);
Show more lines
7. Conditional (Ternary) Operator

Syntax:

C
1
condition ? expression1 : expression2;
Show more lines
Example
C
1
int max = (a > b) ? a : b;
Show more lines

Returns the larger value.

8. Special Operators
sizeof

Returns the size of a data type or variable.

C
1
printf("%d", sizeof(int));
Show more lines
Address Operator (&)

Returns the address of a variable.

C
1
int x = 10;
2
 
3
printf("%p", &x);
Show more lines
Pointer Operator (*)

Used with pointers.

C
1
int *p;
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
int a = 10, b = 5;
6
 
7
printf("Addition = %d\n", a + b);
8
printf("Greater = %d\n", a > b);
9
 
10
return 0;
11
}
Show more lines
Operator Precedence (High to Low)
()
++ , --
* , / , %
+ , -
<, <=, >, >=
==, !=
&&
||
=
Example
C
1
int result = 10 + 5 * 2;
Show more lines

Output:

Plain Text
1
20
Show more lines

because * has higher precedence than +.

Exam Point

Operators are symbols used to perform operations on data. The main types of operators in C are Arithmetic, Relational, Logical, Assignment, Increment/Decrement, Bitwise, Conditional, and Special Operators.

## Control statements
Control Statements are statements that control the flow of execution of a program. They determine which statements are executed, how many times they are executed, and under what conditions.

Types of Control Statements
1. Decision Making Statements

Used to make decisions based on conditions.

if Statement

Syntax:

C
1
if(condition)
2
{
3
statements;
4
}
Show more lines

Example:

C
1
if(age >= 18)
2
{
3
printf("Eligible");
4
}
Show more lines
if-else Statement

Syntax:

C
1
if(condition)
2
{
3
statements;
4
}
5
else
6
{
7
statements;
8
}
Show more lines

Example:

C
1
if(marks >= 40)
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
Nested if

An if statement inside another if.

C
1
if(a > 0)
2
{
3
if(a % 2 == 0)
4
{
5
printf("Even Positive Number");
6
}
7
}
Show more lines
else-if Ladder

Used for multiple conditions.

C
1
if(marks >= 80)
2
{
3
printf("Distinction");
4
}
5
else if(marks >= 60)
6
{
7
printf("First Class");
8
}
9
else
10
{
11
printf("Pass");
12
}
Show more lines
switch Statement

Used for multiple choices.

Syntax:

C
1
switch(expression)
2
{
3
case value1:
4
statements;
5
break;
6
 
7
case value2:
8
statements;
9
break;
10
 
11
default:
12
statements;
13
}
Show more lines

Example:

C
1
switch(day)
2
{
3
case 1:
4
printf("Monday");
5
break;
6
 
7
case 2:
8
printf("Tuesday");
9
break;
10
 
11
default:
12
printf("Invalid Day");
13
}
Show more lines
2. Looping Statements

Used to execute a block of code repeatedly.

for Loop

Syntax:

C
1
for(initialization; condition; increment)
2
{
3
statements;
4
}
Show more lines

Example:

C
1
for(int i = 1; i <= 5; i++)
2
{
3
printf("%d ", i);
4
}
Show more lines

Output:

Plain Text
1
1 2 3 4 5
Show more lines
while Loop

Syntax:

C
1
while(condition)
2
{
3
statements;
4
}
Show more lines

Example:

C
1
int i = 1;
2
 
3
while(i <= 5)
4
{
5
printf("%d ", i);
6
i++;
7
}
Show more lines
do-while Loop

Syntax:

C
1
do
2
{
3
statements;
4
}
5
while(condition);
Show more lines

Example:

C
1
int i = 1;
2
 
3
do
4
{
5
printf("%d ", i);
6
i++;
7
}
8
while(i <= 5);
Show more lines

Note: Executes at least once.

3. Jump Statements

Used to transfer program control from one location to another.

break

Terminates a loop or switch statement.

C
1
for(int i = 1; i <= 10; i++)
2
{
3
if(i == 5)
4
Show more lines

Output:

Plain Text
1
1 2 3 4
Show more lines
continue

Skips the current iteration and moves to the next iteration.

C
1
for(int i = 1; i <= 5; i++)
2
{
3
if(i == 3)
4
continue;
5
 
6
printf("%d ", i);
7
}
8
 
Show more lines

Output:

Plain Text
1
1 2 4 5
Show more lines
goto

Transfers control to a labeled statement.

C
1
goto end;
2
 
3
printf("Hello");
4
 
5
end:
6
printf("Finished");
Show more lines
return

Terminates a function and optionally returns a value.

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
Classification Summary
Selection Control
if
if-else
else-if
switch
Iteration Control
for
while
do-while
Jump Control
break
continue
goto
return
Exam Point

Control Statements are used to control the flow of execution in a C program. They are classified into Decision Making Statements (if, if-else, switch), Looping Statements (for, while, do-while), and Jump Statements (break, continue, goto, return).

## Functions Parameter Passing
Parameter Passing is the process of transferring data from a calling function to a called function through parameters.

Parameters allow functions to receive input values and perform operations on them.

Types of Parameters
Actual Parameters (Arguments)

The values supplied during the function call.

C
1
add(10, 20);
Show more lines

Here:

Plain Text
1
10 and 20
Show more lines

are actual parameters.

Formal Parameters

The variables declared in the function definition.

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

Here:

Plain Text
1
a and b
Show more lines

are formal parameters.

Methods of Parameter Passing
1. Call by Value

A copy of the actual argument is passed to the function.

Changes inside the function do not affect the original variable.
Default method in C.
Example
C
1
#include <stdio.h>
2
 
3
void change(int x)
4
{
5
x = 100;
6
}
7
 
8
int main()
9
{
10
int a = 10;
11
 
12
change(a);
13
 
14
printf("%d", a);
15
 
16
return 0;
17
}
Show more lines
Output
Plain Text
1
10
Show more lines

The original value remains unchanged.

2. Call by Reference

The address of the variable is passed using pointers.

Changes inside the function affect the original variable.
Used when the function needs to modify the caller's data.
Example
C
1
#include <stdio.h>
2
 
3
void change(int *x)
4
{
5
*x = 100;
6
}
7
 
8
int main()
9
{
10
int a = 10;
11
 
12
change(&a);
13
 
14
printf("%d", a);
15
 
16
return 0;
17
}
Show more lines
Output
Plain Text
1
100
Show more lines

The original variable is modified.

Call by Value vs Call by Reference
Feature	Call by Value	Call by ReferenceData Passed	Copy of value	Address of variable
Original Variable	Not modified	Modified
Memory Usage	More	Less for large data
Safety	Safer	Requires pointers
Advantages of Parameter Passing
Promotes code reusability.
Allows data sharing between functions.
Makes programs modular.
Reduces code duplication.
Exam Point

Parameter Passing is the mechanism of passing data to functions. In C, data can be passed using Call by Value (copy of data is passed) and Call by Reference (address of data is passed using pointers).

## Virtual Functions
A Virtual Function is a member function in a base class that is declared using the virtual keyword and can be overridden in a derived class.

It is used to achieve Run-Time Polymorphism (Dynamic Binding) in C++.

Syntax
C++
1
class Base
2
{
3
public:
4
virtual void display()
5
{
6
cout << "Base Class";
7
}
8
};
Show more lines
Example Program
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Base
5
{
6
public:
7
virtual void display()
8
{
9
cout << "Base Class";
10
}
11
};
12
 
13
class Derived : public Base
14
{
15
public:
16
void display()
17
{
18
cout << "Derived Class";
19
}
20
};
21
 
22
int main()
23
{
24
Base *ptr;
25
Derived d;
26
 
27
ptr = &d;
28
 
29
ptr->display();
30
 
31
return 0;
32
}
Show less
Output
Plain Text
1
Derived Class
Show more lines
Working
C++
1
Base *ptr;
2
Derived d;
3
 
4
ptr = &d;
5
 
Show more lines

When:

C++
1
ptr->display();
2
 
Show more lines

is executed,

Without virtual → Base::display() is called.
With virtual → Derived::display() is called.

Thus, the function call is decided at run time.

Advantages
Supports run-time polymorphism.
Increases flexibility.
Promotes code reusability.
Enables dynamic method binding.
Useful in inheritance hierarchies.
Pure Virtual Function

A virtual function can be made pure virtual by assigning 0.

C++
1
virtual void display() = 0;
Show more lines

A class containing a pure virtual function becomes an Abstract Class.

Example:


class Shape
2
{


public:
virtual void draw() = 0;
};












Both implement:

C++
1
sound()
Show more lines

Calling:

C++
1
animal->sound();
Show more lines

produces different outputs depending on whether the object is a Dog or Cat.

Exam Point

A Virtual Function is a function declared with the virtual keyword in a base class. It allows a derived class function to be called through a base-class pointer or reference, enabling run-time polymorphism (dynamic binding).

## Class and Objects
A Class is a user-defined data type that combines data members (variables) and member functions (methods) into a single unit.

A class acts as a blueprint for creating objects.

Syntax
C++
1
class Student
2
{
3
public:
4
int id;
5
 
6
void display()
7
{
8
cout << id;
9
}
10
};
Show more lines

In the above example:

Student → Class
id → Data member
display() → Member function
Object
Definition

An Object is an instance of a class.

When an object is created, memory is allocated for the data members of the class.

Syntax
C++
1
Student s1;
Show more lines

Here:

Student → Class
s1 → Object
Example Program
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Student
5
{
6
public:
7
int id;
8
 
9
void display()
10
{
11
cout << "ID = " << id;
12
}
13
};
14
 
15
int main()
16
{
17
Student s1;
18
 
19
s1.id = 101;
20
 
21
s1.display();
22
 
23
return 0;
24
}
Show less
Output
Plain Text
1
ID = 101
Show more lines
Accessing Members of an Object

The dot (.) operator is used.

C++
1
s1.id = 101;
2
s1.display();
3
 
Show more lines
Characteristics of a Class
Logical entity.
Acts as a blueprint.
Defines data and functions.
Does not occupy memory until objects are created.
Characteristics of an Object
Physical entity.
Occupies memory.
Has state (data) and behavior (functions).
Created from a class.
Class vs Object
Class	ObjectBlueprint or template	Instance of a class
Logical entity	Physical entity
No memory allocated for data members	Memory allocated
Defines properties and behavior	Uses properties and behavior
Example
C++
1
class Student
2
{
3
};
Show more lines

Class = Student

C++
1
Student s1;
Show more lines

Object = s1

Advantages
Supports Object-Oriented Programming.
Improves code reusability.
Provides data security through encapsulation.
Makes programs modular and maintainable.
Applications
Banking systems
Student management systems
Library management systems
Inventory systems
Hospital management systems
Exam Point

A Class is a user-defined data type that acts as a blueprint for objects. An Object is an instance of a class that occupies memory and is used to access the data members and member functions of the class.

## Constructors and Destructors
A Constructor is a special member function of a class that is automatically called when an object is created.

Its main purpose is to initialize the object's data members.

Characteristics
Name is the same as the class name.
Has no return type.
Called automatically when an object is created.
Can be overloaded.
Syntax
C++
1
class Student
2
{
3
public:
4
Student()
5
{
6
cout << "Constructor Called";
7
}
8
};
9
 
Show more lines
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Student
5
{
6
public:
7
Student()
8
{
9
cout << "Object Created";
10
}
11
};
12
 
13
int main()
14
{
15
Student s1;
16
 
17
return 0;
18
}
Show more lines
Output
Plain Text
1
Object Created
Show more lines
Types of Constructors
Default Constructor

Constructor without parameters.

C++
1
class Demo
2
{
3
public:
4
Demo()
5
{
6
cout << "Default Constructor";
7
}
8
};
Show more lines
Parameterized Constructor

Constructor with parameters.

C++
1
class Student
2
{
3
public:
4
int id;
5
 
6
Student(int x)
7
{
8
id = x;
9
}
10
};
Show more lines

Example:

C++
1
Student s1(101);
Show more lines
Copy Constructor

Used to initialize one object using another object.

C++
1
class Test
2
{
3
public:
4
int x;
5
 
6
Test(int a)
7
{
8
x = a;
9
}
10
 
11
Test(const Test &t)
12
{
13
x = t.x;
14
}
15
};
16
 
Show less
Destructor
Definition

A Destructor is a special member function that is automatically called when an object is destroyed.

Its main purpose is to release resources and perform cleanup operations.

Characteristics
Name is the same as the class name.
Preceded by ~ (tilde).
Has no return type.
Takes no arguments.
Cannot be overloaded.
Syntax
C++
1
class Student
2
{
3
public:
4
~Student()
5
{
6
cout << "Destructor Called";
7
}
8
};
Show more lines
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Student
5
{
6
public:
7
Student()
8
{
9
cout << "Constructor Called\n";
10
}
11
 
12
~Student()
13
{
14
cout << "Destructor Called";
15
}
16
};
17
 
18
int main()
19
{
20
Student s1;
21
 
22
return 0;
23
}
Show more lines
Output
Plain Text
1
Constructor Called
2
Destructor Called
Show more lines
Constructor vs Destructor
Feature	Constructor	DestructorPurpose	Initializes object	Destroys object
Name	Same as class name	Same as class name with ~
Arguments	Can have arguments	No arguments
Overloading	Possible	Not possible
Invocation	Object creation	Object destruction
Advantages
Constructors
Automatic initialization of objects.
Reduces coding effort.
Improves reliability.
Destructors
Frees allocated memory.
Closes files and releases resources.
Prevents memory leaks.
Exam Point

A Constructor is a special member function automatically invoked when an object is created and is used to initialize object data. A Destructor is a special member function automatically invoked when an object is destroyed and is used to release resources and perform cleanup operations.
## Overloading
Overloading is a feature of C++ that allows multiple functions or operators to have the same name but different parameters or behavior.

It is an example of Compile-Time Polymorphism (Static Polymorphism).

Types of Overloading
1. Function Overloading

Function overloading means defining multiple functions with the same name but different:

Number of parameters
Type of parameters
Order of parameters
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Demo
5
{
6
public:
7
void add(int a, int b)
8
{
9
cout << a + b << endl;
10
}
11
 
12
void add(int a, int b, int c)
13
{
14
cout << a + b + c << endl;
15
}
16
};
17
 
18
int main()
19
{
20
Demo d;
21
 
22
d.add(10, 20);
23
d.add(10, 20, 30);
24
 
25
return 0;
26
}
Show less
Output
Plain Text
1
30
2
60
Show more lines
2. Operator Overloading

Operator overloading allows existing operators to work with user-defined objects.

Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Test
5
{
6
public:
7
int x;
8
 
9
Test(int a)
10
{
11
x = a;
12
}
13
 
14
Test operator +(Test t)
15
{
16
return Test(x + t.x);
17
}
18
};
19
 
20
int main()
21
{
22
Test t1(10), t2(20);
23
 
24
Test t3 = t1 + t2;
25
 
26
cout << t3.x;
27
 
28
return 0;
29
}
Show less
Output
Plain Text
1
30
Show more lines
Rules of Function Overloading

Valid:

C++
1
void display(int);
2
void display(float);
3
void display(int, int);
Show more lines

Invalid:

C++
1
int add(int, int);
2
float add(int, int);
Show more lines

Only changing the return type is not sufficient for overloading.

Advantages of Overloading
Improves readability.
Reduces the number of function names.
Increases code reusability.
Supports compile-time polymorphism.
Function Overloading vs Operator Overloading
Function Overloading
Same function name.
Different parameter lists.

Example:

C++
1
add(10, 20);
2
add(10, 20, 30);
Show more lines
Operator Overloading
Same operator.
Different behavior for user-defined objects.

Example:

C++
1
obj1 + obj2;
Show more lines
Exam Point

Overloading is a compile-time polymorphism feature in C++ that allows multiple functions or operators to have the same name but different parameter lists or behaviors. The two main types are Function Overloading and Operator Overloading.

## Inheritance
Inheritance is an Object-Oriented Programming (OOP) mechanism in which a new class acquires the properties and behaviors of an existing class.

Base Class (Parent Class): Class whose properties are inherited.
Derived Class (Child Class): Class that inherits properties from the base class.

Inheritance promotes code reusability and reduces duplication.

Syntax
C++
1
class Base
2
{
3
public:
4
void display()
5
{
6
cout << "Base Class";
7
}
8
};
9
 
10
class Derived : public Base
11
{
12
};
Show more lines
Example Program
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Person
5
{
6
public:
7
void show()
8
{
9
cout << "Person Details";
10
}
11
};
12
 
13
class Student : public Person
14
{
15
};
16
 
17
int main()
18
{
19
Student s;
20
s.show();
21
 
22
return 0;
23
}
Show less
Output
Plain Text
1
Person Details
Show more lines

The Student class inherits the show() method from the Person class.

Types of Inheritance
1. Single Inheritance

One derived class inherits from one base class.

C++
1
class A
2
{
3
};
4
 
5
class B : public A
6
{
7
};
Show more lines
2. Multilevel Inheritance

A derived class becomes the base class for another class.

C++
1
class A
2
{
3
};
4
 
5
class B : public A
6
{
7
};
8
 
9
class C : public B
10
{
11
};
Show more lines
3. Multiple Inheritance

A class inherits from more than one base class.

C++
1
class A
2
{
3
};
4
 
5
class B
6
{
7
};
8
 
9
class C : public A, public B
10
{
11
};
Show more lines
4. Hierarchical Inheritance

Multiple derived classes inherit from the same base class.


class A

{

};


class B : public A

{

};

 

class C : public A

{

};

5. Hybrid Inheritance

Combination of two or more inheritance types.
Public members remain public.
Protected members remain protected.
Protected Inheritance
class B : protected A

{

};

Public and protected members become private.
Advantages of Inheritance
Code reusability.
Reduced code duplication.
Easier maintenance.
Extensibility of programs.
Supports hierarchical classification.
Real-Life Example
Plain Text
1
Vehicle
2
|
3

4
| |
5
Car Bike
Show more lines
Car is a Vehicle.
Bike is a Vehicle.

Common properties such as:

Plain Text
1
start()
2
stop()
3
speed


can be inherited from the Vehicle class.

Exam Point

Inheritance is an OOP feature through which a derived class acquires the data members and member functions of a base class. It promotes code reusability and is classified into Single, Multiple, Multilevel, Hierarchical, and Hybrid Inheritance.

## Templates
A Template is a C++ feature that allows writing generic programs and functions. A template enables the same code to work with different data types without rewriting it.

Templates support code reusability and generic programming.

Types of Templates
Function Template
Class Template
1. Function Template

A function template allows a single function to operate on different data types.

Syntax
C++
1
template <class T>
2
 
3
T add(T a, T b)
4
{
5
return a + b;
6
}
Show more lines
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
template <class T>
5
T add(T a, T b)
6
{
7
return a + b;
8
}
9
 
10
int main()
11
{
12
cout << add(10, 20) << endl;
13
cout << add(5.5, 2.5);
14
 
15
return 0;
16
}
Show less
Output
Plain Text
1
30
2
8
Show more lines
2. Class Template

A class template allows creating classes that work with different data types.

Syntax
C++
1
template <class T>
2
 
3
class Test
4
{
5
T data;
6
};
Show more lines
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
template <class T>
5
class Test
6
{
7
public:
8
T data;
9
 
10
Test(T x)
11
{
12
data = x;
13
}
14
 
15
void display()
16
{
17
cout << data;
18
}
19
};
20
 
21
int main()
22
{
23
Test<int> t1(100);
24
Test<float> t2(10.5);
25
 
26
t1.display();
27
cout << endl;
28
t2.display();
29
 
30
return 0;
31
}
Show more lines
Output
Plain Text
1
100
2
10.5
Show more lines
Template Syntax Keywords
Using class
C++
1
template <class T>
Show more lines
Using typename
C++
1
template <typename T>
Show more lines

Both are equivalent.

Advantages of Templates
Code reusability.
Generic programming.
Reduces code duplication.
Improves program flexibility.
Type safety at compile time.
Function Overloading vs Templates
Function Overloading
C++
1
int add(int a, int b);
2
float add(float a, float b);
Show more lines

Separate functions are required.

Template
C++
1
template <class T>
2
T add(T a, T b);
Show more lines

One function works for multiple data types.

Applications
Standard Template Library (STL)
Generic algorithms
Data structures
Containers such as Vector, List, Stack, Queue
Software libraries
Exam Point

A Template is a C++ feature used for generic programming. It allows functions and classes to operate with different data types using a single definition. The two types of templates are Function Templates and Class Templates.

## Exception and Event Handling
Exception Handling is a mechanism used to detect and handle runtime errors (exceptions) so that the normal flow of a program is not interrupted.

Examples of exceptions:

Division by zero
File not found
Invalid input
Memory allocation failure
Need for Exception Handling
Prevents program crashes.
Separates error-handling code from normal code.
Improves program reliability.
Makes debugging easier.
C++ Exception Handling Keywords
try

Contains code that may generate an exception.

C++
1
try
2
{
3
// risky code
4
}
Show more lines
throw

Used to generate an exception.

C++
1
throw value;
Show more lines
catch

Handles the exception.

C++
1
catch(type variable)
2
{
3
// handling code
4
}
Show more lines
Example Program
C++
1
#include <iostream>
2
using namespace std;
3
 
4
int main()
5
{
6
int a = 10, b = 0;
7
 
8
try
9
{
10
if(b == 0)
11
throw b;
12
 
13
cout << a / b;
14
}
15
 
16
catch(int x)
17
{
18
cout << "Division by Zero Exception";
19
}
20
 
21
return 0;
22
}
Show less
Output
Plain Text
1
Division by Zero Exception
Show more lines
Working
Code in try block executes.
Exception occurs.
throw generates the exception.
Control transfers to the matching catch block.
Exception is handled.
Advantages
Prevents abnormal termination.
Improves program robustness.
Simplifies error management.
Event Handling
Definition

Event Handling is the process of responding to events generated by the user or system.

An event is an action or occurrence such as:

Mouse click
Keyboard press
Button click
Window closing
Timer expiration
Components of Event Handling
Event

An action that occurs.

Examples:

Plain Text
1
Mouse Click
2
Key Press
3
Button Click
Show more lines
Event Source

Object that generates the event.

Examples:

Plain Text
1
Button
2
Text Box
3
Menu
Show more lines
Event Handler

Function or method that responds to the event.

Event Handling Process
User performs an action.
Event is generated.
Event handler receives the event.
Appropriate action is executed.
Example
Plain Text
1
Button Click
2
↓
3
Event Generated
4
↓
5
Event Handler Executes
6
↓
7
Message Displayed
Show more lines
Example (GUI Concept)
C++
1
button.click()
2
{
3
cout << "Button Pressed";
4
}
Show more lines

When the button is clicked, the event handler executes.

Advantages of Event Handling
Supports interactive applications.
Improves user experience.
Simplifies GUI programming.
Enables event-driven programming.
Exception Handling vs Event Handling
Exception Handling	Event HandlingHandles runtime errors	Handles user/system events
Uses try, throw, catch	Uses event handlers
Improves reliability	Improves interactivity
Example: Divide by zero	Example: Button click
Applications
Exception Handling
Banking software
Database systems
File processing
Operating systems
Event Handling
GUI applications
Web applications
Mobile apps
Games
Exam Point

Exception Handling is the mechanism of detecting and handling runtime errors using try, throw, and catch blocks. Event Handling is the mechanism of responding to user or system-generated events such as mouse clicks, key presses, and button selections through event handlers.

## Streams and Files
A Stream is a flow of data between a program and an input/output device.

In C++, streams are used to perform input and output operations.

Types of Streams
Input Stream

Transfers data from input device to program.

Example:

C++
1
cin >> x;
Show more lines
Output Stream

Transfers data from program to output device.

Example:

C++
1
cout << x;
Show more lines
Common Stream Classes
cin

Used for input.

C++
1
int age;
2
cin >> age;
Show more lines
cout

Used for output.

C++
1
cout << "Hello";
Show more lines
cerr

Used to display error messages.

C++
1
cerr << "Error Occurred";
Show more lines
clog

Used for logging messages.

C++
1
clog << "Log Message";
Show more lines
File Handling
Definition

A File is a collection of data stored permanently on a storage device.

File handling allows programs to:

Create files
Read data
Write data
Append data
File Stream Classes

The header file used is:

C++
1
#include <fstream>
Show more lines
ifstream

Used for reading from a file.

C++
1
ifstream fin;
Show more lines
ofstream

Used for writing to a file.

C++
1
ofstream fout;
Show more lines
fstream

Used for both reading and writing.

C++
1
fstream file;
Show more lines
Opening a File
Writing to a File
C++
1
ofstream fout;
2
 
3
fout.open("data.txt");
Show more lines
Reading from a File
C++
1
ifstream fin;
2
 
3
fin.open("data.txt");
Show more lines
Writing to a File
Example
C++
1
#include <iostream>
2
#include <fstream>
3
using namespace std;
4
 
5
int main()
6
{
7
ofstream fout;
8
 
9
fout.open("data.txt");
10
 
11
fout << "Hello World";
12
 
13
fout.close();
14
 
15
return 0;
16
}
Show less
Reading from a File
Example
C++
1
#include <iostream>
2
#include <fstream>
3
using namespace std;
4
 
5
int main()
6
{
7
ifstream fin;
8
string str;
9
 
10
fin.open("data.txt");
11
 
12
fin >> str;
13
 
14
cout << str;
15
 
16
fin.close();
17
 
18
return 0;
19
}
Show less
Output
Plain Text
1
Hello
Show more lines
File Opening Modes
Input Mode
C++
1
ios::in
Show more lines

Used for reading.

Output Mode
C++
1
ios::out
Show more lines

Used for writing.

Append Mode
C++
1
ios::app
Show more lines

Adds data at the end of the file.

Binary Mode
C++
1
ios::binary
Show more lines

Used for binary files.

Example
C++
1
ofstream fout("data.txt", ios::app);
Show more lines
Closing a File
C++
1
file.close();
Show more lines

Always close files after use to release resources.

Stream Hierarchy
Plain Text
1
ios
2
├── istream
3
│ └── ifstream
4
├── ostream
5
│ └── ofstream
6
└── iostream
7
└── fstream
Show more lines
Advantages of File Handling
Permanent data storage.
Easy retrieval of data.
Supports large amounts of information.
Useful for databases and record management.
Applications
Student Management Systems
Banking Applications
Inventory Systems
Library Management Systems
Database Applications
Exam Point

A Stream is a flow of data between a program and an I/O device. C++ uses cin, cout, cerr, and clog for stream operations. File handling is performed using ifstream, ofstream, and fstream classes available in the <fstream> header file.