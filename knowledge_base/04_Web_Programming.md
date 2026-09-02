# Web Programming
## HTML
HTML (HyperText Markup Language) is the standard markup language used to create and structure web pages.

It defines the content and layout of a webpage using tags and elements.

Features of HTML
Easy to learn and use.
Platform independent.
Used to create web pages.
Supports images, links, tables, forms, and multimedia.
Works with CSS and JavaScript.
Basic Structure of an HTML Document
HTML
1
<!DOCTYPE html>
2
<html>
3
<head>
4
<title>My Web Page</title>
5
</head>
6
<body>
7
<h1>Hello World</h1>
8
<p>Welcome to HTML.</p>
9
</body>
10
</html>
Show more lines
HTML Tags

HTML uses tags enclosed within angle brackets < >.

Examples
HTML
1
<h1>Heading</h1>
2
<p>Paragraph</p>
Show more lines
Common HTML Tags
Heading Tags
HTML
1
<h1>Heading 1</h1>
2
<h2>Heading 2</h2>
3
<h3>Heading 3</h3>
Show more lines
Paragraph Tag
HTML
1
<p>This is a paragraph.</p>
Show more lines
Line Break Tag
HTML
1
Line 1<br>
2
Line 2
Show more lines
Horizontal Rule
HTML
1
<hr>
Show more lines
Hyperlinks

Used to link one page to another.

Syntax
HTML
1
https://www.google.com
Show more lines
Images

Used to display images.

Syntax
HTML
1
image.jpg
Show more lines
Lists
Ordered List
HTML
1
<ol>
2
<li>Java</li>
3
<li>Python</li>
4
</ol>
Show more lines

Output:

Java
Python
Unordered List
HTML
1
<ul>
2
<li>Apple</li>
3
<li>Mango</li>
4
</ul>
Show more lines

Output:

Apple
Mango
Tables
Example
HTML
1
<table border="1">
2
<tr>
3
<th>Name</th>
4
<th>Age</th>
5
</tr>
6
 
7
<tr>
8
<td>John</td>
9
<td>20</td>
10
</tr>
11
</table>
Show more lines
Forms

Used to collect user input.

Example
HTML
1
<form>
2
Name:
3
<input type="text">
4
 
5
<input type="submit">
6
</form>
Show more lines
Text Formatting Tags
Bold
HTML
1
<b>Bold Text</b>
Show more lines
Italic
HTML
1
<i>Italic Text</i>
2
 
Show more lines
Underline
HTML
1
<u>Underlined Text</u>
Show more lines
HTML Attributes

Attributes provide additional information about elements.

Example
HTML
1
https://www.google.com
Show more lines

Here:

HTML
1
href
Show more lines

is an attribute.

HTML5 Features
Audio support
Video support
Canvas
Semantic elements
Local storage
Semantic Tags
HTML
1
<header>
2
<nav>
3
<section>
4
<article>
5
<footer>
Show more lines
Advantages of HTML
Simple and easy to learn.
Free and open standard.
Supported by all browsers.
Creates structured web pages.
Integrates with CSS and JavaScript.
Applications
Website development
Web applications
Online forms
E-commerce websites
Educational portals
Exam Point

HTML (HyperText Markup Language) is the standard markup language used to create and structure web pages. It uses tags such as <html>, <head>, <body>, <h1>, <p>, <a>, and <img> to define webpage content.

## DHTML
DHTML (Dynamic HyperText Markup Language) is a combination of HTML, CSS, JavaScript, and DOM (Document Object Model) used to create interactive and dynamic web pages.

DHTML allows the content, style, and behavior of a webpage to change dynamically without reloading the page.

Components of DHTML
1. HTML

Provides the structure of the webpage.

HTML
1
<h1>Welcome</h1>
2
<p>This is a webpage.</p>
Show more lines
2. CSS

Provides styling and layout.

CSS
1
h1 {
2
color: blue;
3
}
Show more lines
3. JavaScript

Adds interactivity and dynamic behavior.

JavaScript
1
document.getElementById("msg").innerHTML = "Hello";
Show more lines
4. DOM (Document Object Model)

Allows JavaScript to access and modify HTML elements.

JavaScript
1
document.getElementById("demo").style.color = "red";
Show more lines
Features of DHTML
Dynamic content updates.
Interactive web pages.
Event handling support.
Animation effects.
Real-time page modifications.
No page reload required for changes.
Example of DHTML
HTML
1
<!DOCTYPE html>
2
<html>
3
<body>
4
 
5
<h2 id="demo">Welcome</h2>
6
 
7
<button onclick="changeText()">Click Me</button>
8
 
9
<script>
10
function changeText()
11
{
12
document.getElementById("demo").innerHTML =
13
"DHTML Example";
14
}
15
</script>
16
 
17
</body>
18
</html>
Show more lines
Output

When the button is clicked:

Plain Text
1
Welcome
2
↓
3
DHTML Example
Show more lines
Event Handling in DHTML

DHTML responds to user actions called events.

Common Events
HTML
1
onclick
2
onmouseover
3
onmouseout
4
onchange
5
onload
Show more lines
Example
HTML
1
<button onclick="alert('Button Clicked')">
2
Click Me
3
</button>
Show more lines
Applications of DHTML
Interactive websites
Online forms
Menus and navigation bars
Animations
Games
E-commerce websites
HTML vs DHTML
HTML	DHTMLStatic web pages	Dynamic web pages
Content does not change automatically	Content can change dynamically
No interactivity	Supports interactivity
Uses only HTML	Uses HTML + CSS + JavaScript + DOM
Advantages of DHTML
Improves user experience.
Creates interactive web pages.
Reduces page reloads.
Supports animations and effects.
Faster and more responsive interfaces.
Disadvantages of DHTML
More complex than HTML.
Browser compatibility issues may occur.
Requires knowledge of JavaScript and CSS.
Exam Point

DHTML (Dynamic HTML) is a technology that combines HTML, CSS, JavaScript, and DOM to create dynamic and interactive web pages. It allows webpage content and appearance to change without reloading the page.

## CSS
CSS (Cascading Style Sheets) is a stylesheet language used to control the appearance and layout of HTML documents. It is used to add colors, fonts, spacing, positioning, and responsive designs to web pages.

Advantages of CSS
Separates content from presentation.
Improves webpage appearance.
Reduces code repetition.
Faster website maintenance.
Supports responsive web design.
Basic Syntax
CSS
1
selector
2
{
3
property: value;
4
}
Show more lines
Example
CSS
1
h1
2
{
3
color: blue;
4
}
Show more lines
Ways to Apply CSS
1. Inline CSS

Applied directly inside an HTML tag.

HTML
1
<h1 style="color:red;">Welcome</h1>
Show more lines
2. Internal CSS

Written inside the <style> tag in the HTML document.

HTML
1
<head>
2
<style>
3
h1
4
{
5
color: blue;
6
}
7
</style>
8
</head>
Show more lines
3. External CSS

Stored in a separate .css file.

style.css

CSS
1
h1
2
{
3
color: green;
4
}
5
 
Show more lines

HTML File

HTML
1
style.css
Show more lines
CSS Selectors
Element Selector
CSS
1
p
2
{
3
color: red;
4
}
Show more lines

Applies to all <p> elements.

ID Selector

Uses #.

CSS
1
#header
2
{
3
color: blue;
4
}
Show more lines

HTML:

HTML
1
<h1 id="header">Welcome</h1>
Show more lines
Class Selector

Uses .

CSS
1
.title
2
{
3
color: green;
4
}
Show more lines

HTML:

HTML
1
<h1 class="title">Welcome</h1>
Show more lines
Common CSS Properties
Text Color
CSS
1
p
2
{
3
color: red;
4
}
Show more lines
Background Color
CSS
1
body
2
{
3
background-color: lightyellow;
4
}
Show more lines
Font Size
CSS
1
h1
2
{
3
font-size: 30px;
4
}
Show more lines
Text Alignment
CSS
1
h1
2
{
3
text-align: center;
4
}
Show more lines
Border
CSS
1
div
2
{
3
border: 2px solid black;
4
}
Show more lines
Box Model

Every HTML element is treated as a box consisting of:

Content
Padding
Border
Margin

Example:

CSS
1
div
2
{
3
padding: 10px;
4
border: 1px solid black;
5
margin: 20px;
6
}
Show more lines
CSS Positioning
Static
CSS
1
position: static;
Show more lines
Relative
CSS
1
position: relative;
Show more lines
Absolute
CSS
1
position: absolute;
Show more lines
Fixed
CSS
1
position: fixed;
Show more lines
CSS List Styling
CSS
1
ul
2
{
3
list-style-type: square;
4
}
Show more lines
CSS Table Styling
CSS
1
table
2
{
3
border-collapse: collapse;
4
}
5
 
6
th, td
7
{
8
border: 1px solid black;
9
}
Show more lines
CSS Pseudo Classes
Hover Effect
CSS
1
a:hover
2
{
3
color: red;
4
}
Show more lines

Changes link color when the mouse pointer is placed over it.

Example Program
HTML
1
<!DOCTYPE html>
2
<html>
3
<head>
4
<style>
5
body
6
{
7
background-color: lightblue;
8
}
9
 
10
h1
11
{
12
color: navy;
13
text-align: center;
14
}
15
 
16
p
17
{
18
font-size: 18px;
19
}
20
</style>
21
</head>
22
 
23
<body>
24
<h1>CSS Example</h1>
25
<p>Welcome to CSS.</p>
26
</body>
27
</html>
Show more lines
HTML vs CSS
HTML	CSSDefines structure	Defines presentation
Creates content	Styles content
Uses tags	Uses selectors and properties
Static appearance	Attractive appearance
Applications of CSS
Website design
Responsive web pages
Mobile-friendly layouts
Animations and effects
User interface development
Exam Point

CSS (Cascading Style Sheets) is a stylesheet language used to control the presentation, layout, and appearance of HTML documents. CSS can be applied using Inline, Internal, or External stylesheets and uses selectors and properties to style web pages.

## XML
XML (eXtensible Markup Language) is a markup language used to store, organize, and transport data in a structured format.

Unlike HTML, XML is designed to store and exchange data, not to display it.

Features of XML
User-defined tags.
Platform independent.
Self-descriptive.
Easy to read and write.
Supports data exchange between applications.
Extensible and flexible.
Basic Structure of XML Document
XML
1
<?xml version="1.0"?>
2
 
3
<student>
4
<id>101</id>
5
<name>John</name>
6
<marks>90</marks>
7
</student>
Show more lines

Here:

<student> is the root element.
<id>, <name>, and <marks> are child elements.
XML Elements

An element consists of a start tag, content, and end tag.

XML
1
<name>John</name>
Show more lines
Start tag: <name>
Content: John
End tag: </name>
XML Tags

Tags are user-defined.

Example:

XML
1
<book>
2
<title>Programming</title>
3
</book>
Show more lines
XML Attributes

Attributes provide additional information about elements.

Syntax
XML
1
<student id="101">
2
</student>
Show more lines
Example
XML
1
<book code="B101">
2
<title>XML Basics</title>
3
</book>
Show more lines
XML Tree Structure
XML
1
<college>
2
<student>
3
<name>John</name>
4
</student>
5
</college>
Show more lines

Tree:

Plain Text
1
college
2
└── student
3
└── name
Show more lines
XML Rules
Must have a single root element.
Tags must be properly closed.
Tags are case-sensitive.
Attribute values must be enclosed in quotes.
Elements must be properly nested.
Correct
XML
1
<student>
2
<name>John</name>
3
</student>
Show more lines
Incorrect
XML
1
<student>
2
<name>John</student>
3
</name>
Show more lines
XML vs HTML
XML	HTMLUsed for storing data	Used for displaying data
User-defined tags	Predefined tags
Focuses on data	Focuses on presentation
Extensible	Fixed tag set
Advantages of XML
Easy data sharing.
Platform independent.
Human-readable format.
Supports structured data storage.
Widely used in web services.
Applications
Data exchange between systems
Web services
Configuration files
Database applications
E-commerce systems
Example XML Document
XML
1
<?xml version="1.0"?>
2
 
3
<employees>
4
<employee>
5
<id>1</id>
6
<name>Alice</name>
7
<salary>50000</salary>
8
</employee>
9
 
10
<employee>
11
<id>2</id>
12
<name>Bob</name>
13
<salary>60000</salary>
14
</employee>
15
</employees>
Show more lines
Exam Point

XML (eXtensible Markup Language) is a markup language used to store and transport data in a structured format. It uses user-defined tags, follows a hierarchical tree structure, and is widely used for data exchange between applications.

## Scripting
Scripting is the process of writing programs called scripts that automate tasks and control the behavior of software applications.

Scripts are usually executed by an interpreter rather than being compiled into machine code.

Features of Scripting Languages
Easy to learn and write.
Interpreted execution.
Rapid development.
Portable across platforms.
Used for automation and web development.
Examples of Scripting Languages
JavaScript
Python
PHP
Perl
VBScript
Bash Shell Script
Types of Scripting
1. Client-Side Scripting

Executed on the user's browser.

Example: JavaScript

HTML
1
<script>
2
alert("Hello");
3
</script>
Show more lines
Advantages
Faster execution.
Reduces server load.
Improves user interaction.
2. Server-Side Scripting

Executed on the web server.

Examples:

PHP
Python
ASP.NET
PHP
1
<?php
2
echo "Hello World";
3
?>
Show more lines
Advantages
Better security.
Access to databases.
Dynamic content generation.
Scripting vs Programming
Scripting	ProgrammingUsually interpreted	Usually compiled
Faster development	More complex development
Used for automation	Used for full applications
Examples: JavaScript, Python	Examples: C, C++
Applications of Scripting
Web development
Task automation
System administration
Data processing
Game development
Testing and deployment
Advantages
Easy coding.
Less development time.
Platform independent.
Supports automation.
Rapid prototyping.
Disadvantages
Generally slower than compiled programs.
Less efficient for large applications.
Security risks if poorly written.
Example: JavaScript Script
HTML
1
<html>
2
<body>
3
 
4
<button onclick="showMsg()">
5
Click Me
6
</button>
7
 
8
<script>
9
function showMsg()
10
{
11
alert("Welcome");
12
}
13
</script>
14
 
15
</body>
16
</html>
Show more lines

When the button is clicked, the script displays a message.

Exam Point

Scripting is the process of writing interpreted programs called scripts to automate tasks and create dynamic applications. Scripting languages include JavaScript, Python, PHP, Perl, and Bash. Scripting can be Client-Side or Server-Side.

## java Script
JavaScript (JS) is a high-level, interpreted scripting language used to create dynamic and interactive web pages. It is one of the core technologies of web development along with HTML and CSS.

HTML → Structure
CSS → Presentation
JavaScript → Behavior and Interactivity
Features of JavaScript
Interpreted language.
Object-oriented.
Platform independent.
Event-driven.
Dynamic typing.
Supports client-side and server-side programming.
Uses of JavaScript
Form validation
Web page interactivity
Animations
Games
Web applications
Server-side development (Node.js)
Adding JavaScript to HTML
Internal JavaScript
HTML
1
<!DOCTYPE html>
2
<html>
3
<body>
4
 
5
<script>
6
document.write("Hello JavaScript");
7
</script>
8
 
9
</body>
10
</html>
Show more lines
External JavaScript

app.js

JavaScript
1
document.write("Welcome");
Show more lines

HTML File

HTML
1
app.js
Show more lines
Variables

Variables store data values.

Syntax
JavaScript
1
let age = 20;
2
const PI = 3.14;
3
var name = "John";
Show more lines
Data Types
Number
JavaScript
1
let x = 10;
Show more lines
String
JavaScript
1
let name = "John";
Show more lines
Boolean
JavaScript
1
let result = true;
Show more lines
Undefined
JavaScript
1
let value;
Show more lines
Null
JavaScript
1
let data = null;
Show more lines
Operators
Arithmetic Operators
JavaScript
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

Example:

JavaScript
1
let sum = 10 + 20;
Show more lines
Relational Operators
JavaScript
1
==
2
!=
3
>
4
<
5
>=
6
<=
Show more lines
Logical Operators
JavaScript
1
&&
2
||
3
!
Show more lines
Conditional Statements
if Statement
JavaScript
1
let age = 18;
2
 
3
if(age >= 18)
4
{
5
console.log("Eligible");
6
}
Show more lines
if-else Statement
JavaScript
1
if(age >= 18)
2
{
3
console.log("Adult");
4
}
5
else
6
{
7
console.log("Minor");
8
}
9
 
Show more lines
Loops
for Loop
JavaScript
1
for(let i = 1; i <= 5; i++)
2
{
3
console.log(i);
4
}
Show more lines
while Loop
JavaScript
1
let i = 1;
2
 
3
while(i <= 5)
4
{
5
console.log(i);
6
i++;
7
}
Show more lines
Functions
Syntax
JavaScript
1
function add(a, b)
2
{
3
return a + b;
4
}
Show more lines
Example
JavaScript
1
let result = add(10, 20);
2
 
3
console.log(result);
Show more lines

Output:

Plain Text
1
30
Show more lines
Arrays
JavaScript
1
let fruits = ["Apple", "Mango", "Orange"];
Show more lines

Access:

JavaScript
1
console.log(fruits[0]);
Show more lines

Output:

Plain Text
1
Apple
Show more lines
Objects
JavaScript
1
let student =
2
{
3
name: "John",
4
age: 20
5
};
Show more lines

Access:

JavaScript
1
console.log(student.name);
Show more lines
Events

JavaScript responds to user actions.

Example
HTML
1
<button onclick="showMessage()">
2
Click Me
3
</button>
4
 
5
<script>
6
function showMessage()
7
{
8
alert("Button Clicked");
9
}
10
</script>
Show more lines
DOM (Document Object Model)

JavaScript can modify HTML elements dynamically.

HTML
1
<p id="demo">Hello</p>
2
 
3
<script>
4
document.getElementById("demo").innerHTML =
5
"Welcome";
6
</script>
Show more lines
Advantages of JavaScript
Easy to learn.
Fast execution in browsers.
Creates interactive web pages.
Reduces server load.
Supports modern web development.
Applications
Web development
Mobile applications
Game development
Server-side programming
Single Page Applications (SPA)
Exam Point

JavaScript is a high-level scripting language used to create dynamic and interactive web pages. It supports variables, functions, loops, events, objects, and DOM manipulation, making it an essential technology for modern web development.