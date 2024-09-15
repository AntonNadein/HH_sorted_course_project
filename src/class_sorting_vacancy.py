from abc import ABC, abstractmethod


class SortingVacancy(ABC):
    """Абстрактный класс для взаимодействия с вакансиями."""

    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def cast_to_object_list(cls, list_vacancy) -> list:
        pass

    @abstractmethod
    def __str__(self):
        pass


class SortingVacancyHeadHunter(SortingVacancy):
    """Класс для взаимодействия с вакансиями с HH.ru."""

    __slots__ = ("id", "name", "salary", "city", "url")
    id: str
    name: str
    salary: float
    city: str
    url: str

    def __init__(self, id: str, name: str, salary: int | dict, city: str, url: str) -> None:
        self.id = id
        self.name = name
        if salary is None:
            self.__salary = 0
        elif type(salary) is dict:
            if salary.get("from") is None:
                self.__salary = salary.get("to")
            else:
                self.__salary = salary.get("from")
        elif type(salary) is float or type(salary) is int:
            self.__salary = salary
        else:
            raise TypeError("Вводымые данные должны быть численными.")
        self.city = city
        self.url = url

    @classmethod
    def cast_to_object_list(cls, list_vacancy: list) -> list:
        """
        Метод для создания списка экземпляров класса из полученного API или Json-файла
        :param list_vacancy: API или Json-файл
        :return: Список экземпляров класса вакансий
        """
        try:
            class_vacancy_list = [
                cls(data["id"], data["name"], data["salary"], data["area"]["name"], data["alternate_url"])
                for data in list_vacancy
            ]
            return class_vacancy_list
        except TypeError as e:
            print(f"Введены не корретные данные: {e}")

    @classmethod
    def __comparison(cls, other):
        """Вспомогательный метод класса для методов сравнения"""
        if not isinstance(other, (int, SortingVacancyHeadHunter)):
            raise TypeError("Операнд справа должен иметь тип int или SortingVacancyHeadHunter")
        return other if isinstance(other, int) else other.__salary

    @property
    def _salary(self):
        """Вывод параметра зарплаты"""
        return self.__salary

    @_salary.setter
    def _salary(self, new_salary):
        """Вывод параметра зарплаты"""
        self.__salary = new_salary

    def __str__(self):
        """Вывод информации для пользователя"""
        return f"Вакансия: {self.name} Зарплата: {self.__salary} Город: {self.city} Ссылка: {self.url}"

    def __lt__(self, other):
        """Метод сравнения меньше"""
        salary = self.__comparison(other)
        return self.__salary < salary

    def __gt__(self, other):
        """Метод сравнения больше"""
        salary = self.__comparison(other)
        return self.__salary > salary

    def __eq__(self, other):
        """Метод сравнения равно"""
        salary = self.__comparison(other)
        return self.__salary == salary

    @staticmethod
    def sorting_vacancy_to_salary(list_vacancy, reverse=True) -> list:
        """
        Метод для сортировки списка экземпляров класса по зарплате
        :param list_vacancy: список экземпляров класса
        :param reverse: Направление сортировки (по убыванию)
        :return: Отсортированный список
        """
        return sorted(list_vacancy, key=lambda i: i.__salary, reverse=reverse)
