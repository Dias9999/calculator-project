import math

def calculate():
    """Простой консольный калькулятор, который поддерживает основные операции и работает в цикле."""
    memory = None  # переменная для хранения предыдущего результата
    while True:
        try:
            # Запрос операции
            operation = input("Выберите операцию (+, -, *, /, **, sqrt) или введите 'exit' для выхода, 'M' для использования памяти: ")

            # Обработка выхода
            if operation.lower() == 'exit':
                print("Программа завершена.")
                break

            # Для sqrt требуется только одно число
            if operation == 'sqrt':
                num = input("Введите число для извлечения квадратного корня (или 'M' для использования памяти): ")
                if num == 'M':
                    if memory is None:
                        print("Память пуста.")
                        continue
                    num = memory
                else:
                    num = float(num)
                if num < 0:
                    print("Ошибка: нельзя извлекать корень из отрицательного числа.")
                    continue
                result = math.sqrt(num)
                print(f"Результат: sqrt({num}) = {result}")
                memory = result
                continue

            # Для остальных операций — два числа
            num1 = input("Введите первое число (или 'M' для использования памяти): ")
            if num1 == 'M':
                if memory is None:
                    print("Память пуста.")
                    continue
                num1 = memory
            else:
                num1 = float(num1)
            num2 = input("Введите второе число (или 'M' для использования памяти): ")
            if num2 == 'M':
                if memory is None:
                    print("Память пуста.")
                    continue
                num2 = memory
            else:
                num2 = float(num2)

            # Выполнение операции и обработка ошибок
            result = None
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль невозможно.")
                    continue  # Возврат к началу цикла
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            else:
                print("Ошибка: некорректная операция. Попробуйте снова.")
                continue

            # Вывод результата
            print(f"Результат: {num1} {operation} {num2} = {result}")
            memory = result
        
        except ValueError:
            print("Ошибка: введены некорректные данные. Пожалуйста, вводите только числа.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

# Запуск функции калькулятора
calculate()