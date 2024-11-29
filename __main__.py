from .calculator.__main__ import main as calculator_loop
from .contacts.__main__ import main as contacts_loop


def loop():
    try:
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        match int(input()):
            case 1:
                pass
            case 2:
                pass
            case 3:
                contacts_loop()
            case 4:
                pass
            case 5:
                calculator_loop()
            case 6:
                return True
            case _:
                print("Не смог обработать твой выбор. Повтори попытку:")
                return False
    except ValueError:
        print("Не смог обработать твой выбор. Повтори попытку")
        return False
    except KeyboardInterrupt:
        return True


if __name__ == "__main__":
    end = False
    while not end:
        end = loop()
