# Memory Hierarchy
## Main Memory
Main Memory (also called Primary Memory or Internal Memory) is the memory directly accessible by the CPU. It stores programs, instructions, and data that are currently being used by the computer.

It acts as a working area between the CPU and secondary storage devices.

Characteristics of Main Memory
Directly accessible by the CPU.
Stores currently executing programs and data.
Faster than secondary memory.
Limited storage capacity.
Volatile in nature (RAM loses data when power is off).
Block Diagram
Plain Text
1
CPU
2
│
3
▼
4
Main Memory
5
│
6
▼
7
Secondary Storage
Show more lines
Functions of Main Memory
Stores operating system instructions.
Stores application programs currently in use.
Stores input data and processing results.
Supplies instructions and data to the CPU.
Stores intermediate processing results.
Types of Main Memory
1. RAM (Random Access Memory)

RAM is a read-write memory that stores data temporarily.

Features
Volatile memory.
Data is lost when power is switched off.
Fast access speed.
Used during program execution.
Types of RAM
SRAM (Static RAM)
Uses flip-flops to store data.
Does not require refreshing.
Very fast.
Expensive.
Used in cache memory.
DRAM (Dynamic RAM)
Uses capacitors to store data.
Requires periodic refreshing.
Slower than SRAM.
Less expensive.
Used as main memory.
2. ROM (Read Only Memory)

ROM stores permanent information.

Features
Non-volatile memory.
Retains data even when power is off.
Used to store firmware and boot programs.
Types of ROM
PROM (Programmable ROM)
EPROM (Erasable PROM)
EEPROM (Electrically Erasable PROM)
Memory Organization

A memory unit consists of:

Plain Text
1
Memory = Words × Bits
Show more lines

Example:

Plain Text
1
1024 × 16
Show more lines

Means:

1024 memory locations
Each location stores 16 bits
Memory Operations
Read Operation
Plain Text
1
Memory Location → CPU
Show more lines
CPU reads data from memory.
Write Operation
Plain Text
1
CPU → Memory Location
Show more lines
CPU stores data into memory.
Main Memory vs Secondary Memory
Feature	Main Memory	Secondary MemoryAccess Speed	Fast	Slow
CPU Access	Direct	Indirect
Capacity	Smaller	Larger
Cost	Higher	Lower
Volatility	Usually Volatile	Non-Volatile
Examples	RAM, ROM	HDD, SSD, DVD
Advantages of Main Memory
Fast data access.
Direct communication with CPU.
Improves processing speed.
Stores active programs and data.
Disadvantages of Main Memory
Limited capacity.
Higher cost per bit.
RAM loses data when power is off.
Applications
Operating system storage during execution.
Program execution.
Data processing.
Temporary storage of user data.
Intermediate result storage.
Exam Point

Main Memory is the primary memory directly accessible by the CPU. It stores programs, instructions, and data currently being processed. The two main types of primary memory are RAM (volatile) and ROM (non-volatile).

## Auxiliary Memory
Auxiliary Memory (also called Secondary Memory or External Memory) is a storage device used to store data and programs permanently. It is not directly accessed by the CPU and provides large-capacity storage for long-term data retention.

Need for Auxiliary Memory
Main memory has limited capacity.
RAM is volatile and loses data when power is off.
Large amounts of data need permanent storage.
Used for backup and archival purposes.
Characteristics of Auxiliary Memory
Non-volatile storage.
Large storage capacity.
Lower cost per bit than main memory.
Slower access compared to main memory.
Data remains stored even after power is turned off.
Block Diagram
Plain Text
1
CPU
2
│
3
▼
4
Main Memory
5
│
6
▼
7
Auxiliary Memory
Show more lines
Functions of Auxiliary Memory
Permanent storage of programs.
Permanent storage of user data.
Backup and recovery.
Long-term information retention.
Storage of operating systems and applications.
Types of Auxiliary Memory
1. Magnetic Disk Storage
Hard Disk Drive (HDD)
Stores data magnetically on rotating disks.
Large storage capacity.
Non-volatile.

Advantages:

Large capacity
Low cost

Disadvantages:

Mechanical parts
Slower than SSD
2. Solid State Storage
Solid State Drive (SSD)
Uses flash memory.
No moving parts.
Faster than HDD.

Advantages:

High speed
Reliable
Low power consumption

Disadvantages:

More expensive than HDD
3. Optical Storage

Examples:

CD
DVD
Blu-ray Disc

Data is stored using laser technology.

Applications:

Software distribution
Multimedia storage
Backup
4. Flash Memory Devices

Examples:

Pen Drives
Memory Cards
USB Flash Drives

Features:

Portable
Rewritable
Non-volatile
5. Magnetic Tape
Stores data on magnetic tape.
Very large storage capacity.
Used for backup and archival storage.

Advantage:

Low cost for large data storage

Disadvantage:

Sequential access
Memory Hierarchy
Plain Text
1
Registers
2
↓
3
Cache Memory
4
↓
5
Main Memory
6
↓
7
Auxiliary Memory
Show more lines
Speed Order
Plain Text
1
Registers > Cache > Main Memory > Auxiliary Memory
Show more lines
Capacity Order
Plain Text
1
Auxiliary Memory > Main Memory > Cache > Registers
Show more lines
Auxiliary Memory vs Main Memory
Feature	Main Memory	Auxiliary MemoryAccess by CPU	Direct	Indirect
Speed	Fast	Slow
Capacity	Smaller	Larger
Cost per Bit	Higher	Lower
Volatility	Usually Volatile	Non-Volatile
Examples	RAM, ROM	HDD, SSD, CD, DVD
Advantages of Auxiliary Memory
Permanent storage.
Large capacity.
Low cost per bit.
Suitable for backup and archival.
Retains data without power.
Disadvantages of Auxiliary Memory
Slower access speed.
Not directly accessible by CPU.
Requires data transfer to main memory before processing.
Applications
Operating system storage.
Software installation.
Multimedia storage.
Database storage.
Backup and recovery systems.
Cloud and enterprise storage solutions.
Exam Point

Auxiliary Memory is a non-volatile secondary storage used for permanent data storage. It provides large storage capacity at a lower cost than main memory and includes devices such as HDDs, SSDs, CDs, DVDs, USB drives, and magnetic tapes.

## Associative Memory
Associative Memory (also called Content Addressable Memory - CAM) is a special type of memory in which data is accessed based on its content rather than its memory address.

Unlike conventional memory, where an address is supplied to retrieve data, associative memory searches all memory locations simultaneously and returns the location containing the matching data.

Need for Associative Memory
High-speed data searching.
Fast retrieval of information.
Parallel comparison of stored data.
Efficient lookup operations.
Basic Concept
Conventional Memory
Plain Text
1
Address → Memory → Data
Show more lines

Example:

Plain Text
1
Address 100 → 25
Show more lines
Associative Memory
Plain Text
1
Data → Memory Search → Address/Match
Show more lines

Example:

Plain Text
1
Search Key = 25
Show more lines

Memory automatically searches all locations and finds where 25 is stored.

Block Diagram
Plain Text
1
Search Data
2
│
3
▼
4
+------------------+
5
| Associative |
6
| Memory (CAM) |
7
+------------------+
8
│
9
▼
10
Match Information
Show more lines
Working of Associative Memory
A search key is placed in the argument register.
The search key is compared simultaneously with all stored words.
Matching words are identified.
Match register indicates the matched locations.
The desired data is accessed.
Example

Memory Contents:

Plain Text
1
Location 0 → 1010
2
Location 1 → 1100
3
Location 2 → 1001
4
Location 3 → 1111
Show more lines

Search:

Plain Text
1
1010
Show more lines

Result:

Plain Text
1
Match Found at Location 0
Show more lines
Components of Associative Memory
1. Argument Register
Stores the search data.
Contains the value to be searched.
2. Memory Array
Stores the data words.
All words are compared in parallel.
3. Match Register
Indicates which memory word matches the search key.
4. Read/Write Logic
Controls memory operations.
Associative Memory Organization
Plain Text
1
Argument Register
2
│
3
▼
4
+---------------------------+
5
| Associative Memory |
6
| |
7
| Word 0 Comparator |
8
| Word 1 Comparator |
9
| Word 2 Comparator |
10
| Word n Comparator |
11
+---------------------------+
12
│
13
▼
14
Match Register
Show more lines
Advantages of Associative Memory
Very fast searching.
Parallel data comparison.
Reduced search time.
Efficient retrieval of information.
Suitable for real-time applications.
Disadvantages of Associative Memory
Expensive hardware.
Complex design.
Higher power consumption.
Limited storage capacity.
Applications of Associative Memory
Cache Memory

Used for fast cache tag matching.

Translation Lookaside Buffer (TLB)

Used in virtual memory systems for rapid address translation.

Routers and Networking Devices

Used for fast packet lookup and routing decisions.

Database Search Systems

Used for high-speed record matching.

Artificial Intelligence Systems

Used where rapid pattern matching is required.

Associative Memory vs Conventional Memory
Feature	Associative Memory	Conventional MemoryAccess Method	By Content	By Address
Search Speed	Very Fast	Slower
Comparison	Parallel	Sequential
Cost	High	Lower
Complexity	High	Low
Advantages Over Conventional Memory
Plain Text
1
Conventional Memory:
2
Address → Data
3
 
4
Associative Memory:
5
Data → Match → Location
Show more lines

Associative memory can locate data without knowing its address, making searches significantly faster.

Exam Point

Associative Memory (Content Addressable Memory - CAM) is a memory system that retrieves information by comparing the input data with all stored data simultaneously. It is accessed by content rather than address and is widely used in cache memories, TLBs, and networking applications for high-speed searches.

## Cache Memory
Cache Memory is a small, high-speed memory located between the CPU and Main Memory (RAM). It stores frequently used data and instructions so that the CPU can access them faster, thereby reducing memory access time and improving overall system performance.

Need for Cache Memory
CPU operates much faster than main memory.
Frequent memory access can slow down program execution.
Cache stores commonly used data and instructions.
Reduces the speed gap between CPU and RAM.
Basic Organization
Plain Text
1
CPU
2
│
3
▼
4
Cache Memory
5
│
6
▼
7
Main Memory
8
│
9
▼
10
Auxiliary Memory
Show more lines
Working of Cache Memory
Cache Hit

When the required data is found in the cache memory.

Plain Text
1
CPU → Cache → Data Found
Show more lines
Fast access
High performance
Cache Miss

When the required data is not found in cache memory.

Plain Text
1
CPU → Cache → Not Found
2
↓
3
Main Memory
Show more lines
Additional access time is required.
Characteristics of Cache Memory
Very high-speed memory.
Located between CPU and main memory.
Stores frequently used data and instructions.
Small storage capacity.
More expensive than RAM.
Usually implemented using SRAM (Static RAM).
Types of Cache Memory
L1 Cache (Level 1)
Located inside the CPU.
Smallest and fastest cache.
Very low access time.
L2 Cache (Level 2)
Larger than L1.
Slightly slower than L1.
May be inside or near the processor.
L3 Cache (Level 3)
Larger shared cache.
Shared among CPU cores.
Slower than L1 and L2 but faster than RAM.
Cache Mapping Techniques
1. Direct Mapping
Each block of main memory maps to exactly one cache location.
Simple implementation.
Fast access.
2. Associative Mapping
Any memory block can be placed in any cache location.
Flexible.
Higher hardware complexity.
3. Set Associative Mapping
Combination of direct and associative mapping.
Widely used in modern processors.
Advantages of Cache Memory
Reduces memory access time.
Improves CPU performance.
Increases execution speed.
Reduces CPU waiting time.
Improves overall system efficiency.
Disadvantages of Cache Memory
High cost.
Limited storage capacity.
Complex management mechanisms.
Cache Memory vs Main Memory
Feature	Cache Memory	Main MemorySpeed	Very Fast	Slower
Capacity	Small	Large
Cost	High	Lower
Technology	SRAM	DRAM
Location	Between CPU and RAM	Connected to CPU
Applications
Modern processors
Servers
Mobile devices
Embedded systems
High-performance computing
Example

Suppose a program repeatedly accesses:

Plain Text
1
A[0], A[1], A[2]
Show more lines

These values are loaded into cache memory. Future accesses are served directly from cache instead of RAM, resulting in faster execution.

Exam Point

Cache Memory is a small, high-speed memory located between the CPU and main memory. It stores frequently used data and instructions to reduce memory access time and improve processor performance.

## Virtual Memory
Virtual Memory is a memory management technique that allows a computer to execute programs larger than the available main memory (RAM) by using a portion of secondary storage (hard disk/SSD) as an extension of main memory.

It creates the illusion of a very large memory space for programs.

Need for Virtual Memory
RAM capacity is limited.
Large programs may not fit entirely into main memory.
Multiple programs can execute simultaneously.
Improves memory utilization.
Enables efficient multitasking.
Basic Concept
Plain Text
1
CPU
2
│
3
▼
4
Main Memory (RAM)
5
│
6
▼
7
Virtual Memory
8
(Disk/SSD Space)
Show more lines

The operating system transfers data between RAM and disk as required.

Working of Virtual Memory
A program is divided into pages.
Only the required pages are loaded into RAM.
Remaining pages stay on disk.
When a required page is not in RAM, a Page Fault occurs.
The operating system loads the required page from disk into RAM.
Example

Suppose:

Plain Text
1
Program Size = 8 GB
2
RAM Available = 4 GB
Show more lines

Virtual memory allows the 8 GB program to run by loading only the necessary portions into RAM.

Paging
Definition

Paging divides:

Virtual memory into Pages
Physical memory into Frames
Plain Text
1
Virtual Memory → Pages
2
Main Memory → Frames
Show more lines

Pages are loaded into available frames when needed.

Page Table

A Page Table maintains the mapping between:

Plain Text
1
Virtual Address → Physical Address
Show more lines

Example:

Page Number	Frame Number0	5
1	2
2	7
Page Fault
Definition

A page fault occurs when the CPU requests a page that is not currently loaded into RAM.

Steps
CPU requests a page.
Page not found in RAM.
Operating System loads the page from disk.
Execution continues.
Advantages of Virtual Memory
Allows execution of large programs.
Supports multitasking.
Better memory utilization.
Increases degree of multiprogramming.
Provides an illusion of larger memory.
Disadvantages of Virtual Memory
Slower than RAM access.
Page faults reduce performance.
Requires disk space.
Increased operating system overhead.
Virtual Memory vs Main Memory
Feature	Virtual Memory	Main MemoryLocation	Disk/SSD + RAM	RAM
Speed	Slower	Faster
Capacity	Very Large	Limited
Cost	Lower	Higher
Access Time	High	Low
Virtual Memory vs Cache Memory
Feature	Virtual Memory	Cache MemoryPurpose	Increase effective memory size	Increase access speed
Storage Medium	Disk/SSD	SRAM
Speed	Slow	Very Fast
Managed By	Operating System	Hardware/CPU
Applications
Multitasking operating systems
Large databases
Scientific computing
Virtual machines
Web browsers and modern applications
Exam Point

Virtual Memory is a memory management technique that uses secondary storage as an extension of main memory, allowing programs larger than available RAM to execute by loading required pages into memory on demand.

## Memory Management Hardware
Memory Management Hardware refers to the hardware mechanisms used by a computer system to manage memory efficiently, translate addresses, protect memory spaces, and support virtual memory.

It enables the CPU to generate logical addresses while the hardware converts them into physical memory addresses.

Need for Memory Management Hardware
Efficient utilization of memory.
Support for virtual memory.
Protection between user programs.
Relocation of programs in memory.
Sharing of memory among processes.
Faster address translation.
Basic Concept

When a program executes, it generates a:

Plain Text
1
Logical Address (Virtual Address)
2
 
Show more lines

The memory management hardware translates it into:

Plain Text
1
Physical Address
Show more lines
Plain Text
1
CPU
2
│
3
▼
4
Logical Address
5
│
6
▼
7
Memory Management Hardware
8
│
9
▼
10
Physical Address
11
│
12
▼
13
Main Memory
Show more lines
Components of Memory Management Hardware
1. Relocation Register (Base Register)
Contains the starting physical address of a program.
Added to the logical address generated by the CPU.
Example
Plain Text
1
Base Register = 1000
2
Logical Address = 250
Show more lines

Physical Address:

Plain Text
1
1000 + 250 = 1250
Show more lines
2. Limit Register
Stores the size of the process.
Ensures the process does not access memory outside its allocated space.
Example
Plain Text
1
Limit = 500
2
Logical Address = 600
Show more lines

Since:

Plain Text
1
600 > 500
2
 
Show more lines

An error (trap) is generated.

Address Translation

Physical Address is calculated as:

Plain Text
1
Physical Address =
2
Base Register + Logical Address
Show more lines
Example
Plain Text
1
Base Register = 4000
2
Logical Address = 200
Show more lines

Then:

Plain Text
1
Physical Address = 4200
Show more lines
Paging Hardware
Definition

Paging divides memory into:

Plain Text
1
Pages
2
Frames
Show more lines
Virtual Memory → Pages
Physical Memory → Frames

A page table maps pages to frames.

Address Structure
Plain Text
1
Logical Address
2
 
3
+-----------+------------+
4
| Page No. | Offset |
5
+-----------+------------+
Show more lines

The page number is used to access the page table.

Page Table

Example:

Page	Frame0	5
1	2
2	7

If:

Plain Text
1
Page = 1
2
Offset = 20
Show more lines

Frame:

Plain Text
1
2
Show more lines

Physical Address:

Plain Text
1
Frame 2 + Offset 20
Show more lines
Translation Lookaside Buffer (TLB)
Definition

A TLB is a small, high-speed associative memory used to store recently used page table entries.

Purpose
Speeds up address translation.
Reduces page table access time.
Operation
Plain Text
1
CPU
2
│
3
▼
4
TLB
5
│
6
├─ Hit → Physical Address
7
│
8
└─ Miss → Page Table → Physical Address
Show more lines
Advantages
Faster memory access.
Improved system performance.
Segmentation Hardware
Definition

Segmentation divides a program into logical units such as:

Code
Data
Stack
Logical Address
Plain Text
1
(segment number, offset)
Show more lines
Segment Table

Contains:

Base Address
Limit

Example:

Segment	Base	LimitCode	1000	500
Data	2000	300
Stack	3000	200
Memory Protection

Memory management hardware prevents unauthorized memory access.

Methods:

Base Register
Limit Register
Page Protection Bits
Segment Protection

This ensures one process cannot access another process's memory.

Advantages of Memory Management Hardware
Efficient memory utilization.
Faster address translation.
Supports virtual memory.
Provides memory protection.
Allows multiprogramming and multitasking.
Enables process relocation.
Applications
Operating Systems
Virtual Memory Systems
Multiprogramming Environments
Embedded Systems
Modern Computers and Servers
Exam Point

Memory Management Hardware consists of components such as the Base Register, Limit Register, Page Table, TLB, and Segmentation Hardware. It translates logical addresses into physical addresses, provides memory protection, and supports virtual memory for efficient system operation.