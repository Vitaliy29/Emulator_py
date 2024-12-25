class Assembler:
    def __init__(self):
        self.program = []

    def load(self, reg, value):
        """Загружает значение в указанный регистр."""
        self.program.append((2 << 12) | (reg << 8) | value)  # 2 - код операции LOAD

    def add(self, reg1, reg2):
        """Складывает значения из двух регистров и сохраняет результат в первом регистре."""
        self.program.append((1 << 12) | (reg1 << 8) | reg2)  # 1 - код операции ADD

    def multiply(self, reg1, reg2):
        """Умножает значения из двух регистров и сохраняет результат в первом регистре."""
        self.program.append((3 << 12) | (reg1 << 8) | reg2)  # 3 - код операции MULTIPLY

    def max(self, reg1, reg2):
        """Находит максимум между значениями в двух регистрах и сохраняет результат в первом регистре."""
        self.program.append((4 << 12) | (reg1 << 8) | reg2)  # 4 - код операции MAX

    def min(self, reg1, reg2):
        """Находит минимум между значениями в двух регистрах и сохраняет результат в первом регистре."""
        self.program.append((5 << 12) | (reg1 << 8) | reg2)  # 5 - код операции MIN

    def store(self, reg, address):
        """Сохраняет значение из указанного регистра в указанной ячейке памяти."""
        self.program.append((3 << 12) | (reg << 8) | address)  # 3 - код операции STORE

    def finish(self):
        """Завершает выполнение программы."""
        self.program.append(0)  # Код завершения

    def get_program(self):
        """Возвращает сгенерированный ассемблерный код."""
        return self.program

    def save_to_file(self, filename):
        """Сохраняет сгенерированный ассемблерный код в текстовый файл."""
        with open(filename, 'w') as f:
            for instruction in self.program:
                f.write(f"{instruction}\n")  # Записываем каждую инструкцию в файл
