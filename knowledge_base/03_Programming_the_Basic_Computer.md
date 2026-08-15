# Programming the Basic Computer
## Machine Language
Programming in Basic Computer Machine Language means writing programs using the machine instructions directly understood by the CPU.

Instruction Format

A basic computer instruction typically contains:

Opcode: Specifies the operation to perform.
Address Field: Specifies the memory location of the operand.

Example:

Plain Text
1
ADD 200
Show more lines

Meaning: Add the contents of memory location 200 to the accumulator.

Types of Instructions

Memory Reference Instructions

AND
ADD
LDA (Load Accumulator)
STA (Store Accumulator)
BUN (Branch Unconditionally)
BSA (Branch and Save Return Address)
ISZ (Increment and Skip if Zero)

Register Reference Instructions

CLA (Clear Accumulator)
CMA (Complement Accumulator)
INC (Increment Accumulator)
HLT (Halt)

Input-Output Instructions

INP (Input)
OUT (Output)
ION (Interrupt On)
IOF (Interrupt Off)
Example Program: Add Two Numbers
Plain Text
1
LDA A ; Load first number
2
ADD B ; Add second number
3
STA SUM ; Store result
4
HLT ; Stop execution
Show more lines

Where:

Plain Text
1
A = First number
2
B = Second number
3
SUM = Result location
Show more lines
Advantages
Direct control over hardware.
Efficient memory utilization.
Faster execution.
Disadvantages
Difficult to write and debug.
Machine dependent.
Time-consuming for large programs.

Exam Point: Machine language is the lowest-level programming language and is executed directly by the CPU without translation.

## Assembly Language
Assembly Language is a low-level programming language that uses symbolic instructions (mnemonics) instead of binary machine code. It serves as an interface between machine language and high-level languages.

Definition
Assembly language uses mnemonic codes to represent machine instructions.
Each assembly instruction corresponds to a machine language instruction.
An Assembler translates assembly language into machine code.
Features of Assembly Language
Uses symbolic names instead of binary codes.
Easier to write, read, and debug than machine language.
Provides direct control over hardware.
Machine dependent.
Common Assembly Language Instructions
Data Transfer Instructions
Plain Text
1
LDA 200 ; Load data from memory location 200
2
STA 300 ; Store accumulator contents at location 300
3
MOV A, B ; Transfer data from B to A
Show more lines
Arithmetic Instructions
Plain Text
1
ADD B ; Add B to accumulator
2
SUB B ; Subtract B from accumulator
3
INC A ; Increment A
4
DEC A ; Decrement A
Show more lines
Logical Instructions
Plain Text
1
AND B
2
OR B
3
XOR B
Show more lines
Branch Instructions
Plain Text
1
JMP LOOP ; Unconditional jump
2
JZ END ; Jump if zero
3
JNZ LOOP ; Jump if not zero
Show more lines
Structure of an Assembly Program
Plain Text
1
LABEL OPCODE OPERAND
Show more lines

Example:

Plain Text
1
START LDA NUM1
2
ADD NUM2
3
STA RESULT
4
HLT
Show more lines
Example Program: Addition of Two Numbers
Plain Text
1
LDA NUM1
2
ADD NUM2
3
STA RESULT
4
HLT
Show more lines

Working:

Load first number into Accumulator.
Add second number.
Store result.
Stop execution.
Advantages of Assembly Language
Easier than machine language.
Faster execution.
Efficient memory utilization.
Direct hardware control.
Easier debugging and modification.
Disadvantages of Assembly Language
Machine dependent.
Difficult for large programs.
Requires knowledge of hardware architecture.
Development is slower compared to high-level languages.
Machine Language vs Assembly Language
Machine Language	Assembly LanguageUses binary codes (0 and 1)	Uses mnemonics
Difficult to write	Easier to write
No translator required	Requires assembler
Hard to debug	Easier to debug
Machine dependent	Machine dependent
Exam Point

Assembly Language is a low-level programming language that uses mnemonic codes and symbolic addresses. An assembler converts assembly language programs into machine language for execution by the CPU.

## Assembler
An Assembler is a system software that translates an Assembly Language program into Machine Language (binary code) that can be executed by the computer's CPU.

Definition
An Assembler converts mnemonic instructions into their equivalent machine code.
It acts as a translator between Assembly Language and Machine Language.
Each assembly instruction is translated into a corresponding machine instruction.
Example

Assembly Language:

Plain Text
1
LDA NUM1
2
ADD NUM2
3
STA RESULT
4
HLT
Show more lines

Machine Language (Illustrative):

Plain Text
1
0010 1000
2
0001 1001
3
0011 1010
4
1111 0000
Show more lines

The assembler performs this translation automatically.

Functions of an Assembler
Translates assembly language into machine language.
Converts symbolic addresses into actual memory addresses.
Detects syntax errors in assembly programs.
Generates object code.
Produces listing and error reports.
Working of an Assembler
Step 1: Read Source Program
Plain Text
1
START LDA NUM1
2
ADD NUM2
3
STA RESULT
4
HLT
Show more lines
Step 2: Translate Mnemonics
Plain Text
1
LDA → Machine Opcode
2
ADD → Machine Opcode
3
STA → Machine Opcode
4
HLT → Machine Opcode
Show more lines
Step 3: Assign Memory Addresses

Labels and variables are assigned memory locations.

Step 4: Generate Object Code

The assembler produces machine-readable code.

Types of Assemblers
1. Single-Pass Assembler
Scans the source program only once.
Faster execution.
Difficult to handle forward references.
2. Two-Pass Assembler

Pass 1

Assigns addresses.
Creates the symbol table.

Pass 2

Generates machine code.
Resolves symbolic references.

Advantages:

More accurate.
Handles forward references easily.
Symbol Table

A symbol table stores:

Plain Text
1
Symbol Address
2
NUM1 100
3
NUM2 101
4
RESULT 102
Show more lines

The assembler uses this table during translation.

Assembler vs Compiler
Assembler	CompilerConverts Assembly Language to Machine Language	Converts High-Level Language to Machine Language
Uses mnemonics	Uses high-level statements
One assembly instruction translates to one machine instruction	One statement may generate many machine instructions
Faster translation	More complex translation
Advantages of an Assembler
Simplifies programming compared to machine language.
Uses meaningful mnemonics.
Reduces programming errors.
Easier debugging and maintenance.
Faster program development.
Disadvantages of an Assembler
Machine dependent.
Requires knowledge of computer architecture.
Not suitable for very large applications.
Less portable than high-level languages.
Applications of Assemblers
System software development.
Operating systems.
Embedded systems.
Device drivers.
Real-time control systems.
Microprocessor programming.
Exam Point

Assembler is a system software that converts Assembly Language programs into Machine Language and generates executable object code for the CPU.

## Program Loops Subroutines
A Program Loop is a sequence of instructions that is executed repeatedly until a specified condition is satisfied.

Definition
A loop allows a set of instructions to be executed multiple times.
It reduces program size and avoids writing the same instructions repeatedly.
Loops are commonly implemented using branch instructions.
Components of a Loop
Initialization
Condition Checking
Loop Body
Update Operation
Loop Exit
Example
Plain Text
1
LOOP: ADD NUM
2
ISZ COUNT
3
BUN LOOP
4
 
Show more lines
Working
ADD NUM adds the value.
ISZ COUNT increments COUNT and skips the next instruction if COUNT becomes zero.
BUN LOOP branches back to LOOP.
Execution continues until the condition is met.
Advantages of Loops
Reduces program length.
Saves memory.
Simplifies coding.
Improves program efficiency.
Applications
Repetitive calculations.
Array processing.
Data processing.
Counting operations.
Subroutines

A Subroutine is a group of instructions designed to perform a specific task and can be called from different parts of a program.

Definition
A subroutine is a reusable program module.
It avoids duplication of code.
Control returns to the calling program after execution.
Need for Subroutines
Reduce program size.
Increase modularity.
Improve readability.
Simplify debugging and maintenance.
Subroutine Call and Return

In a basic computer:

Plain Text
1
BSA SUBR
Show more lines
BSA (Branch and Save Return Address) is used to call a subroutine.
The return address is stored before branching to the subroutine.

Subroutine:

Plain Text
1
SUBR, ...
2
...
3
BUN I SUBR
Show more lines
BUN I SUBR returns control to the calling program.
Working of a Subroutine
Main program calls the subroutine using BSA.
Return address is saved.
Control transfers to the subroutine.
Required task is executed.
Control returns using BUN I.
Example
Plain Text
1
MAIN, BSA SUM
2
HLT
3
 
4
SUM, ADD NUM1
5
ADD NUM2
6
BUN I SUM
Show more lines
Advantages of Subroutines
Code reusability.
Reduced memory usage.
Easier maintenance.
Modular programming.
Improved readability.
Applications
Mathematical calculations.
Input/Output processing.
Data conversion.
String manipulation.
Operating system routines.
Difference Between Loops and Subroutines
Program Loop	SubroutineRepeats a set of instructions	Performs a specific task
Used for iteration	Used for modularity
Control stays inside the loop until the condition is met	Control returns to the caller after execution
Implemented using branch instructions	Implemented using call and return instructions
Reduces repetitive execution statements	Reduces duplicate code
Exam Point

Program Loop is a mechanism for repeatedly executing a set of instructions until a condition is satisfied, whereas a Subroutine is a reusable block of instructions that performs a specific task and returns control to the calling program.

## Input-Output Programming
nput-Output Programming refers to the techniques and instructions used to transfer data between the CPU, memory, and external input/output devices such as keyboards, printers, monitors, and storage devices.

It enables communication between the computer system and peripheral devices.

Need for Input-Output Programming
Transfer data between CPU and I/O devices.
Communicate with external peripherals.
Improve system efficiency.
Coordinate devices operating at different speeds.
Support user interaction with the computer.
Basic I/O Organization
Plain Text
1
Input Device
2
↓
3
Input Register
4
↓
5
CPU
6
↓
7
Output Register
8
↓
9
Output Device
Show more lines
Components
CPU: Processes data and controls operations.
Memory: Stores instructions and data.
Input Register (INPR): Receives data from input devices.
Output Register (OUTR): Sends data to output devices.
I/O Interface: Connects devices with the CPU.
Input-Output Instructions
Input Instruction (INP)
Plain Text
1
INP
Show more lines
Transfers data from an input device to the Accumulator (AC).
Data passes through the Input Register.

Operation:

Plain Text
1
Input Device → INPR → AC
Show more lines
Output Instruction (OUT)
Plain Text
1
OUT
Show more lines
Transfers data from the Accumulator to an output device.

Operation:

Plain Text
1
AC → OUTR → Output Device
Show more lines
Skip Instructions
SKI (Skip on Input Flag)
Plain Text
1
SKI
Show more lines
Skips the next instruction if the input flag is set.
SKO (Skip on Output Flag)
Plain Text
1
SKO
Show more lines
Skips the next instruction if the output flag is set.
Interrupt Control Instructions
ION
Plain Text
1
ION
Show more lines
Enables interrupts.
IOF
Plain Text
1
IOF
Show more lines
Disables interrupts.
Methods of Input-Output Programming
1. Programmed I/O
Definition

The CPU continuously checks whether an I/O device is ready for data transfer.

Working
CPU checks device status.
CPU waits until the device is ready.
Data transfer occurs.
Advantages
Simple implementation.
Low hardware cost.
Disadvantages
CPU remains busy.
Wastes processor time.
2. Interrupt-Driven I/O
Definition

The I/O device interrupts the CPU whenever it is ready to transfer data.

Working
CPU executes other tasks.
Device generates an interrupt.
CPU services the request.
Data transfer takes place.
Advantages
Better CPU utilization.
Faster response.
Disadvantages
More complex than Programmed I/O.
3. Direct Memory Access (DMA)
Definition

DMA allows data transfer directly between memory and I/O devices without continuous CPU involvement.

Working
CPU initiates DMA transfer.
DMA Controller takes control.
Data moves directly between memory and the device.
CPU is notified after completion.
Advantages
High-speed transfer.
Reduced CPU workload.
Efficient for large data blocks.
Disadvantages
Additional hardware required.
More complex implementation.
DMA Controller Functions
Generates memory addresses.
Controls data transfer.
Maintains transfer count.
Sends completion signal to CPU.
Programmed I/O vs Interrupt I/O vs DMA
Feature	Programmed I/O	Interrupt I/O	DMACPU Involvement	High	Medium	Very Low
Speed	Low	Medium	High
Hardware Complexity	Low	Medium	High
CPU Utilization	Poor	Better	Excellent
Applications of Input-Output Programming
Computers and laptops
Smartphones
Embedded systems
Industrial automation
Communication systems
Banking applications
Medical equipment
Data acquisition systems
Exam Point

Input-Output Programming is the process of transferring data between the CPU, memory, and peripheral devices using Programmed I/O, Interrupt-Driven I/O, or DMA techniques. DMA provides the highest efficiency because data is transferred directly between memory and I/O devices with minimal CPU involvement.