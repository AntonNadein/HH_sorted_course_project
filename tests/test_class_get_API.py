from unittest.mock import patch

import pytest
from requests.exceptions import RequestException, Timeout

from src.class_get_API import HeadHunterAPI, ParserHH


def test_hh_api():
    """тест экземпляров класса HeadHunterAPI"""
    hh_api = HeadHunterAPI("Python", 1, 10, 20)
    assert hh_api.search_text == "Python"
    assert hh_api.city_key == 1
    assert hh_api.page == 10
    assert hh_api.per_page == 20
    assert hh_api.params == {"text": "Python", "area": 1, "page": 10, "per_page": 20}


def test_hh_api_none():
    """тест экземпляров класса HeadHunterAPI при отсутсвующих параметрах"""
    hh_api = HeadHunterAPI("Python")
    assert hh_api.search_text == "Python"
    assert hh_api.city_key is None
    assert hh_api.page == 0
    assert hh_api.per_page == 30
    assert hh_api.params == {"text": "Python", "area": None, "page": 0, "per_page": 30}


@patch("requests.get")
def test_get_api_hh(mocked_get, test_list_dict_input):
    """тест работы HeadHunterAPI"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = test_list_dict_input
    hh_api = HeadHunterAPI("Python", 1, 10, 20)
    result = hh_api.get_vacancies
    assert result == [{"name": "test1", "area": {"name": "test3"}, "salary": "test2", "alternate_url": "test4"}]


@patch("requests.get")
def test_get_api_hh_type_error(mocked_get, capsys):
    """тест экземпляров класса HeadHunterAPI при отсутсвующих параметрах"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = None
    hh_api = HeadHunterAPI("Python", 1, 2.1, 20)
    result = hh_api.get_vacancies
    message = capsys.readouterr()
    assert message.out.strip() == "Введены не корретные данные TypeError: 'NoneType' object is not subscriptable"
    assert result is None


@patch("requests.get")
def test_get_api_hh_attribute_error(mocked_get, capsys):
    """тест экземпляров класса HeadHunterAPI при отсутсвующих параметрах"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = None
    hh_api = HeadHunterAPI("Python", city_key=-10, page=1, per_page=-20)
    result = hh_api.get_vacancies
    message = capsys.readouterr()
    assert message.out.strip() == "Введены не корретные данные TypeError: 'NoneType' object is not subscriptable"
    assert result is None


def test_request_exception(parser_hh):
    """Тест ошибки: общие ошибки запроса"""
    with patch("requests.get", side_effect=RequestException):
        with pytest.raises(RequestException):
            print(parser_hh.get_vacancies)


@patch("requests.get")
def test_failed_response(mocked_get, parser_hh, test_list_dict_input, capsys):
    """Тест ошибки: сайт не отвечает"""
    mocked_get.return_value.status_code = 404
    mocked_get.return_value.json.return_value = test_list_dict_input
    result = parser_hh.get_vacancies
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[0] == "Запрос не был успешным."
    assert message.out.strip().split("\n")[-1] == "Произошла ошибка."
    assert result is None


def test_timeout_exception(parser_hh):
    """Тест ошибки: время ожидания превышино"""
    with patch("requests.get", side_effect=Timeout):
        with pytest.raises(Timeout):
            print(parser_hh.get_vacancies)


def test_parser_hh_init():
    """Тест ошибки: время ожидания превышино"""
    with pytest.raises(TypeError):
        ParserHH(123)
