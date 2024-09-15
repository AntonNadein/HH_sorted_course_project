import os

from src.class_get_API import HeadHunterAPI
from src.class_sorting_vacancy import SortingVacancyHeadHunter
from src.save_to_file import SaveToJson
from src.utils import selection_condition, tuple_value_filtering


def user_interaction():
    """Функция взаимодествия с пользователем"""
    global json_file
    while True:
        print("--- " * 10)
        print("ДЛЯ ВЫХОДА ВВЕДИТЕ: 0")
        search = input("Введите запрос для поиска: ")
        # условие выхода из цикла
        if search == "0":
            print("Спасибо что воспользовались нашими услугами!")
            break
        # проверка кода города
        city_key = input("Код города для запроса поиска: ")
        if city_key.isdigit() and int(city_key) > 0:
            city_key = int(city_key)
        else:
            city_key = None
        # проверка вывода количества вакансий
        text_condition = ("\nВведите номера страниц для поска вакансий через запятую"
                          "\nФОРМАТ ВВОДА: число1, число2"
                          "\nили нажмите Enter для пропуска\n")
        page_1, page_2 = tuple_value_filtering(input(text_condition))
        # запрос с hh.ru и его обрабоботка
        hh_api = HeadHunterAPI(search, city_key, page_1, page_2)
        vacancy_list = hh_api.get_vacancies
        vacancy = SortingVacancyHeadHunter.cast_to_object_list(vacancy_list)
        print("--- " * 10)

        while True:
            print("ДЛЯ ВОЗВРАЩЕНИЯ В ПРЕДЫДУЩИЙ ПУНКТ ВВЕДИТЕ: 0")
            question = ("Введитте:\n 1 Работа с файлами"
                        "\n 2 Работа с данными")
            answer = selection_condition(question, "1", "2")
            print("--- " * 10)
            if answer == "1":
                # работа с файлами
                print("0 ДЛЯ ВОЗВРАЩЕНИЯ В ПРЕДЫДУЩИЙ ПУНКТ МЕНЮ")
                file_name = input("\nВведите имя файла с которым предстоит работать "
                                  "\nили нажмите Enter для работы со стандартным файлом"
                                  "\nИмя файла: ")
                if file_name not in "":
                    json_file = f"{file_name}.json"
                    path_file = os.path.join(os.path.dirname(__file__), "data", json_file)
                    if not os.path.exists(path_file):
                        save = SaveToJson(file_name, vacancy)
                        save.del_vacancies()
                elif file_name == "0":
                    break
                else:
                    file_name = None
                while True:
                    save = SaveToJson(file_name, vacancy)
                    question = ("Введитте:\n 1 ПЕРЕЗАПИСАТЬ ДАННЫЕ В ФАЙЛЕ"
                                "\n 2 ДОБАВИТЬ ВАКАНСИИ В СУЩЕСТВУЮЩИЙ ФАЙЛ"
                                "\n 3 УДАЛИТЬ ДАННЫЕ ИЗ ФАЙЛА"
                                "\n 4 КОНВЕРТИРОВАТЬ ИЗ ФАЙЛА ОБЪЕКТЫ"
                                "\n 0 ДЛЯ ВОЗВРАЩЕНИЯ В ПРЕДЫДУЩИЙ ПУНКТ МЕНЮ")
                    answer = selection_condition(question, "1", "2", "3", "4")
                    if answer == "1":
                        # добавление вакансий
                        save.save_to_new_file()
                    elif answer == "2":
                        # объединение данных
                        save.add_unique_vacancy_to_file()
                    elif answer == "3":
                        # удаление данных
                        save.del_vacancies()
                    elif answer == "4":
                        # конвертация в SortingVacancyHeadHunter
                        vacancy_json = save.open_json_file_for_class()
                        vacancy = SortingVacancyHeadHunter.cast_to_object_list(vacancy_json)
                    elif answer == "exit":
                        break
                print("--- " * 10)
            elif answer == "2":
                # работа с данными
                while True:
                    print(f"Всего вакансий в перечне: {len(vacancy)}")
                    question = ("Введитте:\n 1 ВЫВЕСТИ В КОНСОЛЬ ВСЕ ВАКАНСИИ"
                                "\n 2 ОТСОРТИРОВАТЬ ВАКАНСИИ ПО ВОЗРАСТАНИЮ ЗАРПЛАТЫ"
                                "\n 3 ОТСОРТИРОВАТЬ ВАКАНСИИ ПО УБЫВАНИЮ ЗАРПЛАТЫ"
                                "\n 4 ОТСЕЯТЬ ВАКАНСИИ НИЖЕ ОПРЕДЕЛЕННОЙ ЗАРПЛАТЫ"
                                "\n 5 ВЫВЕСТИ ТОП N ВАКАНСИЙ ПО ЗАРПЛАТЕ"
                                "\n 0 ДЛЯ ВОЗВРАЩЕНИЯ В ПРЕДЫДУЩИЙ ПУНКТ МЕНЮ")
                    answer = selection_condition(question, "1", "2", "3", "4", "5")
                    if answer == "1":
                        # вывод в консоль
                        if vacancy == []:
                            print("Список вакансий пустой")
                        else:
                            for i in vacancy:
                                print(i)
                    elif answer == "2":
                        # сортировка вверх
                        vacancy = SortingVacancyHeadHunter.sorting_vacancy_to_salary(vacancy, False)
                    elif answer == "3":
                        # сортировка вниз
                        vacancy = SortingVacancyHeadHunter.sorting_vacancy_to_salary(vacancy, True)
                    elif answer == "4":
                        # выборка по зарплате
                        salary = int(input("Уровень отсева вакансий по зарплате: "))
                        for i in vacancy:
                            if i > salary:
                                print(i)
                    elif answer == "5":
                        # топ N по зарплате
                        quantity = int(input("Введите топ 'N' количество вакансий: "))
                        vacancy = SortingVacancyHeadHunter.sorting_vacancy_to_salary(vacancy, True)
                        for i in range(quantity):
                            if len(vacancy) < quantity:
                                print("--- " * 10)
                                print(f"Вакансий в списке всего {len(vacancy)} введите другое значение для сортировки")
                                break
                            print(vacancy[i])
                    elif answer == "exit":
                        break
                    print("--- " * 10)
            elif answer == "exit":
                break


if __name__ == "__main__":
    user_interaction()
