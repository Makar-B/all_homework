import logging


logging.basicConfig(
    filename="calculation_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

class Calculation:
    def __init__(self):
        pass

    def __call__(self, a, b, operation):
        try:
            a = self.convert_to_number(a)
            b = self.convert_to_number(b)
            if operation == "+":
                return a + b
            elif operation == "-":
                return a - b
            elif operation == "*":
                return a * b
            elif operation == "/":
                if b == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе.")
                return a / b
            else:
                raise ValueError(f"Операція '{operation}' не підтримується.")
        except Exception as e:
            logging.error(f"Помилка виконання операції: {e}")
            return None

    def convert_to_number(self, value):
        try:
            if isinstance(value, (int, float)):
                return value
            return float(value)
        except ValueError:
            logging.error(f"Неможливо конвертувати '{value}' до int або float.")
            raise


if __name__ == "__main__":
    calc = Calculation()


    print(calc(10, 5, "+"))  # 15
    print(calc(10, 5, "-"))  # 5
    print(calc(10, 5, "*"))  # 50
    print(calc(10, 5, "/"))  # 2.0


    print(calc(10, 0, "/"))
    print(calc("10a", 5, "+"))
    print(calc(10, 5, "^"))
