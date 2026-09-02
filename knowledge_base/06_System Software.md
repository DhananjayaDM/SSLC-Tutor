# System Software
## Machine, Assembly and High-Level Languages
Machine Language is the lowest-level programming language consisting entirely of binary digits (0s and 1s). It is the only language directly understood by the CPU.

Example
Plain Text
1
10110000 01100001
2
00000101 00000010
3
 
Show more lines

Each binary instruction represents a specific operation.

Characteristics
Written in binary form.
Directly understood by the processor.
No translator required.
Machine dependent.
Difficult for humans to read and write.
Working
Plain Text
1
Programmer
2
↓
3
Machine Code (0s and 1s)
4
↓
5
CPU Execution
Show more lines

Since the instructions are already in machine format, the CPU executes them directly.

Advantages
Fast Execution

No translation process is required.

Direct Hardware Control

Programmer can access hardware resources directly.

Efficient Memory Usage

Consumes less memory.

Disadvantages
Difficult to Understand

Binary instructions are hard to remember.

Time Consuming

Writing large programs is extremely difficult.

Error Prone

Even a single bit error causes program failure.

Machine Dependent

Programs written for one processor may not run on another.

Applications
Embedded systems
Device drivers
Firmware programming
2. Assembly Language (Second Generation Language - 2GL)
Definition

Assembly Language is a low-level language that uses mnemonic symbols instead of binary numbers.

Example
Assembly
1
MOV A,10
2
ADD A,20
3
SUB A,5
Show more lines

Instead of remembering binary codes, programmers use meaningful abbreviations.

Mnemonic Instructions
Mnemonic	MeaningMOV	Move Data
ADD	Addition
SUB	Subtraction
MUL	Multiplication
DIV	Division
JMP	Jump
Translator: Assembler

Assembly Language cannot be executed directly.

An Assembler translates assembly instructions into machine language.

Process
Plain Text
1
Assembly Program
2
↓
3
Assembler
4
↓
5
Machine Code
6
↓
7
CPU
Show more lines
Characteristics
Uses symbolic names.
Easier than machine language.
Machine dependent.
Requires assembler.
Advantages
Easier Programming

Mnemonics are easier to remember.

Faster Execution

Produces efficient machine code.

Better Hardware Control

Provides direct access to hardware resources.

Easier Debugging

Errors can be identified more easily.

Disadvantages
Machine Dependent

Different processors require different assembly languages.

Complex for Large Programs

Writing large software systems is difficult.

Requires Hardware Knowledge

Programmer must understand computer architecture.

Applications
Operating systems
Microprocessor programming
Embedded systems
Real-time systems
3. High-Level Language (Third Generation Language - 3GL)
Definition

High-Level Languages are programming languages that use English-like statements and mathematical symbols to make programming easier.

Examples
C
C++
Java
Python
Pascal
FORTRAN
COBOL
Example Program
C Program
C
1
#include<stdio.h>
2
 
3
int main()
4
{
5
printf("Hello World");
6
return 0;
7
}
Show more lines

This is much easier to understand than assembly or machine language.

Characteristics
Human readable.
Uses English-like statements.
Machine independent.
Supports structured programming.
Easier debugging and maintenance.
Translation Process

Since computers understand only machine language, high-level programs must be translated.

Compiler

A compiler translates the entire program at once.

Plain Text
1
Source Program
2
↓
3
Compiler
4
↓
5
Object Program
6
↓
7
Machine Code
Show more lines

Examples:

C
C++
Interpreter

An interpreter translates and executes one statement at a time.

Plain Text
1
Source Program
2
↓
3
Interpreter
4
↓
5
Execution
Show more lines

Examples:

Python
JavaScript
Advantages
Easy to Learn

Uses simple syntax.

Portable

Programs can run on different machines with little modification.

Faster Development

Large applications can be developed quickly.

Easier Maintenance

Programs are easier to modify and debug.

Disadvantages
Slower Execution

Requires translation before execution.

Less Hardware Control

Compared to machine and assembly language.

More Memory Usage

Requires translator programs.

Applications
Scientific Computing
Business Applications
Web Development
Artificial Intelligence
Mobile Applications
Database Applications
Comparison of Machine, Assembly and High-Level Languages
Feature	Machine Language	Assembly Language	High-Level LanguageGeneration	1GL	2GL	3GL
Representation	Binary (0,1)	Mnemonics	English-like Statements
Translator	Not Required	Assembler	Compiler / Interpreter
Machine Dependency	Yes	Yes	No
Portability	No	No	Yes
Ease of Programming	Very Difficult	Moderate	Easy
Execution Speed	Very High	High	Moderate
Error Detection	Difficult	Moderate	Easy
Maintenance	Difficult	Moderate	Easy
Relationship Between Languages
Plain Text
1
High-Level Program
2
↓
3
Compiler / Interpreter
4
↓
5
Assembly Language
6
↓
7
Assembler
8
↓
9
Machine Language
10
↓
11
CPU Execution
12
``
Show more lines
Compiler vs Interpreter
Compiler
Translates entire program at once.
Generates object code.
Faster execution.
Reports all errors together.
Examples
C
C++
Interpreter
Translates line by line.
No separate object code generated.
Slower execution.
Stops at first error.
Examples
Python
JavaScript
Exam-Oriented Differences
Machine Language
Binary code.
Directly executed by CPU.
No translator needed.
Assembly Language
Uses mnemonics.
Requires assembler.
Machine dependent.
High-Level Language
English-like syntax.
Requires compiler/interpreter.
Machine independent.
Frequently Asked University/KSET Questions
1. What is Machine Language?

Machine Language is the lowest-level language consisting of binary instructions directly understood and executed by the CPU.

2. What is Assembly Language?

Assembly Language is a low-level language that uses mnemonic instructions and requires an assembler for translation into machine code.

3. What is High-Level Language?

High-Level Language is a user-friendly programming language that uses English-like statements and requires a compiler or interpreter for execution.

4. Differentiate Machine Language and Assembly Language.
Machine Language	Assembly LanguageUses binary code	Uses mnemonics
Difficult to write	Easier to write
No translator needed	Requires assembler
Machine dependent	Machine dependent
5. Differentiate Compiler and Interpreter.
Compiler	InterpreterTranslates whole program	Translates line by line
Faster execution	Slower execution
Generates object code	No object code
Reports all errors together	Stops at first error

## Compilers and Interpreters
A computer understands only Machine Language (binary code). Programs written in High-Level Languages such as C, C++, Java, and Python must be translated into machine code before execution.

The software used to perform this translation is called a Language Translator.

The two most common translators are:

Compiler
Interpreter
Compiler
Definition

A Compiler is a system software that translates the entire source program into machine code (object code) at once before execution.

Working
Plain Text
1
Source Program
2
↓
3
Compiler
4
↓
5
Object Program
6
↓
7
Execution
Show more lines
Example
C
1
#include<stdio.h>
2
 
3
int main()
4
{
5
printf("Hello World");
6
return 0;
7
}
8
``
Show more lines

The compiler converts the entire C program into machine code before executing it.

Characteristics
Translates the whole program at once.
Generates object code.
Reports all errors together after compilation.
Execution is faster.
Suitable for large programs.
Advantages
Faster Execution

The program is already translated before execution.

Error List

All errors are displayed together.

Reusability

Compiled object code can be executed multiple times.

Better Performance

Produces optimized machine code.

Disadvantages
Compilation Time

Entire program must be translated before execution.

Memory Requirement

Requires additional memory for object code.

Difficult to Debug

All errors are shown after compilation.

Examples of Compiled Languages
C
C++
Go
Rust
FORTRAN
Interpreter
Definition

An Interpreter is a language translator that translates and executes the source code statement-by-statement.

Working
Plain Text
1
Source Program
2
↓
3
Interpreter
4
↓
5
Translate One Line
6
↓
7
Execute
8
↓
9
Translate Next Line
Show more lines
Example
Python
1
a = 10
2
b = 20
3
print(a+b)
Show more lines

The interpreter translates and executes each line individually.

Characteristics
Translates line by line.
Executes immediately.
Does not generate object code.
Stops execution when an error occurs.
Advantages
Easy Debugging

Errors are detected immediately.

No Object Code Generation

Less storage required.

Interactive Execution

Program can be tested line by line.

Easier Development

Suitable for beginners.

Disadvantages
Slower Execution

Translation occurs during execution.

Repeated Translation

Every execution requires retranslation.

Stops at First Error

Remaining code is not executed until error is fixed.

Examples of Interpreted Languages
Python
JavaScript
Ruby
PHP
Compiler vs Interpreter
Feature	Compiler	InterpreterTranslation	Entire program at once	One statement at a time
Object Code	Generated	Not generated
Execution Speed	Faster	Slower
Error Reporting	All errors together	One error at a time
Memory Usage	More	Less
Debugging	Difficult	Easier
Program Execution	After compilation	During translation
Compilation Process

A compiler generally works in the following phases:

Lexical Analysis
Syntax Analysis
Semantic Analysis
Intermediate Code Generation
Code Optimization
Code Generation
Plain Text
1
Source Program
2
↓
3
Lexical Analysis
4
↓
5
Syntax Analysis
6
↓
7
Semantic Analysis
8
↓
9
Intermediate Code
10
↓
11
Optimization
12
↓
13
Machine Code
Show more lines
Similarities Between Compiler and Interpreter
Both are language translators.
Both convert source code into machine-understandable form.
Both detect errors in programs.
Both enable execution of high-level language programs.
Exam-Oriented Differences
Compiler
Translates complete program.
Generates object code.
Faster execution.
Example: C, C++.
Interpreter
Translates line-by-line.
No object code generated.
Slower execution.
Example: Python, JavaScript.

## Loading, Linking and Relocation; Macros, Debuggers
Loading is the process of transferring a program from secondary memory (disk) into main memory (RAM) for execution.

The system software responsible for this task is called the Loader.

Plain Text
1
Program on Disk
2
↓
3
Loader
4
↓
5
Main Memory
6
↓
7
Execution
Show more lines
Functions of Loader
Allocates memory to the program.
Loads executable code into memory.
Resolves external references.
Performs relocation.
Starts program execution.
Types of Loaders
1. Absolute Loader

Loads the program into a fixed memory location.

Advantages
Simple.
Fast loading.
Disadvantages
No relocation.
Program must always be loaded at same address.
2. Relocating Loader

Loads program at any available memory location.

Advantages
Flexibility in memory allocation.
Efficient memory usage.
3. Dynamic Loader

Loads routines only when they are needed during execution.

Advantages
Saves memory.
Faster startup.
2. Linking
Definition

Linking is the process of combining one or more object modules and libraries into a single executable program.

The software responsible is called a Linker.

Plain Text
1
Source Programs
2
↓
3
Compiler
4
↓
5
Object Files
6
↓
7
Linker
8
↓
9
Executable File
Show more lines
Need for Linking

Consider:

Module A
C
1
int add(int a,int b);
2
 
Show more lines
Module B
C
1
int add(int a,int b)
2
{
3
return a+b;
4
}
Show more lines

The linker connects these modules together.

Functions of Linker
Combines object files.
Resolves external references.
Searches required library routines.
Produces executable file.
Types of Linking
Static Linking

Libraries are copied into executable file.

Advantages
Faster execution.
Independent executable.
Disadvantages
Larger executable size.
Dynamic Linking

Library routines are loaded during execution.

Advantages
Smaller executable.
Easy library updates.
Disadvantages
Library must exist during execution.
3. Relocation
Definition

Relocation is the process of modifying address-dependent instructions when a program is loaded into memory.

Since programs may not always be loaded at the same location, addresses must be adjusted.

Example

Program assumes:

Plain Text
1
Starting Address = 1000
Show more lines

But loaded at:

Plain Text
1
Starting Address = 5000
Show more lines

Addresses must be modified.

This process is called Relocation.

Need for Relocation
Allows flexible memory allocation.
Supports multiprogramming.
Improves memory utilization.
Types of Relocation
Static Relocation

Performed before execution.

Dynamic Relocation

Performed during execution.

4. Macros
Definition

A Macro is a user-defined abbreviation for a sequence of instructions.

Rather than writing the same code repeatedly, a macro is defined once and expanded whenever needed.

Macro Structure
Macro Definition
Assembly
1
MACRO
2
INCREMENT X
3
ADD X,1
4
MEND
Show more lines
Macro Call
Assembly
1
INCREMENT A
Show more lines
After Expansion
Assembly
1
ADD A,1
Show more lines
Components of Macro Processor
Macro Definition Table (MDT)

Stores macro body.

Macro Name Table (MNT)

Stores macro names.

Argument List Array (ALA)

Stores macro arguments.

Advantages of Macros
Reduces coding effort.
Improves readability.
Avoids repetitive coding.
Easier maintenance.
Disadvantages
Larger object code after expansion.
Increased compilation time.
Macro vs Function
Macro	FunctionExpanded before execution	Executed during runtime
Faster execution	Slight call overhead
Code duplication possible	Single copy of code
Handled by Macro Processor	Handled by Compiler
5. Debuggers
Definition

A Debugger is a software tool used to detect, locate, and correct errors in programs.

It helps programmers analyze program execution.

Functions of Debugger
Execute program step-by-step.
Monitor variables.
Trace program flow.
Set breakpoints.
Identify logical and runtime errors.
Debugging Process
Plain Text
1
Program
2
↓
3
Error Found
4
↓
5
Debugger
6
↓
7
Error Correction
8
↓
9
Correct Program
Show more lines
Features of Debugger
Breakpoint

Temporary stopping point in execution.

Example:

C
1
break at line 25
Show more lines
Single Stepping

Executes one instruction at a time.

Variable Inspection

Displays values of variables during execution.

Program Trace

Shows execution sequence of statements.

Watch Point

Monitors specific variables.

Types of Errors Detected
Syntax Errors
C
1
printf("Hello")
Show more lines

Missing semicolon.

Runtime Errors
C
1
a = 10/0;
Show more lines

Division by zero.

Logical Errors

Program executes but gives incorrect output.

Common Debuggers
GDB (GNU Debugger)
Visual Studio Debugger
Turbo Debugger
Eclipse Debugger
Difference Between Loader, Linker and Debugger
Loader	Linker	DebuggerLoads program into memory	Combines object modules	Finds and fixes errors
Executes before program runs	Creates executable file	Used during testing
Memory allocation	External reference resolution	Error analysis
Produces running image	Produces executable program	Produces corrected program