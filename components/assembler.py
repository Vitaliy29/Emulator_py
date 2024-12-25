class Assembler:
    def __init__(self):
        self.instructions = []

    def load(self, reg, value):
        # Пример инструкции в двоичном формате
        instruction = (0b0001 << 12) | (reg << 8) | (value & 0xFF)  # LOAD
        self.instructions.append(instruction)

    def add(self, reg1, reg2):
        # Пример инструкции сложения в двоичном формате
        instruction = (0b0010 << 12) | (reg1 << 8) | (reg2 & 0xFF)  # ADD
        self.instructions.append(instruction)

    def finish(self):
        # Завершение программы (можно добавить инструкцию завершения)
        self.instructions.append(0b1111)  # HALT

    def get_program(self):
        return self.instructions

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for instruction in self.instructions:
                # Преобразуем каждую инструкцию в двоичный формат и записываем в файл
                binary_instruction = format(instruction, '016b')  # 16-битное двоичное представление
                f.write(binary_instruction + '\n')  # Записываем каждую инструкцию на новой строке