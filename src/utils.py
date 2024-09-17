def selection_condition(
    question: str,
    answer_one: str,
    answer_two: str,
    answer_three: str = "",
    answer_four: str = "",
    answer_five: str = "",
) -> str:
    """
    Функция логики выбора
    :param question: Условие
    :param answer_one: Первый ответ
    :param answer_two: Второй ответ
    :param answer_three: Третий ответ
    :param answer_four: Четвертый ответ
    :param answer_five: Пятый ответ
    :return: Один из ответов
    """
    while True:
        string = (input(f"{question}:\n")).lower()
        if string in [answer_one.lower()]:
            return "1"
        elif string in [answer_two.lower()]:
            return "2"
        elif string in [answer_three.lower()]:
            return "3"
        elif string in [answer_four.lower()]:
            return "4"
        elif string in [answer_five.lower()]:
            return "5"
        elif string in ["0"]:
            return "exit"


def tuple_value_filtering(input_tuple_text: str) -> tuple:
    """
    Функция для отсеивания значений кортежа
    :param input_tuple_text: Строка формата 1, 1
    :return: кортеж с приведенными данными
    """
    try:
        value = tuple(map(int, input_tuple_text.split(",")))
        if value[0] < 0 or value[1] < 0 or value[0] == value[1]:
            raise ValueError
        elif value[0] < value[1]:
            value_1 = value[0]
            value_2 = value[1]
            return value_1, value_2
        elif value[0] > value[1]:
            value_1 = value[1]
            value_2 = value[0]
            return value_1, value_2
    except IndexError:
        print("номера страниц для поска не выбраны")
        value_1 = None
        value_2 = None
        return value_1, value_2
    except ValueError:
        print("номера страниц для поска не выбраны")
        value_1 = None
        value_2 = None
        return value_1, value_2
