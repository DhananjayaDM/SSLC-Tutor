# Object Oriented Programming
## Class
A Class is a user-defined data type that groups data members (variables) and member functions (methods) into a single unit. It serves as a blueprint for creating objects.

Class is one of the fundamental concepts of Object-Oriented Programming (OOP).

Syntax
C++
1
class ClassName
2
{
3
access_specifier:
4
 
5
data_members;
6
 
7
member_functions();
8
};
Show more lines
Example
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
char grade;
6
 
7
void display()
8
{
9
cout << id;
10
}
11
};
Show more lines
Object

An Object is an instance of a class.

Example
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
Components of a Class
Data Members

Variables declared inside a class.

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
float marks;
6
};
Show more lines
Member Functions

Functions declared inside a class.

C++
1
void display()
2
{
3
cout << id;
4
}
Show more lines
Access Specifiers
Public

Members can be accessed from anywhere.

C++
1
public:
2
int id;
Show more lines
Private

Members can be accessed only within the class.

C++
1
private:
2
int marks;
Show more lines
Protected

Members can be accessed within the class and derived classes.

C++
1
protected:
2
int age;
3
 
Show more lines
Creating Multiple Objects
C++
1
Student s1, s2, s3;
Show more lines

Each object has its own copy of data members.

Class vs Object
Class	ObjectBlueprint	Instance of a class
Logical entity	Physical entity
No memory allocated for data members until objects are created	Memory is allocated
Example: Student	Example: s1
Advantages of Classes
Encapsulation of data and functions.
Code reusability.
Improved security through data hiding.
Better program organization.
Supports Object-Oriented Programming.
Applications
Student Management Systems
Banking Applications
Inventory Systems
Healthcare Systems
Software Development
Exam Point

A Class is a user-defined data type that combines data members and member functions into a single unit. It acts as a blueprint for creating objects and supports the principles of Object-Oriented Programming.

## Object
An Object is an instance of a class. It is a real entity that occupies memory and is used to access the data members and member functions of a class.

A class is a blueprint, while an object is the actual implementation of that blueprint.

Syntax
C++
1
ClassName objectName;
Show more lines
Example
C++
1
Student s1;
Show more lines
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
Accessing Object Members

The dot (.) operator is used to access data members and member functions.

Example
C++
1
s1.id = 101;
2
s1.display();
Show more lines
Creating Multiple Objects
C++
1
Student s1, s2, s3;
Show more lines

Each object has its own separate copy of data members.

Example
C++
1
s1.id = 101;
2
s2.id = 102;
Show more lines
Characteristics of Objects
Occupy memory.
Have state (data members).
Have behavior (member functions).
Are created from classes.
Can interact with other objects.
Class and Object
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
};
Show more lines

Creating object:

C++
1
Student s1;
Show more lines

Here:

Student is the class.
s1 is the object.
Advantages of Objects
Represent real-world entities.
Support data encapsulation.
Improve code reusability.
Simplify program design.
Enable object-oriented programming.
Applications
Student Management Systems
Banking Systems
Library Management Systems
Inventory Systems
Hospital Management Systems
Exam Point

An Object is an instance of a class that occupies memory and is used to access the data members and member functions of the class. Objects are the fundamental runtime entities in Object-Oriented Programming.

## Instantiation
Instantiation is the process of creating an object from a class. When an object is created, memory is allocated for the data members of the class.

A class is only a blueprint. Instantiation creates the actual object that can be used in a program.

Syntax
C++
1
ClassName objectName;
Show more lines
Example
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
};
6
 
7
Student s1;
Show more lines

Here:

Student → Class
s1 → Object
Creating s1 is called Instantiation.
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
};
9
 
10
int main()
11
{
12
Student s1; // Instantiation
13
 
14
s1.id = 101;
15
 
16
cout << s1.id;
17
 
18
return 0;
19
}
Show less
Output
Plain Text
1
101
2
 
Show more lines
Why Instantiation is Needed
A class itself does not occupy memory for its data members.
Memory is allocated only when objects are created.
Objects allow access to data members and member functions.

Example:

C++
1
Student s1;
2
Student s2;
Show more lines

Two separate objects are created.

Multiple Instantiations
C++
1
Student s1;
2
Student s2;
3
Student s3;
Show more lines

Each object has its own copy of data members.

C++
1
s1.id = 100;
2
s2.id = 200;
3
s3.id = 300;
Show more lines
Class vs Instantiation
Class	InstantiationBlueprint	Creation of object
No memory for object data	Memory allocated
Defines properties and behavior	Creates actual usable entity
Advantages
Creates usable objects from classes.
Allocates memory for data members.
Supports object-oriented programming.
Allows multiple objects from the same class.
Exam Point

Instantiation is the process of creating an object from a class. When an object is instantiated, memory is allocated and the object can access the data members and member functions defined in the class.

## Inheritance
Inheritance is an Object-Oriented Programming (OOP) feature that allows a new class to acquire the properties and behaviors of an existing class.

The existing class is called the Base Class (Parent Class).
The new class is called the Derived Class (Child Class).

Inheritance promotes code reusability and reduces redundancy.

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
cout << "Person Class";
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
Person Class
Show more lines

The Student class inherits the show() function from the Person class.

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

A class inherits from another derived class.

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
class C : public A
10
{
11
};
Show more lines
5. Hybrid Inheritance

Combination of two or more inheritance types.

Access Modes in Inheritance
Public Inheritance
C++
1
class B : public A
2
{
3
};
Show more lines
Public members remain public.
Protected members remain protected.
Protected Inheritance
C++
1
class B : protected A
2
{
3
};
Show more lines
Private Inheritance
C++
1
class B : private A
2
{
3
};
Show more lines
Advantages
Code reusability.
Reduces code duplication.
Easier maintenance.
Supports extensibility.
Represents real-world relationships.
Example
C++
1
class Vehicle
2
{
3
public:
4
void start()
5
{
6
cout << "Vehicle Started";
7
}
8
};
9
 
10
class Car : public Vehicle
11
{
12
};
Show more lines
C++
1
Car c;
2
c.start();
Show more lines

Car can use the start() function without redefining it.

Inheritance vs Composition
Inheritance	Composition"is-a" relationship	"has-a" relationship
Child acquires parent properties	Class contains another class
Example: Car is a Vehicle	Car has an Engine
Exam Point

Inheritance is an OOP mechanism in which a derived class acquires the data members and member functions of a base class. It improves code reusability and supports hierarchical classification.

## Encapsulation
Encapsulation is the process of combining data (variables) and methods (functions) into a single unit called a class, while restricting direct access to the data.

It is one of the fundamental principles of Object-Oriented Programming (OOP) and is also known as data hiding.

Purpose of Encapsulation
Protect data from unauthorized access.
Improve security.
Increase maintainability.
Control how data is accessed and modified.
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
private:
7
int marks;
8
 
9
public:
10
void setMarks(int m)
11
{
12
marks = m;
13
}
14
 
15
int getMarks()
16
{
17
return marks;
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
Student s;
24
 
25
s.setMarks(90);
26
 
27
cout << s.getMarks();
28
 
29
return 0;
30
}
Show less
Output
Plain Text
1
90
Show more lines

Here:

marks is hidden using private.
Access is provided through setMarks() and getMarks().
Access Specifiers
Private
C++
1
private:
2
int marks;
Show more lines
Accessible only within the class.
Public
C++
1
public:
2
void setMarks();
Show more lines
Accessible from anywhere.
Protected
C++
1
protected:
2
int age;
Show more lines
Accessible within the class and derived classes.
Advantages
Data security.
Data hiding.
Better control over data.
Improved code maintainability.
Increased modularity.
Real-Life Example
Plain Text
1
Bank Account
Show more lines

A user can:

Deposit money
Withdraw money

A user cannot directly access or modify the account balance.

This is achieved through encapsulation.

Encapsulation vs Abstraction
Encapsulation
Hides data.
Achieved using classes and access specifiers.
Focuses on data security.
Abstraction
Hides implementation details.
Focuses on showing only essential features.
Exam Point

Encapsulation is the OOP concept of binding data members and member functions into a single unit (class) and restricting direct access to data using access specifiers. It is used to achieve data hiding and security.

## Abstract Class
An Abstract Class is a class that cannot be instantiated (cannot create objects directly). It is used as a base class and contains one or more pure virtual functions that must be implemented by derived classes.

Abstract classes provide a common interface for related classes.

Syntax
C++
1
class Shape
2
{
3
public:
4
virtual void draw() = 0;
5
};
Show more lines

Here:

C++
1
virtual void draw() = 0;
Show more lines

is a pure virtual function, making Shape an abstract class.

Example Program
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Shape
5
{
6
public:
7
virtual void draw() = 0;
8
};
9
 
10
class Circle : public Shape
11
{
12
public:
13
void draw()
14
{
15
cout << "Drawing Circle";
16
}
17
};
18
 
19
int main()
20
{
21
Circle c;
22
c.draw();
23
 
24
return 0;
25
}
Show less
Output
Plain Text
1
Drawing Circle
Show more lines
Pure Virtual Function

A function declared with:

C++
1
virtual void functionName() = 0;
Show more lines

Characteristics:

Has no implementation in the abstract class.
Must be overridden by derived classes.
Makes the class abstract.

Example:

C++
1
virtual void display() = 0;
Show more lines
Key Features
Cannot create objects directly.
May contain normal functions.
May contain data members.
Used for achieving abstraction.
Serves as a blueprint for derived classes.
Invalid Example
C++
1
class Shape
2
{
3
public:
4
virtual void draw() = 0;
5
};
6
 
7
int main()
8
{
9
Shape s; // Error
10
}
Show more lines

Reason:

Plain Text
1
Shape is an abstract class.
Show more lines
Advantages
Provides a common interface.
Supports code reusability.
Enforces implementation in derived classes.
Helps achieve abstraction.
Improves program design.
Real-World Example
Plain Text
1
Vehicle
Show more lines

Abstract operations:

start()
stop()

Derived classes:

Car
Bike
Bus

Each vehicle implements these functions differently.

Abstract Class vs Concrete Class
Abstract Class	Concrete ClassCannot create objects	Objects can be created
Contains pure virtual functions	Fully implemented
Used as base class	Used directly
Achieves abstraction	Provides implementation
Applications
Framework design
GUI systems
Game development
Banking systems
Enterprise applications
Exam Point

An Abstract Class is a class that contains at least one pure virtual function and cannot be instantiated. It is used to provide a common interface and achieve abstraction in Object-Oriented Programming.

## Polymorphism
Polymorphism is an Object-Oriented Programming (OOP) concept that allows the same function or operator to behave differently in different situations.

The word Polymorphism means "many forms".

Types of Polymorphism
1. Compile-Time Polymorphism (Static Polymorphism)

Achieved during compilation.

Methods:

Function Overloading
Operator Overloading
Function Overloading

Same function name with different parameters.

C++
1
class Demo
2
{
3
public:
4
void add(int a, int b)
5
{
6
cout << a + b;
7
}
8
 
9
void add(int a, int b, int c)
10
{
11
cout << a + b + c;
12
}
13
};
Show more lines
Operator Overloading

Existing operators are given new meanings.

C++
1
class Complex
2
{
3
public:
4
int real;
5
 
6
Complex operator +(Complex c)
7
{
8
Complex temp;
9
temp.real = real + c.real;
10
return temp;
11
}
12
};
Show more lines
2. Run-Time Polymorphism (Dynamic Polymorphism)

Achieved during program execution using:

Inheritance
Virtual Functions
Example
C++
1
#include <iostream>
2
using namespace std;
3
 
4
class Animal
5
{
6
public:
7
virtual void sound()
8
{
9
cout << "Animal Sound";
10
}
11
};
12
 
13
class Dog : public Animal
14
{
15
public:
16
void sound()
17
{
18
cout << "Bark";
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
Animal *a;
25
Dog d;
26
 
27
a = &d;
28
 
29
a->sound();
30
 
31
return 0;
32
}
Show less
Output
Plain Text
1
Bark
Show more lines
Virtual Function

A virtual function is a function declared using the virtual keyword in the base class.

C++
1
virtual void display();
Show more lines

It allows the correct derived-class function to be called at runtime.

Advantages of Polymorphism
Code reusability.
Flexibility.
Easier maintenance.
Extensibility.
Supports dynamic binding.
Real-Life Example
Plain Text
1
Shape
Show more lines

Method:

Plain Text
1
draw()
Show more lines

Different implementations:

Circle → Draw Circle
Rectangle → Draw Rectangle
Triangle → Draw Triangle

Same function name, different behavior.

Compile-Time vs Run-Time Polymorphism
Compile-Time Polymorphism	Run-Time PolymorphismResolved during compilation	Resolved during execution
Faster	Slightly slower
Function/Operator Overloading	Virtual Functions and Overriding
Static Binding	Dynamic Binding
Exam Point

Polymorphism is the ability of an object or function to take many forms. It is of two types: Compile-Time Polymorphism (Function Overloading, Operator Overloading) and Run-Time Polymorphism (Function Overriding using Virtual Functions).