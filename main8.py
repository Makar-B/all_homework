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
            a = self.__convert_to_number(a)
            b = self.__convert_to_number(b)

            addition = lambda x, y: x + y
            subtraction = lambda x, y: x - y
            multiplication = lambda x, y: x * y
            division = self.__safe_divide

            operations = {
                "+": addition,
                "-": subtraction,
                "*": multiplication,
                "/": division
            }

            if operation not in operations:
                raise ValueError(f"Операція '{operation}' не підтримується.")

            result = operations[operation](a, b)
            return result
        except Exception as e:
            logging.error(f"Помилка виконання операції: {e}")
            return None

    def __safe_divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            return a / b
        except ZeroDivisionError as e:
            logging.error(e)
            raise

    def __convert_to_number(self, value):
        try:
            if isinstance(value, (int, float)):
                return value
            return float(value)
        except ValueError:
            logging.error(f"Неможливо конвертувати '{value}' до int або float.")
            raise

if __name__ == "__main__":
    calc = Calculation()

    print(calc(10, 5, "+"))
    print(calc(10, 5, "-"))
    print(calc(10, 5, "*"))
    print(calc(10, 5, "/"))

    print(calc(10, 0, "/"))
    print(calc("10a", 5, "+"))
    print(calc(10, 5, "^"))
