# Input-Output Organization
## Peripheral Devices
Input-Output (I/O) Organization refers to the mechanism used to transfer data between the CPU, memory, and peripheral devices. It provides communication between the computer system and external devices.

Need for I/O Organization
Enables communication with external devices.
Transfers data between CPU and peripherals.
Handles speed differences between CPU and devices.
Improves system performance.
Supports user interaction.
Basic I/O Organization
Plain Text
1
Input Device
2
↓
3
Input Interface
4
↓
5
CPU
6
↓
7
Output Interface
8
↓
9
Output Device
Show more lines

Components:

CPU: Controls execution of instructions.
Memory: Stores data and programs.
Input Interface: Connects input devices to CPU.
Output Interface: Connects output devices to CPU.
Peripheral Devices: External devices used for input/output.
I/O Data Transfer Methods
1. Programmed I/O
CPU continuously checks device status.
CPU waits until device becomes ready.
Simple but wastes CPU time.
2. Interrupt-Driven I/O
Device sends an interrupt when ready.
CPU performs other tasks until interrupted.
Efficient CPU utilization.
3. Direct Memory Access (DMA)
Data transferred directly between memory and device.
CPU involvement is minimal.
Suitable for high-speed data transfer.
Peripheral Devices
Definition

Peripheral Devices are external hardware components connected to a computer for input, output, storage, or communication purposes.

They are not part of the CPU or main memory but help in system operation.

Classification of Peripheral Devices
1. Input Devices

Used to enter data into the computer.

Examples:

Keyboard
Mouse
Scanner
Microphone
Webcam
Barcode Reader
Touch Screen
Example
Plain Text
1
Keyboard → Input Data → CPU
Show more lines
2. Output Devices

Used to display or present processed information.

Examples:

Monitor
Printer
Plotter
Speakers
Projector
Example
Plain Text
1
CPU → Monitor → Display Output
Show more lines
3. Storage Devices

Used to store data and programs.

Examples:

Hard Disk Drive (HDD)
Solid State Drive (SSD)
Pen Drive
CD/DVD
Memory Card
4. Communication Devices

Used for data communication between systems.

Examples:

Modem
Network Interface Card (NIC)
Router
Switch
Wireless Adapter
Characteristics of Peripheral Devices
Operate at slower speeds than CPU.
Require I/O interfaces for communication.
Can be input, output, storage, or communication devices.
Expand system functionality.
I/O Interface

An I/O Interface acts as a bridge between CPU and peripheral devices.

Functions:

Data transfer.
Device communication.
Status monitoring.
Error handling.
Synchronization between CPU and devices.
Importance of Peripheral Devices
Allow user interaction.
Provide permanent data storage.
Enable communication and networking.
Support multimedia applications.
Increase system usability.
Advantages
Extend computer capabilities.
Improve productivity.
Facilitate communication.
Provide data storage.
Support real-time applications.
Applications
Banking systems
Hospitals
Educational institutions
Industries
Communication networks
E-commerce systems
Exam Point

Input-Output Organization is the mechanism that enables communication between the CPU, memory, and peripheral devices. Peripheral devices are external hardware components used for input, output, storage, and communication, such as keyboards, monitors, printers, disks, and network devices

## Input-Output Interface
An Input-Output (I/O) Interface is a hardware unit that acts as an intermediary between the CPU and peripheral devices. It enables communication and data transfer between devices operating at different speeds and formats.

Need for I/O Interface
CPU operates much faster than peripheral devices.
Different devices use different data formats.
Provides synchronization between CPU and I/O devices.
Reduces direct CPU involvement in device management.
Handles control and status information.
Block Diagram
Plain Text
1
Input Device
2
│
3
▼
4
+--------------+
5
| I/O Interface|
6
+--------------+
7
│
8
▼
9
CPU
10
│
11
▼
12
+--------------+
13
| I/O Interface|
14
+--------------+
15
│
16
▼
17
Output Device
Show more lines
Functions of I/O Interface
1. Data Buffering
Temporarily stores data during transfer.
Handles speed mismatch between CPU and peripheral devices.
2. Control and Timing
Generates control signals.
Coordinates communication between CPU and I/O devices.
3. Status Reporting
Indicates whether a device is ready, busy, or has encountered an error.
4. Data Conversion
Converts data formats when necessary.
Ensures compatibility between CPU and peripheral devices.
5. Error Detection
Detects communication and transmission errors.
Components of an I/O Interface
Data Register
Stores data being transferred between CPU and device.
Status Register

Contains device status information such as:

Plain Text
1
Ready
2
Busy
3
Error
4
Interrupt Request
Show more lines
Control Register

Stores commands sent by the CPU to control device operations.

Working of an I/O Interface
Input Operation
Plain Text
1
Input Device
2
↓
3
I/O Interface
4
↓
5
CPU
Show more lines

Steps:

Device sends data to the interface.
Interface stores data in the data register.
CPU reads data from the interface.
Status information is updated.
Output Operation
Plain Text
1
CPU
2
↓
3
I/O Interface
4
↓
5
Output Device
Show more lines

Steps:

CPU sends data to the interface.
Interface buffers the data.
Device receives the data.
Status register indicates completion.
Types of I/O Interfaces
Parallel Interface
Transfers multiple bits simultaneously.
High-speed communication.
Used for printers and high-speed devices.

Example:

Plain Text
1
Printer Interface
Show more lines
Serial Interface
Transfers one bit at a time.
Requires fewer communication lines.
Suitable for long-distance communication.

Examples:

Plain Text
1
USB
2
UART
3
RS-232
4
 
Show more lines
I/O Interface with Programmed I/O
Plain Text
1
CPU → Status Check → Device Ready?
2
↓
3
Yes
4
↓
5
Data Transfer
Show more lines
CPU continuously checks device status.
Simple but inefficient.
I/O Interface with Interrupts
Plain Text
1
CPU executes program
2
↓
3
Device Ready
4
↓
5
Interrupt Generated
6
↓
7
CPU Services Device
Show more lines
Better CPU utilization.
Device requests service when needed.
I/O Interface with DMA
Plain Text
1
Device ↔ DMA Controller ↔ Memory
2
↓
3
CPU
Show more lines
Direct data transfer between memory and device.
CPU involvement is minimal.
Suitable for large data transfers.
Advantages of I/O Interface
Simplifies communication between CPU and devices.
Handles speed mismatch.
Improves system efficiency.
Supports interrupts and DMA.
Provides error checking and control.
Applications
Keyboards
Printers
Disk drives
Mouse
Network devices
Industrial control systems
Embedded systems
Difference Between I/O Interface and Peripheral Device
I/O Interface	Peripheral DeviceActs as a bridge between CPU and device	External hardware connected to the computer
Handles control and data transfer	Provides input/output functionality
Contains registers and control logic	Performs actual user interaction
Example: USB Controller	Example: Keyboard, Printer
Exam Point

An Input-Output Interface is a hardware module that provides communication between the CPU and peripheral devices by handling data transfer, control signals, synchronization, and status monitoring. It contains data, status, and control registers and supports Programmed I/O, Interrupt-Driven I/O, and DMA operations.

## Asynchronous Data Transfer
Asynchronous Data Transfer is a method of transferring data between two devices that do not share a common clock signal. The transfer is controlled using control signals to ensure that data is transmitted and received correctly.

Unlike synchronous transfer, the sender and receiver operate independently and communicate through handshaking signals.

Need for Asynchronous Data Transfer
Different devices operate at different speeds.
A common clock may not be available.
Ensures reliable communication between CPU and peripheral devices.
Accommodates variable data transfer rates.
Basic Concept
Plain Text
1
Sender ─────► Receiver
2
│ │
3
Request Acknowledge
Show more lines

The sender informs the receiver when data is ready, and the receiver acknowledges after receiving it.

Methods of Asynchronous Data Transfer
1. Strobe Control Method

Data transfer is controlled using a strobe pulse.

Source-Initiated Strobe
Plain Text
1
Source → Data
2
Source → Strobe Signal
3
Destination receives data
Show more lines

Steps:

Source places data on the bus.
Source generates a strobe pulse.
Destination reads the data.
Destination-Initiated Strobe
Plain Text
1
Destination → Strobe
2
Source → Data
Show more lines

Steps:

Destination requests data using a strobe signal.
Source places data on the bus.
Destination reads the data.
Disadvantage
No confirmation that data has been received successfully.
2. Handshaking Method

Handshaking uses two control signals:

Request (REQ)
Acknowledge (ACK)

This method is more reliable than strobe control.

Handshaking Process
Plain Text
1
Sender Receiver
2
│ │
3
│---- Request -------------> │
4
│ │
5
│ <--- Acknowledge --------- │
6
│ │
Show more lines
Steps
Sender places data on the bus.
Sender activates Request signal.
Receiver reads data.
Receiver activates Acknowledge signal.
Sender removes data and request signal.
Receiver clears acknowledge signal.
Block Diagram
Plain Text
1
Data Bus
2
Sender <--------> Receiver
3
 
4
Request -------->
5
Acknowledge <------
Show more lines
Advantages of Handshaking
Reliable data transfer.
No common clock required.
Supports devices with different speeds.
Prevents data loss.
Disadvantages
Slower than synchronous transfer.
Requires additional control lines.
More complex control mechanism.
Synchronous vs Asynchronous Data Transfer
Feature	Synchronous	AsynchronousClock Signal	Required	Not Required
Speed	Higher	Lower
Control Signals	Minimal	Request/Acknowledge
Complexity	Lower	Higher
Reliability with Different Speeds	Moderate	High
Applications
CPU and I/O communication
Keyboard interfaces
Serial communication
UART communication
Network communication
Data exchange between devices with different operating speeds
Exam Point

Asynchronous Data Transfer is a method of data communication between two devices that do not share a common clock. It uses either Strobe Control or Handshaking techniques, with handshaking being more reliable because it uses Request and Acknowledge signals to ensure successful data transfer.

## Modes of Transfer
Modes of Transfer refer to the methods used for transferring data between the CPU, memory, and Input/Output (I/O) devices.

Because peripheral devices operate at different speeds than the CPU, special transfer methods are required for efficient communication.

Types of Data Transfer Modes
1. Programmed I/O (Polling)
Definition

In Programmed I/O, the CPU continuously checks the status of the I/O device until it becomes ready for data transfer.

Working
CPU sends a request to the device.
CPU repeatedly checks device status.
When the device is ready, data transfer occurs.
CPU resumes execution.
Diagram
Plain Text
1
CPU ⇄ I/O Interface ⇄ Peripheral Device
Show more lines
Advantages
Simple implementation.
Low hardware cost.
Disadvantages
CPU remains busy waiting.
Wastage of processor time.
Low efficiency.
Applications
Simple embedded systems.
Low-speed devices.
2. Interrupt-Initiated I/O (Interrupt-Driven I/O)
Definition

In Interrupt-Driven I/O, the device interrupts the CPU whenever it is ready for data transfer.

Working
CPU executes another program.
Device becomes ready.
Device sends an interrupt request.
CPU suspends current task.
Interrupt Service Routine (ISR) executes.
Data transfer takes place.
CPU resumes previous task.
Diagram
Plain Text
1
Device
2
│
3
Interrupt
4
▼
5
CPU
6
│
7
Transfer Data
8
▼
9
Memory
Show more lines
Advantages
Better CPU utilization.
No busy waiting.
Faster response.
Disadvantages
More complex than Programmed I/O.
Interrupt handling overhead.
Applications
Keyboards
Mouse
Communication devices
3. Direct Memory Access (DMA)
Definition

DMA is a mode of transfer in which data is transferred directly between memory and an I/O device without continuous CPU involvement.

Working
CPU initializes DMA transfer.
DMA Controller takes control of the bus.
Data transfers directly between memory and device.
DMA interrupts CPU after completion.
Diagram
Plain Text
1
┌─────────┐
2
│ CPU │
3
└────┬────┘
4
│
5
Initializes
6
│
7
▼
8
┌────────────────┐
9
│ DMA Controller │
10
└─────┬─────┬────┘
11
│ │
12
▼ ▼
13
Memory I/O Device
Show more lines
Advantages
High-speed data transfer.
Minimal CPU involvement.
Efficient for large data blocks.
Disadvantages
Additional hardware required.
More complex design.
Applications
Hard disks
SSDs
Network interfaces
Multimedia systems
Comparison of Transfer Modes
Feature	Programmed I/O	Interrupt I/O	DMACPU Involvement	Very High	Medium	Very Low
Transfer Speed	Low	Medium	High
Hardware Complexity	Low	Medium	High
CPU Utilization	Poor	Good	Excellent
Suitable For	Low-speed Devices	Medium-speed Devices	High-speed Devices
Exam Point

The three modes of data transfer are Programmed I/O, Interrupt-Initiated I/O, and Direct Memory Access (DMA). Among these, DMA provides the highest performance because data is transferred directly between memory and I/O devices with minimal CPU involvement.

## Priority Interrupt
A Priority Interrupt system is used when multiple interrupt requests occur simultaneously. It assigns a priority level to each interrupt source so that the CPU services the highest-priority interrupt first.

This ensures that important devices receive immediate attention.

Need for Priority Interrupt
Multiple devices may request CPU service at the same time.
Some devices are more critical than others.
Prevents loss of important data.
Improves system efficiency and response time.
Example

Consider the following devices:

Plain Text
1
Priority 1 → Disk Controller
2
Priority 2 → Network Card
3
Priority 3 → Keyboard
4
Priority 4 → Printer
5
 
Show more lines

If all devices generate interrupts simultaneously:

Plain Text
1
Disk Controller
Show more lines

will be serviced first because it has the highest priority.

Types of Priority Interrupt
1. Software Priority Interrupt

Priority is determined by software.

Working
CPU receives interrupt requests.
Interrupt Service Routine checks all requests.
Highest-priority request is selected.
Corresponding ISR is executed.
Advantages
Flexible implementation.
Easy to modify priorities.
Disadvantages
Slower than hardware priority.
Increased software overhead.
2. Hardware Priority Interrupt

Priority is determined using hardware circuits.

Advantages
Faster response.
Suitable for real-time systems.
Disadvantages
More hardware required.
Higher implementation cost.
Methods of Hardware Priority Interrupt
1. Daisy Chain Method

Devices are connected in series.

Plain Text
1
CPU
2
│
3
▼
4
Device 1
5
│
6
▼
7
Device 2
8
│
9
▼
10
Device 3
11
│
12
▼
13
Device 4
Show more lines
Working
Interrupt acknowledge signal travels through devices.
The first device requesting service captures the signal.
Devices closer to CPU have higher priority.
Advantages
Simple implementation.
Low hardware cost.
Disadvantages
Fixed priority.
Failure of one device may affect others.
2. Parallel Priority Interrupt

Uses priority encoder hardware.

Plain Text
1
Interrupt Requests
2
↓
3
Priority Encoder
4
↓
5
CPU
Show more lines
Working
All interrupt requests are examined simultaneously.
Priority encoder selects the highest-priority request.
CPU services the selected device.
Advantages
Faster than daisy chain.
Simultaneous interrupt handling.
Disadvantages
More hardware complexity.
Interrupt Priority Levels

Example:

Device	PriorityDisk Controller	Highest
Network Interface	High
Keyboard	Medium
Printer	Low

If all interrupt simultaneously:

Plain Text
1
Disk Controller
2
↓
3
Network Interface
4
↓
5
Keyboard
6
↓
7
Printer
Show more lines

will be serviced in that order.

Priority Interrupt Sequence
Device generates interrupt request.
CPU receives requests.
Priority logic determines highest priority.
CPU acknowledges selected interrupt.
Corresponding ISR executes.
CPU returns to interrupted program.
Advantages
Fast response to critical devices.
Prevents data loss.
Efficient CPU utilization.
Supports multiple interrupt sources.
Suitable for real-time systems.
Disadvantages
Additional hardware/software complexity.
Low-priority devices may experience starvation.
Implementation cost may increase.
Applications
Operating Systems
Real-Time Systems
Network Controllers
Disk Controllers
Embedded Systems
Communication Systems
Daisy Chain vs Parallel Priority Interrupt
Feature	Daisy Chain	Parallel PrioritySpeed	Lower	Higher
Cost	Lower	Higher
Hardware Complexity	Simple	Complex
Priority Assignment	Fixed	Flexible
Reliability	Lower	Higher
Exam Point

Priority Interrupt is a mechanism used to determine which interrupt should be serviced first when multiple interrupt requests occur simultaneously. Priority can be implemented using software or hardware methods such as Daisy Chaining and Parallel Priority Interrupt systems.

## DMA
Direct Memory Access (DMA) is a technique that allows data to be transferred directly between an I/O device and main memory without continuous involvement of the CPU.

DMA improves system performance by reducing CPU workload during large data transfers.

Need for DMA
CPU is much faster than I/O devices.
Continuous CPU involvement wastes processing time.
Large volumes of data need efficient transfer.
Improves overall system throughput.
Basic Concept

Without DMA:

Plain Text
1
I/O Device ↔ CPU ↔ Memory
Show more lines

With DMA:

Plain Text
1
I/O Device ↔ DMA Controller ↔ Memory
Show more lines

The CPU only initiates the transfer, and the DMA controller handles the rest.

DMA Controller

A DMA Controller is a hardware unit responsible for managing data transfer between memory and I/O devices.

Functions
Generates memory addresses.
Controls data transfer.
Maintains transfer count.
Requests bus access.
Sends completion interrupt to CPU.
Working of DMA
Step 1

CPU initializes the DMA controller by providing:

Starting memory address
Number of bytes/words to transfer
Direction of transfer
Step 2

DMA controller requests control of the system bus.

Step 3

CPU grants bus access.

Step 4

DMA transfers data directly between memory and I/O device.

Step 5

After transfer completion, DMA sends an interrupt to the CPU.

DMA Transfer Process
Plain Text
1
CPU
2
│
3
│ Initialize DMA
4
▼
5
DMA Controller
6
│
7
├── Memory
8
│
9
└── I/O Device
Show more lines
DMA Transfer Modes
1. Burst Mode (Block Transfer)
DMA transfers an entire block of data at once.
CPU remains idle during transfer.

Advantage:

Fastest transfer rate.
2. Cycle Stealing Mode
DMA transfers one word at a time.
Temporarily takes control of the bus from CPU.

Advantage:

CPU can continue executing between transfers.
3. Transparent Mode
DMA transfers data only when CPU is not using the bus.

Advantage:

Minimal impact on CPU performance.
Advantages of DMA
High-speed data transfer.
Reduced CPU workload.
Improved system efficiency.
Better CPU utilization.
Suitable for large data transfers.
Disadvantages of DMA
Requires additional hardware.
More complex design.
Bus contention may occur.
Applications of DMA
Hard Disk Drives (HDD)
SSDs
Network Interface Cards (NIC)
Graphics Cards
Audio Devices
Multimedia Systems
Programmed I/O vs Interrupt I/O vs DMA
Feature	Programmed I/O	Interrupt I/O	DMACPU Involvement	High	Medium	Very Low
Speed	Low	Medium	High
CPU Utilization	Poor	Better	Excellent
Hardware Complexity	Low	Medium	High
Exam Point

DMA (Direct Memory Access) is a data transfer technique in which data is transferred directly between memory and an I/O device through a DMA controller, with minimal CPU involvement. It provides high-speed data transfer and improves system performance.

## Serial Communication
Serial Communication is a method of data transmission in which data bits are sent one bit at a time over a single communication line or channel.

It is widely used for communication between computers, microprocessors, microcontrollers, and peripheral devices.

Need for Serial Communication
Reduces the number of communication lines.
Suitable for long-distance data transmission.
Lower cost compared to parallel communication.
Simplifies wiring and hardware design.
Basic Concept
Serial Transmission
Plain Text
1
Data = 10110011
2
 
3
Transmission:
4
 
5
1 → 0 → 1 → 1 → 0 → 0 → 1 → 1
6
``
Show more lines

Bits are transmitted sequentially, one after another.

Block Diagram
Plain Text
1
Sender
2
│
3
▼
4
Serial Interface
5
│
6
Communication Line
7
│
8
Serial Interface
9
▼
10
Receiver
Show more lines
Types of Serial Communication
1. Asynchronous Serial Communication
Definition

Data is transmitted one character at a time without a common clock signal.

Each character contains:

Start Bit
Data Bits
Optional Parity Bit
Stop Bit
Format
Plain Text
1
| Start | Data Bits | Parity | Stop |
Show more lines

Example:

Plain Text
1
| 0 | 10101010 | 1 | 1 |
Show more lines
Advantages
Simple implementation.
Low cost.
No clock synchronization required.
Disadvantages
Lower speed.
Additional start and stop bits increase overhead.
Examples
UART
RS-232
2. Synchronous Serial Communication
Definition

Sender and receiver share a common clock signal.

Format
Plain Text
1
Clock → Synchronizes transmission
2
Data → Sent continuously
Show more lines
Advantages
Higher speed.
More efficient transmission.
Less overhead.
Disadvantages
More complex hardware.
Clock synchronization required.
Examples
SPI
I²C
Modes of Serial Communication
Simplex

Communication in only one direction.

Plain Text
1
Sender → Receiver
Show more lines

Example: Keyboard to CPU

Half-Duplex

Communication in both directions, but not simultaneously.

Plain Text
1
Sender ↔ Receiver
Show more lines

Example: Walkie-talkie

Full-Duplex

Communication in both directions simultaneously.

Plain Text
1
Sender ⇄ Receiver
Show more lines

Example: Telephone communication

Serial vs Parallel Communication
Feature	Serial Communication	Parallel CommunicationData Transfer	One bit at a time	Multiple bits simultaneously
Number of Lines	One/Few	Multiple
Cost	Low	High
Distance	Long Distance	Short Distance
Wiring Complexity	Simple	Complex
Speed (Short Distance)	Lower	Higher
Common Serial Communication Standards
UART (Universal Asynchronous Receiver Transmitter)
Asynchronous communication.
No shared clock signal.
Widely used in microcontrollers.
RS-232
Standard serial communication interface.
Used in modems and industrial equipment.
SPI (Serial Peripheral Interface)
Synchronous communication.
High-speed communication between devices.
I²C (Inter-Integrated Circuit)
Two-wire serial communication protocol.
Used for communication between integrated circuits.
Advantages of Serial Communication
Requires fewer wires.
Lower installation cost.
Reliable over long distances.
Easy hardware implementation.
Suitable for networking and embedded systems.
Disadvantages of Serial Communication
Lower data transfer rate compared to parallel communication for short distances.
Data is transmitted sequentially.
Communication delay may occur at low speeds.
Applications
Computers and peripherals
Microcontrollers
Embedded systems
Industrial automation
Networking devices
Mobile devices
Communication systems
Exam Point

Serial Communication is a method of data transmission in which bits are transmitted one at a time over a communication channel. It can be synchronous or asynchronous and is preferred for long-distance communication because it requires fewer wires and offers greater reliability.