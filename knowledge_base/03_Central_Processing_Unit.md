# Central Processing Unit
## General Register Organization
General Register Organization is the arrangement of registers within the CPU and the method used to transfer and process data among them.

A CPU contains several high-speed registers used for storing data, instructions, addresses, and intermediate results during program execution.

Need for General Register Organization
Provides fast data storage inside the CPU.
Reduces memory access time.
Increases processing speed.
Facilitates efficient execution of instructions.
Supports arithmetic and logical operations.
Components of General Register Organization
1. Register Set

A collection of registers within the CPU.

Example:

Plain Text
1
R0, R1, R2, R3, ... , Rn
2
 
Show more lines

Each register can store binary information.

2. Multiplexers (MUX)
Select source registers.
Transfer selected register contents to the bus.
3. Common Bus System
Shared communication path used to transfer data among registers.
Reduces the number of direct connections required.
4. Arithmetic Logic Unit (ALU)

Performs:

Arithmetic operations

Addition
Subtraction
Increment
Decrement

Logical operations

AND
OR
XOR
NOT
5. Control Unit
Generates control signals.
Selects registers.
Controls ALU operations.
Coordinates data transfers.
General Register Organization Structure
Plain Text
1
Register Set
2
R0 R1 R2 R3 ... Rn
3
\ | | | /
4
\ | | | /
5
Multiplexers
6
|
7
Common Bus
8
|
9
ALU
10
|
11
Destination
12
Register
Show more lines
Working
Source registers are selected.
Their contents are transferred through multiplexers.
Data reaches the ALU.
ALU performs the required operation.
Result is stored in a destination register.
Register Transfer Operation

Example:

Plain Text
1
R1 ← R2
Show more lines

Meaning:

Contents of register R2 are copied into register R1.

Example:

Plain Text
1
R3 ← R1 + R2
Show more lines

Meaning:

ALU adds contents of R1 and R2.
Result is stored in R3.
Control Word

A Control Word is a binary word that specifies:

Source registers
Destination register
ALU operation

Example:

Plain Text
1
R3 ← R1 + R2
Show more lines

Control word selects:

Source A = R1
Source B = R2
ALU operation = ADD
Destination = R3
Advantages of General Register Organization
Faster execution.
Reduced memory access.
Efficient data transfer.
Improved CPU performance.
Simplified control operations.
Applications
Microprocessors
Microcontrollers
Digital signal processors
Embedded systems
Computers and servers
Real-time control systems
Exam Point

General Register Organization is the arrangement of multiple CPU registers connected through a common bus and ALU, enabling efficient data transfer and arithmetic/logical operations under the control of the Control Unit.

## Stack Organization
Stack Organization is a method of organizing data in memory using a stack, which follows the Last In First Out (LIFO) principle.

In a stack, the last data item inserted is the first one removed.

Need for Stack Organization
Temporary storage of data.
Function and subroutine calls.
Saving return addresses.
Expression evaluation.
Interrupt handling.
Basic Concept

A stack consists of a sequence of memory locations where data is added and removed from only one end called the Top of Stack (TOS).

Plain Text
1
Top
2
↓
3
+-----+
4
| 40 |
5
+-----+
6
| 30 |
7
+-----+
8
| 20 |
9
+-----+
10
| 10 |
11
+-----+
Show more lines

In this stack:

40 was inserted last.
40 will be removed first.
Stack Pointer (SP)

The Stack Pointer (SP) is a special register that contains the address of the top element of the stack.

Functions of SP:

Points to the top of the stack.
Updated whenever data is pushed or popped.
Controls stack operations.
Stack Operations
1. PUSH Operation

Used to insert data onto the stack.

Example:

Plain Text
1
PUSH 50
Show more lines

Before:

Plain Text
1
Top → 40
Show more lines

After:

Plain Text
1
Top → 50
2
40
3
30
4
20
5
10
Show more lines

Operation:

Plain Text
1
SP ← SP + 1
2
M[SP] ← Data
Show more lines
2. POP Operation

Used to remove data from the stack.

Example:

Plain Text
1
POP
2
 
Show more lines

Before:

Plain Text
1
Top → 50
2
40
3
30
Show more lines

After:

Plain Text
1
Top → 40
2
30
Show more lines

Operation:

Plain Text
1
Data ← M[SP]
2
SP ← SP - 1
Show more lines
Types of Stack
Register Stack
Implemented using CPU registers.
Very fast access.
Limited storage capacity.
Memory Stack
Implemented in main memory.
Large storage capacity.
Slower than register stack.
Stack in Subroutine Calls

When a subroutine is called:

Return address is pushed onto the stack.
Control transfers to the subroutine.
After execution, return address is popped.
Control returns to the calling program.

Example:

Plain Text
1
CALL SUBR
2
...
3
SUBR:
4
...
5
RETURN
Show more lines
Applications of Stack
Subroutine handling.
Recursion.
Expression evaluation.
Interrupt processing.
Compiler design.
Function call management.
Advantages of Stack Organization
Simple data management.
Efficient memory utilization.
Fast access to recently used data.
Supports nested subroutines.
Simplifies expression evaluation.
Disadvantages of Stack Organization
Limited direct access to stored elements.
Possible stack overflow.
LIFO order may not suit all applications.
Stack Overflow and Underflow
Stack Overflow

Occurs when data is pushed into a full stack.

Stack Underflow

Occurs when data is popped from an empty stack.

Exam Point

Stack Organization is a data storage technique based on the Last In First Out (LIFO) principle. It uses a Stack Pointer (SP) to manage PUSH and POP operations and is widely used for subroutine calls, recursion, and temporary data storage.

## Instruction Formats
An Instruction Format is the arrangement of bits in an instruction word that specifies the operation to be performed and the operands involved in the operation.

It defines how an instruction is represented in memory and interpreted by the CPU.

Need for Instruction Formats
Specify the operation to be performed.
Identify the operand location.
Facilitate instruction decoding.
Organize data and control information efficiently.
Enable communication between software and hardware.
Components of an Instruction Format
1. Opcode Field
Specifies the operation to be performed.
Determined by the Control Unit during decoding.

Examples:

Plain Text
1
ADD
2
SUB
3
LOAD
4
STORE
5
AND
6
OR
Show more lines
2. Address Field (Operand Field)
Contains the address of the operand.
May specify a memory location, register, or immediate data.

Example:

Plain Text
1
ADD 500
Show more lines
Opcode = ADD
Address = 500
General Instruction Format
Plain Text
1
+----------------+----------------+
2
| Opcode | Address |
3
+----------------+----------------+
Show more lines

Where:

Opcode → Operation
Address → Operand location
Instruction Format in Basic Computer

A basic computer commonly uses a 16-bit instruction word.

Format
Plain Text
1
+---+------+-------------+
2
| I |Opcode| Address |
3
+---+------+-------------+
4
1 3 12 bits
Show more lines
Fields
I Bit (Indirect Bit)
Indicates addressing mode.
0 = Direct Addressing
1 = Indirect Addressing
Opcode
Specifies the operation.
Address
Contains the memory address.
Types of Instruction Formats
1. Memory Reference Instruction Format

Used for instructions that access memory.

Format:

Plain Text
1
+---+------+-------------+
2
| I |Opcode| Address |
3
+---+------+-------------+
Show more lines

Examples:

Plain Text
1
AND
2
ADD
3
LDA
4
STA
5
BUN
6
BSA
7
ISZ
Show more lines
2. Register Reference Instruction Format

Used for operations on CPU registers.

Format:

Plain Text
1
+---+------+-------------+
2
| 0 | 111 | Register Ops|
3
+---+------+-------------+
Show more lines

Examples:

Plain Text
1
CLA
2
CLE
3
CMA
4
CME
5
INC
6
SPA
7
SNA
8
HLT
Show more lines
3. Input-Output Instruction Format

Used for communication with I/O devices.

Format:

Plain Text
1
+---+------+-------------+
2
| 1 | 111 | I/O Function|
3
+---+------+-------------+
Show more lines

Examples:

Plain Text
1
INP
2
OUT
3
SKI
4
SKO
5
ION
6
IOF
Show more lines
Addressing Modes Related to Instruction Format
Direct Addressing
Plain Text
1
Address field = Actual operand address
Show more lines

Example:

Plain Text
1
LDA 500
Show more lines

Operand stored at memory location 500.

Indirect Addressing
Plain Text
1
Address field = Address of address
Show more lines

Example:

Plain Text
1
LDA I 500
Show more lines

Memory location 500 contains the actual operand address.

Immediate Addressing
Plain Text
1
Operand is part of the instruction.
Show more lines

Example:

Plain Text
1
MOV A, #10
Show more lines

Value 10 is directly available.

Advantages of Instruction Formats
Efficient instruction representation.
Simplifies CPU decoding.
Supports different addressing modes.
Enables flexible programming.
Improves processor performance.
Applications
Computer systems
Microprocessors
Embedded systems
Digital signal processors
Microcontrollers
Operating systems
Exam Point

Instruction Format is the bit layout of an instruction that specifies the operation (Opcode) and operand information (Address Field). In a basic computer, the 16-bit instruction format consists of an I-bit, Opcode field, and Address field.

## Addressing Modes
Addressing Modes are the methods used by the CPU to determine the location of an operand (data) required for executing an instruction.

They specify how the operand is accessed from memory, registers, or the instruction itself.

Need for Addressing Modes
Provide flexibility in programming.
Reduce instruction size.
Improve execution efficiency.
Enable access to data stored in different locations.
Simplify instruction execution.
Types of Addressing Modes
1. Direct Addressing Mode

In direct addressing, the address field of the instruction contains the actual address of the operand.

Format
Plain Text
1
Operand Address = Address Field
Show more lines
Example
Plain Text
1
LDA 500
Show more lines

If:

Plain Text
1
M[500] = 25
Show more lines

Then:

Plain Text
1
AC ← M[500]
2
AC = 25
Show more lines
Advantages
Simple implementation.
Fast operand access.
Disadvantage
Limited address range.
2. Indirect Addressing Mode

In indirect addressing, the address field contains the address of a memory location that stores the actual operand address.

Format
Plain Text
1
Effective Address = M[Address Field]
Show more lines
Example
Plain Text
1
LDA I 500
Show more lines

If:

Plain Text
1
M[500] = 700
2
M[700] = 25
Show more lines

Then:

Plain Text
1
AC ← M[700]
2
AC = 25
Show more lines
Advantages
Larger address range.
Flexible memory access.
Disadvantage
Requires an additional memory reference.
3. Immediate Addressing Mode

The operand itself is present within the instruction.

Format
Plain Text
1
Operand = Instruction Data
Show more lines
Example
Plain Text
1
MOV A, #10
Show more lines

Then:

Plain Text
1
A ← 10
Show more lines
Advantages
Fast execution.
No memory access required.
Disadvantage
Limited operand size.
4. Register Addressing Mode

The operand is stored in a CPU register.

Example
Plain Text
1
ADD R1
Show more lines

If:

Plain Text
1
R1 = 20
Show more lines

Then:

Plain Text
1
AC ← AC + R1
Show more lines
Advantages
Very fast access.
No memory reference needed.
Disadvantage
Limited number of registers.
5. Register Indirect Addressing Mode

A register contains the address of the operand.

Example
Plain Text
1
ADD (R1)
2
 
Show more lines

If:

Plain Text
1
R1 = 500
2
M[500] = 20
Show more lines

Then:

Plain Text
1
AC ← AC + M[500]
Show more lines
Advantages
Flexible addressing.
Fewer memory accesses.
6. Indexed Addressing Mode

The effective address is obtained by adding an index register value to the address field.

Format
Plain Text
1
EA = Address Field + Index Register
Show more lines
Example
Plain Text
1
LOAD 500(X)
Show more lines

If:

Plain Text
1
X = 20
Show more lines

Then:

Plain Text
1
EA = 500 + 20 = 520
Show more lines
Applications
Arrays
Tables
Loops
7. Relative Addressing Mode

The effective address is obtained by adding the Program Counter (PC) value to the address field.

Format
Plain Text
1
EA = PC + Address Field
2
 
Show more lines
Example
Plain Text
1
BRANCH 50
Show more lines

If:

Plain Text
1
PC = 100
Show more lines

Then:

Plain Text
1
EA = 150
Show more lines
Applications
Branch instructions
Program relocation
8. Stack Addressing Mode

The operand is stored on the top of the stack.

Example
Plain Text
1
PUSH A
2
POP B
Show more lines

Operations are performed using the Stack Pointer (SP).

Applications
Subroutines
Recursion
Expression evaluation
Comparison of Addressing Modes
Addressing Mode	Operand Location	SpeedImmediate	Inside instruction	Very Fast
Register	CPU Register	Very Fast
Direct	Memory Location	Fast
Indirect	Memory Address Stored in Memory	Moderate
Register Indirect	Memory Address Stored in Register	Fast
Indexed	Address + Index Register	Moderate
Relative	PC + Address	Moderate
Stack	Top of Stack	Fast
Direct vs Indirect Addressing
Direct Addressing
Plain Text
1
Instruction → Address → Operand
Show more lines

Example:

Plain Text
1
LDA 500
Show more lines
Indirect Addressing
Plain Text
1
Instruction → Address → Address → Operand
Show more lines

Example:

Plain Text
1
LDA I 500
Show more lines
Advantages of Addressing Modes
Flexible data access.
Efficient memory utilization.
Reduced instruction length.
Faster execution in many cases.
Supports complex programming structures.
Applications
Microprocessors
Computer Architecture
Embedded Systems
Operating Systems
Compilers
Assembly Language Programming
Exam Point

Addressing Modes specify how the CPU locates operands required by an instruction. The most commonly used addressing modes are Direct, Indirect, Immediate, Register, Register Indirect, Indexed, Relative, and Stack Addressing. In a Basic Computer, Direct and Indirect Addressing are primarily used through the I-bit of the instruction format.

## RISC Computer
RISC (Reduced Instruction Set Computer) is a computer architecture that uses a small, simple, and highly optimized set of instructions. Each instruction is designed to execute very quickly, usually in a single clock cycle.

The main goal of RISC is to improve processor performance by simplifying instruction execution.

Characteristics of RISC
Uses a small set of simple instructions.
Most instructions execute in one clock cycle.
Fixed-length instruction formats.
Fewer addressing modes.
Large number of general-purpose registers.
Uses a Load/Store Architecture.
Designed for efficient pipelining.
RISC Architecture
Plain Text
1
Memory
2
↑
3
↓
4
Load / Store
5
↓
6
CPU Registers
7
↓
8
ALU
Show more lines

In RISC:

Arithmetic and logical operations are performed only on registers.
Data must first be loaded from memory into registers.
Results are stored back into memory using store instructions.
Example
RISC Style
Plain Text
1
LOAD R1, A
2
LOAD R2, B
3
ADD R3, R1, R2
4
STORE R3, C
Show more lines
Working
Load A into R1.
Load B into R2.
Add R1 and R2.
Store result in C.
Features of RISC
1. Simple Instructions

Example:

Plain Text
1
ADD
2
SUB
3
LOAD
4
STORE
Show more lines
2. Fixed Instruction Length

Example:

Plain Text
1
32-bit instruction format
2
 
Show more lines

Benefits:

Easy decoding.
Faster execution.
3. Large Register Set

Example:

Plain Text
1
R0, R1, R2, ... R31
Show more lines

Benefits:

Reduces memory access.
Improves speed.
4. Load/Store Architecture

Only Load and Store instructions access memory.

Example:

Plain Text
1
LOAD R1, A
2
STORE R1, B
3
 
Show more lines
5. Efficient Pipelining

Multiple instructions can execute simultaneously at different stages.

Plain Text
1
Fetch
2
Decode
3
Execute
4
Memory
5
Write Back
Show more lines
Advantages of RISC
Faster execution speed.
Simple hardware design.
Efficient pipelining.
Reduced instruction execution time.
Lower power consumption.
Easier processor design.
Disadvantages of RISC
Program size may be larger.
More instructions may be required for complex tasks.
Greater dependence on compiler optimization.
RISC vs CISC
Feature	RISC	CISCInstruction Set	Small	Large
Instruction Length	Fixed	Variable
Execution Time	Usually 1 Clock Cycle	Multiple Clock Cycles
Addressing Modes	Few	Many
Hardware Complexity	Simple	Complex
Pipelining	Easy	Difficult
Registers	More	Fewer
Examples of RISC Processors
ARM
MIPS
SPARC
PowerPC
RISC-V
Applications
Smartphones
Tablets
Embedded Systems
Microcontrollers
Networking Devices
Modern ARM-based Computers
Exam Point

RISC (Reduced Instruction Set Computer) is a processor architecture that uses a small set of simple instructions, a large number of registers, fixed-length instruction formats, and load/store operations to achieve high-speed execution and efficient pipelining.

## CISC Computer
CISC (Complex Instruction Set Computer) is a computer architecture that uses a large set of complex instructions. A single instruction can perform multiple operations, reducing the number of instructions required to execute a program.

The main objective of CISC is to simplify programming by providing powerful instructions.

Characteristics of CISC
Large instruction set.
Complex instructions.
Variable-length instruction formats.
Many addressing modes.
Instructions may take multiple clock cycles to execute.
Memory-to-memory operations are supported.
Hardware design is more complex.
CISC Architecture
Plain Text
1
Memory
2
↑
3
↓
4
CPU
5
↓
6
ALU
7
 
Show more lines

In CISC:

Instructions can directly access memory.
One instruction may perform several tasks.
Fewer instructions are needed for a program.
Example
CISC Style
Plain Text
1
ADD A, B
Show more lines
Working

A single instruction:

Fetches A from memory.
Fetches B from memory.
Performs addition.
Stores the result.

Thus, one instruction can perform multiple operations.

Features of CISC
1. Large Instruction Set

Examples:

Plain Text
1
ADD
2
SUB
3
MUL
4
DIV
5
MOV
6
CALL
7
RET
Show more lines
2. Variable-Length Instructions

Instructions may have different sizes.

Example:

Plain Text
1
1 byte
2
2 bytes
3
4 bytes
Show more lines
3. Multiple Addressing Modes

Supports:

Direct Addressing
Indirect Addressing
Indexed Addressing
Relative Addressing
Register Addressing
4. Memory-to-Memory Operations

Example:

Plain Text
1
ADD A, B
Show more lines

The processor can operate directly on memory locations.

5. Complex Hardware
Requires a sophisticated control unit.
More decoding logic is needed.
Often uses microprogrammed control.
Advantages of CISC
Fewer instructions per program.
Easier programming.
Reduced program size.
Efficient use of memory.
Powerful instruction set.
Disadvantages of CISC
Complex processor design.
Higher hardware cost.
More difficult pipelining.
Instructions may require multiple clock cycles.
Greater power consumption.
CISC vs RISC
Feature	CISC	RISCInstruction Set	Large	Small
Instruction Format	Variable Length	Fixed Length
Addressing Modes	Many	Few
Registers	Fewer	More
Execution Time	Multiple Cycles	Usually Single Cycle
Hardware Design	Complex	Simple
Pipelining	Difficult	Easy
Program Size	Smaller	Larger
Examples of CISC Processors
Intel x86
Intel Pentium
Intel Core Series
AMD Athlon
AMD Ryzen
Applications
Personal Computers
Laptops
Workstations
Servers
Desktop Operating Systems
Exam Point

CISC (Complex Instruction Set Computer) is a processor architecture that uses a large set of complex instructions, supports multiple addressing modes, and allows memory-to-memory operations, reducing the number of instructions required to execute a program.