class Processor:
    def __init__(self):
        self.registers = [0] * 8  # 8 регистров

    def load_program(self, program):
        self.program = program

    def execute(self):
        for instruction in self.program:
            opcode = (instruction >> 12) & 0xF
            reg1 = (instruction >> 8) & 0xF
            reg2 = instruction & 0xFF
            
            if opcode == 0b0001:  # LOAD
                self.registers[reg1] = reg2
            elif opcode == 0b0010:  # ADD
                self.registers[reg1] += self.registers[reg2]
            elif opcode == 0b1111:  # HALT
                break