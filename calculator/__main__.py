from . import Calculator


def main():
    calc = Calculator()

    while True:
        print("\nКалькулятор:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Некорректный ввод. Пожалуйста, выберите номер операции от 1 до 5.")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == "1":
                result = calc.add(num1, num2)
                print(f"Результат: {num1} + {num2} = {result}")
            elif choice == "2":
                result = calc.subtract(num1, num2)
                print(f"Результат: {num1} - {num2} = {result}")
            elif choice == "3":
                result = calc.multiply(num1, num2)
                print(f"Результат: {num1} * {num2} = {result}")
            elif choice == "4":
                result = calc.divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
        except Exception as e:
            print("Произошла ошибка:", e)


if __name__ == "__main__":
    main()
