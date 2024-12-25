class Processor:
    def __init__(self):
        self.memory = [0] * 256  # Эмуляция памяти
        self.registers = [0] * 16  # Эмуляция 16 регистров
        self.pc = 0  # Программный счетчик

    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.memory[i] = instruction
    
    def execute(self):
        while self.pc < len(self.memory):
            instruction = self.memory[self.pc]
            if instruction == 0:  # Код завершения
                break
            self.execute_instruction(instruction)
            self.pc += 1

    def execute_instruction(self, instruction):
        op_code = (instruction >> 12) & 0xF  # Получаем код операции
        reg_a = (instruction >> 8) & 0xF  # Получаем первый регистр
        value = instruction & 0xFF  # Получаем значение или адрес

        if op_code == 1:  # Сложение
            self.registers[reg_a] += self.registers[value]
        elif op_code == 2:  # Загрузка
            self.registers[reg_a] = value
        elif op_code == 3:  # Сохранение
            self.memory[value] = self.registers[reg_a]
