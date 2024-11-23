class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def str_to_float(value):
        try:
            return float(value)
        except ValueError:
            print(f"Помилка: неможливо конвертувати '{value}' в число типу float.")
            return None
        finally:
            print("Виконано спробу конвертації.")

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Помилка: ділення на нуль неможливе.")
            return None
        finally:
            print("Виконано спробу ділення.")

if __name__ == "__main__":
    calc = Calculator()
    num1 = calc.str_to_float("10.5")
    num2 = calc.str_to_float("not_a_number")
    if num1 is not None:
        print(calc.add(num1, 5))
        print(calc.subtract(num1, 3))
        print(calc.multiply(num1, 2))
        print(calc.divide(num1, 0))
