from . import HELLO_TEXT


def loop():
    try:
        print(HELLO_TEXT)
        match int(input()):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
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
