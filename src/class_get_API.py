from abc import ABC, abstractmethod

import requests


class ABCParser(ABC):
    """Абстрактный класс поиска вакансий."""

    @abstractmethod
    def get_vacancies(self):
        pass


class ParserHH(ABCParser):
    """Базовый класс поиска вакансий с HH.ru"""

    search_text: str

    def __init__(self, search_text: str) -> None:
        if type(search_text) is str:
            self.search_text = search_text
        else:
            raise TypeError("Текст поиска должен быть 'str'")
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": self.search_text,
        }

    def __get_vacancies(self):
        """Функция поиска вакансий по API"""
        try:
            response = requests.get(self.url, self.params, timeout=5)
            verified_response = self.__response_status_code(response)
            vacancies_data = verified_response.json()["items"]
            return vacancies_data
        except AttributeError:
            print("Произошла ошибка.")

    def __response_status_code(self, response):
        """Метод проверки API на ошибки
        :param response: Ответ от HH.ru
        :return: Ответ от HH.ru без ошибок
        """
        try:
            if response.status_code == 200:
                return response
        except requests.exceptions.Timeout:
            print("Время ожидания запроса истекло. Пожалуйста, проверьте свое интернет-соединение.")
        except requests.exceptions.RequestException:
            print("Произошла ошибка. Пожалуйста, повторите попытку позже.")
        else:
            print("Запрос не был успешным.")

    @property
    def get_vacancies(self):
        """Функция выводы вакансий найденых по API"""
        return self.__get_vacancies()


class HeadHunterAPI(ParserHH):
    """Класс поиска вакансий с HH.ru с дополнительными параметрами"""

    search_text: str
    city_key: int
    page: int
    per_page: int

    def __init__(self, search_text: str, city_key: int = None, page: int = None, per_page: int = None) -> None:
        super().__init__(search_text)
        self.page = page if page else 0
        self.per_page = per_page if per_page else 30
        if type(city_key) is int:
            self.city_key = city_key
        else:
            self.city_key = None
        self.params = {"text": self.search_text, "area": self.city_key, "per_page": self.per_page, "page": self.page}

    @property
    def get_vacancies(self):
        try:
            return super().get_vacancies
        except TypeError as e:
            print(f"Введены не корретные данные TypeError: {e}")
