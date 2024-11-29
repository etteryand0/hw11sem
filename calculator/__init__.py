class Calculator:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            print("Деление на ноль невозможно")
            return
        return a / b
