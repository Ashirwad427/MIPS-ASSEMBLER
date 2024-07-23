import re
import binascii
# Define MIPS instruction mappings
instruction_mapping = {
    "addi": {"opcode": "001000"},
    "beq": {"opcode": "000100"},
    "lw": {"opcode": "100011"},
    "sw": {"opcode": "101011"},
    "move":{"opcode": "000000"},
    "j":{"opcode":"000010"},
    "slt":{"opcode":"000000"},
}

# Define register mappings
register_mapping = {
    "$zero": "00000",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$t8": "11000",
    "$t9": "11001",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
}
#Define addresses of mips instructions
add={
    "copy_loop":"1048598",
    "inner_loop":"1048613",
    "outer_loop":"1048608"
}

def twosComplement (value, bitLength) :
    return bin(value & (2**bitLength - 1))

def assemble_instruction(instruction):
    parts_temp=re.split(" |,|\t",instruction)
    parts=[]
    for i in range(len(parts_temp)):
        if parts_temp[i]!="" and parts_temp[i]!="0":
            parts.append(parts_temp[i])

    # Ignore comments and empty lines
    if not parts or parts[0].startswith("#") or len(parts)==1:
        return None
    func=parts[0]
    print("Instruction : ",end="")
    print(*parts)
    if func in ("beq"):
        opcode = instruction_mapping[func]["opcode"]
        # jal and beq instructions have different formats
        rs = register_mapping[parts[1]]
        rt = register_mapping[parts[2]]
        c=0
        next=line_count[tuple(parts[0:4])]
        target=line_count[parts[3]]
        for i in line_count.keys():
            if ( isinstance(i,str)==True and line_count[i]>next and line_count[i]<target):
                c+=1
        immediate=target-next-1-c
        address = format(immediate, '016b')  # Convert the immediate value to binary
        machine_code = opcode + rs + rt + address
        return machine_code
    elif func in ("add","addi"):
        # Instructions with I-format
        opcode = instruction_mapping["addi"]["opcode"]
        rt = register_mapping[parts[1]]
        rs = register_mapping[parts[2]]
        if(int(parts[3])<0):
            imm=twosComplement(int(parts[3]),16)
            imm2=str(imm)
            immediate=format(int(imm2,2), '016b')
        else:
            immediate = format(int(parts[3]), '016b')  # Convert the immediate value to binary
        machine_code = opcode + rs + rt + immediate
        return machine_code
    elif func in ("lw","sw"):
        opcode=instruction_mapping[func]["opcode"]
        rs=register_mapping[parts[2][2:5]]
        rt=register_mapping[parts[1]]
        immediate = format(int(parts[2][0]),'016b')
        machine_code=opcode + rs + rt + immediate
        return machine_code
    elif func == "move":
        # Pseudo-instruction "move" (Copy the value of one register to another)
        opcode = instruction_mapping[func]["opcode"]
        rd = register_mapping[parts[1]]
        rt = register_mapping[parts[2]]
        funct = "100001"  # "move" is essentially an "add" with rd = rs
        machine_code = "000000" + "00000" + rt + rd + "00000" + funct
        return machine_code
    elif func =="j" :
        opcode = instruction_mapping[func]["opcode"]
        immediate = format(int(add[parts[1]]),'026b')  # Convert the immediate value to binary
        machine_code = opcode + immediate
        return machine_code
    elif func =="slt":
        opcode=instruction_mapping[func]["opcode"]
        rd=register_mapping[parts[1]]
        rs=register_mapping[parts[2]]
        rt=register_mapping[parts[3]]
        funct="101010"
        machine_code=opcode+rs+rt+rd+"00000"+funct
        return machine_code
    # Add more cases for other instructions here...

    return None

# Input and output file paths
# input_file_path = "C:\Users\Lenovo\OneDrive\Desktop\CA_assign\IMT2022108_IMT2022122_Assignment1.asm"
# output_file_path = "C:\Users\Lenovo\OneDrive\Desktop\CA_assign\output.txt"

# Read the input .asm file

line_count={}

with open(r"C:\Users\Lenovo\OneDrive\Desktop\CA_assign\MIPS ASSEMBLER\IMT2022108_IMT2022122_Assignment1.asm", "r") as input_file_1:
    lines = input_file_1.readlines()
    lines_func=lines[46:105]
    c=1
    for i in range(len(lines_func)):
        lines_func[i]=lines_func[i].strip()
        parts_temp=re.split(" |,|\t",lines_func[i])
        parts=[]
        for i in range(len(parts_temp)):
            if parts_temp[i]!="" and parts_temp[i]!="0":
                parts.append(parts_temp[i])
        if len(parts)>0 and ":" in parts[0] and not parts[0].startswith("#"):
            parts[0]=parts[0][:len(parts[0])-1]
            line_count[parts[0]]=c
        elif len(parts)>0 and parts[0]=="beq":
            line_count[tuple(parts[0:4])]=c
        elif(len(parts)==0 or parts[0].startswith("#")):
            c-=1
        c+=1




with open(r"C:\Users\Lenovo\OneDrive\Desktop\CA_assign\MIPS ASSEMBLER\IMT2022108_IMT2022122_Assignment1.asm", "r") as input_file:
    lines = input_file.readlines()
    lines_func=lines[46:105]


# Open the output file for writing
with open(r"C:\Users\Lenovo\OneDrive\Desktop\CA_assign\MIPS ASSEMBLER\output.txt", "w") as output_file:
    for l in range(len(lines_func)):
        # Strip leading and trailing whitespace
        lines_func[l] = lines_func[l].strip()
        line=lines_func[l]
        # Assemble the instruction and write the machine code to the output file
        machine_code = assemble_instruction(line)

        if machine_code:
            hexa=hex(int(machine_code,2))[2:].zfill(8)
            print("Machine code : Bin - ",machine_code,"         Hex - ",hexa)
            print()
            output_file.write("Machine code : Bin - 0b"+ machine_code + "         Hex - 0x" + str(hexa)+"\n")

print("Assembly completed.")
