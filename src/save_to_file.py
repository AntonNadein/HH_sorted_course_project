import json
import os
from abc import ABC, abstractmethod
from json import JSONDecodeError


class SaveToFile(ABC):
    """Абстрактный класс для срхранения вакансий в файл."""

    @abstractmethod
    def save_to_new_file(self):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass


class SaveToJson(SaveToFile):
    """Класс для преобразования и сохранения класса
    SortingVacancyHeadHunter в Json файл"""

    file_name: str
    list_to_save: list

    def __init__(self, file_name: str = None, list_to_save: list = None) -> None:
        self.__file_name = f"{file_name}.json" if file_name else "Vacancies.json"
        self.list_to_save = list_to_save if list_to_save else []
        self.__path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", self.__file_name)

    @property
    def file_name(self):
        return self.__file_name

    def __class_to_list_dict(self) -> list:
        """Функция для приведения списка класса
        SortingVacancyHeadHunter к формату для
        записи в Json файл"""
        add_list = []
        for i in self.list_to_save:
            add_dict = {"id": i.id, "name": i.name, "salary": i._salary, "city": i.city, "url": i.url}
            add_list.append(add_dict)
        return add_list

    def __open_file_write(self, file_data) -> None:
        """
        Функция открытия файла для перезаписи
        :param file_data: Данные для перезаписи
        """
        with open(self.__path_to_file, "w", encoding="utf-8") as file:
            json.dump(file_data, file, ensure_ascii=False, indent=4)

    def __open_file_read(self) -> list:
        """
        Функция открытия файла для чтения
        :return: Данные открытого файла
        """
        try:
            with open(self.__path_to_file, "r", encoding="utf-8") as file_open:
                data_file = json.load(file_open)
                return data_file
        except JSONDecodeError:
            print("Json файл пуст, возпользуйтесь функцией добавления")
        except FileNotFoundError:
            print("Отсутствует файл в папке data.")

    def save_to_new_file(self) -> None:
        """
        Функция сохранения списка словарей в файл json
        """
        add_list = self.__class_to_list_dict()
        self.__open_file_write(add_list)

    def add_unique_vacancy_to_file(self) -> None:
        """
        Функция добавление уникальных данных в файл json
        """
        data_file = self.__open_file_read()
        add_list = self.__class_to_list_dict()
        merged_list = data_file + add_list
        unique_elements = []
        for item in merged_list:
            if item not in unique_elements:
                unique_elements.append(item)
        self.__open_file_write(unique_elements)

    def del_vacancies(self) -> None:
        """
        Функция удаляет содержимое файла JSON
        """
        with open(self.__path_to_file, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    def open_json_file_for_class(self) -> list:
        """
        Функция преобразование json в список для
        класса SortingVacancyHeadHunter
        :return: список словарей
        """
        data_file = self.__open_file_read()
        add_list = []
        for i in data_file:
            add_dict = {
                "id": i["id"],
                "name": i["name"],
                "salary": i["salary"],
                "area": {"name": i["city"]},
                "alternate_url": i["url"],
            }
            add_list.append(add_dict)
        return add_list
