# В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки
# и возвращает сумму с учетом скидки. Ваша задача - проверить этот метод с использованием библиотеки
# AssertJ. Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение
# ArithmeticException. Не забудьте написать тесты для проверки этого поведения

def calculate(first_value: float, second_value: float, operator: str):
    match operator:
        case '+':
            result = first_value + second_value
        case '-':
            result = first_value - second_value
        case '*':
            result = first_value * second_value
        case '/':
            if second_value != 0:
                result = first_value / second_value
            else:
                raise ArithmeticError("Деление на ноль запрещено!")
        case _:
            raise ValueError(f"Оператор '{operator}' не поддерживается!")
    return result


def calculate_discount(purchase_amount: float, discount_amount: int):
    if discount_amount < 0:
        raise ArithmeticError("Размер скидки не может быть отрицательным")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не может быть больше 100%")

    return purchase_amount - discount_amount * purchase_amount / 100

