class CalculatorError(Exception):
    pass


def calculate(expression):
    try:
        # Разбиваем строку на числа и оператор
        operators = ['+', '-', '*', '/']
        operator = None
        for op in operators:
            if op in expression:
                operator = op
                break

        if not operator:
            raise CalculatorError("throws Exception //т.к. строка не является математической операцией")

        num1, num2 = map(int, expression.split(operator))

        # Проверяем, что числа находятся в допустимом диапазоне от 1 до 10
        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            raise CalculatorError("Числа должны быть в диапазоне от 1 до 10")

        # Выполняем операцию в зависимости от оператора
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise CalculatorError("Деление на ноль не допускается")
            result = num1 // num2  # Целочисленное деление, отбрасываем остаток

        return str(result)

    except ValueError:
        raise CalculatorError("throws Exception //т.к. формат математической операции не удовлетворяет заданию")
    except CalculatorError as e:
        raise e


def main(input_str):
    try:
        result = calculate(input_str)
        return result
    except CalculatorError as e:
        return f"throws Exception: {e}"


# Пример использования
user_input = input("Введите арифметическое выражение (например, 2+2): ")
print(main(user_input))

