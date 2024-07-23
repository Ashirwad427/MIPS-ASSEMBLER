# MIPS-ASSEMBLER
A small python & assembly based project which converts MIPS assembly instructions into their corresponding machine code in both binary and hexadecimal formats.

### There are mainly two parts to this project:
#### 1. Bubble Sort algorithm using assembly language.
#### 2. Assembler for the above .asm file using Python.

### 1. Bubble Sort algorithm
This MIPS assembly program is designed to read a specified number of integers from the user, store them in memory, and then sort them using the bubble sort algorithm. After sorting, the program outputs the sorted integers. Here’s a breakdown of the program’s functionality:

Data Section:
Defines various strings used for displaying prompts and messages to the user.

Text Section:
Prompts the user to enter the number of integers, starting address of inputs, and starting address of outputs.
Reads these values from the terminal and stores them in registers $t1, $t2, and $t3 respectively.
Prompts the user to enter the integers to be sorted, which are stored in memory starting from the address in $t2.

Copying Inputs to Output Memory:
Copies the unsorted integers from the input memory location to the output memory location.

Bubble Sort Algorithm:
Implements the bubble sort algorithm to sort the integers stored in the output memory location.

Output Sorted Integers:
Reads the sorted integers from the output memory location and prints them to the terminal.

System Calls:
Uses MIPS system calls for reading integers, printing integers, and printing strings.

### 2. MIPS Assembler in Python
 Here's a detailed breakdown of the program's functionality:

Instruction and Register Mappings:

instruction_mapping defines the opcodes for various MIPS instructions.
register_mapping maps register names to their binary equivalents.
add defines the addresses for specific labels used in jump instructions.
Two's Complement Function:

The twosComplement function calculates the two's complement of a value, used for negative immediate values.
Instruction Assembly Function:

The assemble_instruction function takes a MIPS instruction as input, splits it into its components, and assembles it into machine code.
It handles different instruction formats (I-format, J-format, R-format, and pseudo-instructions) and converts operands into their binary equivalents.
For branching (beq) and immediate arithmetic instructions (addi), it calculates the immediate value considering the label addresses.
For load (lw) and store (sw) instructions, it formats the immediate and register values appropriately.
For the move pseudo-instruction, it assembles it as an add instruction with a zero source register.
For jump (j) and set-less-than (slt) instructions, it formats the machine code based on the provided opcode and operands.
Input File Reading and Label Counting:

The program reads the input .asm file containing MIPS assembly code.
It processes the file to count lines and map labels to their line numbers for correct immediate value calculation in branch instructions.
Assembly Process:

The program reads the relevant lines of the assembly file, processes each line to generate machine code, and writes the binary and hexadecimal representation of the machine code to an output file.
Output:

The assembled machine code is written to an output file (output.txt) and also printed to the console for verification.
In summary, this program automates the process of converting MIPS assembly instructions into machine-readable code, considering various instruction formats and handling immediate value calculations for branch instructions.
