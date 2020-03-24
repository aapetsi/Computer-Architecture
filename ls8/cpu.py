"""CPU functionality."""

import sys
import os


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.registers = [0] * 8
        self.ram = [0] * 256
        self.halt = False
        self.pc = 0

    def load(self):
        """Load a program into memory."""
        # Get arguments from command line
        args = sys.argv

        if len(sys.argv) == 1:
            print('ERROR: PROVIDE A PROGRAM NAME')
            sys.exit(-1)

        file_name = os.getcwd() + f"/{args[1]}"
        
        test = [int(line.rstrip('\n')[:8], 2) for line in open(file_name)]
    
        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in test:
            self.ram[address] = instruction
            address += 1

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        HLT = 1
        PRN = 71
        LDI = 130
        MUL = 162

        inc = 0

        while not self.halt:
            
            command = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if command == HLT:
                self.halt = True
                sys.exit(-1)

            elif command == PRN:
                register_index = operand_a
                num = self.registers[register_index]
                print(num)
                inc = 2

            elif command == LDI:
                self.registers[operand_a] = operand_b
                inc = 3
            
            elif command == MUL:
                print('multiply')
                inc = 3

            else:
                print("Invalid instruction")
                self.halt = False

            self.pc += inc

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.registers[address] = value
        return self.ram[address]
