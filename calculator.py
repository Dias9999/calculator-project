def calculate():
    """Простой консольный калькулятор, который поддерживает основные операции и работает в цикле."""
    while True:
        try:
            # Запрос чисел у пользователя
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            # Запрос операции
            operation = input("Выберите операцию (+, -, *, /) или введите 'exit' для выхода: ")

            # Обработка выхода
            if operation.lower() == 'exit':
                print("Программа завершена.")
                break

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
            else:
                print("Ошибка: некорректная операция. Попробуйте снова.")
                continue

            # Вывод результата
            print(f"Результат: {num1} {operation} {num2} = {result}")
        
        except ValueError:
            print("Ошибка: введены некорректные данные. Пожалуйста, вводите только числа.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

# Запуск функции калькулятора
calculate() 