from components.assembler import Assembler
from components.processor import Processor

def main():
    # Запрашиваем у пользователя размер массива
    size = int(input("Введите размер массива: "))
    values = []

    # Запрашиваем значения для каждого элемента массива
    for i in range(size):
        value = int(input(f"Введите значение для элемента {i + 1}: "))
        values.append(value)

    # Создаем экземпляр Assembler
    assembler = Assembler()
    

    # Генерируем ассемблерный код для загрузки значений в регистры и их суммирования
    for i, value in enumerate(values):
        assembler.load(i, value)  # Загружаем значение в регистр i

    # Сложение значений в регистрах
    for i in range(1, size):
        assembler.add(0, i)  # Сложение с результатом в регистре 0

    assembler.finish()  # Завершаем программу

    # Получаем сгенерированный ассемблерный код
    program = assembler.get_program()

    # Сохраняем сгенерированный код в текстовом файле в двоичном формате
    assembler.save_to_file("generated_program.txt")
    print("Сгенерированный код сохранен в 'generated_program.txt'.")

    # Создаем экземпляр Processor и загружаем программу
    processor = Processor()
    processor.load_program(program)

    # Выполняем программу
    processor.execute()

    # Выводим результат
    print(f"Сумма элементов массива: {processor.registers[0]}")
    
    # Выводим значения всех регистров после выполнения программы
    print("Значения регистров после выполнения программы:")
    for i, value in enumerate(processor.registers):
        print(f"Регистр {i}: {value}")

if __name__ == "__main__":
    main()