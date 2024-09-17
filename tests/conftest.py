import pytest

from src.class_get_API import ParserHH
from src.save_to_file import SaveToJson


@pytest.fixture
def test_list_dict_input():
    return {"items": [{"name": "test1", "area": {"name": "test3"}, "salary": "test2", "alternate_url": "test4"}]}


@pytest.fixture
def parser_hh():
    return ParserHH("Юрист")


@pytest.fixture
def test_list_dict_for_class_sort():
    return [
        {
            "id": "1",
            "name": "Менеджер",
            "salary": 86000,
            "area": {"name": "Санкт-Петербург"},
            "alternate_url": "https://test_1",
        },
        {
            "id": "2",
            "name": "Диспетчер",
            "salary": 30000,
            "area": {"name": "Россия"},
            "alternate_url": "https://test_2",
        },
    ]


@pytest.fixture
def test_list_dict_for_class_sort_error():
    return {
        "id": 1,
        "name": "Диспетчер",
        "salary": 86000,
        "area": {"name": "Санкт-Петербург"},
        "alternate_url": "https://test_1",
    }


@pytest.fixture
def test_list_dict_for_json_to_save():
    return [
        {
            "id": "94216601",
            "name": "Менеджер (стажер)",
            "salary": 86000,
            "city": "Санкт-Петербург",
            "url": "https://hh.ru/vacancy/94216601",
        },
        {
            "id": "106735215",
            "name": "Диспетчер чатов (в Яндекс)",
            "salary": 30000,
            "city": "Россия",
            "url": "https://hh.ru/vacancy/106735215",
        },
    ]


@pytest.fixture
def test_init_save_to_json_1():
    return SaveToJson()


@pytest.fixture
def test_init_save_to_json_2(test_list_dict_for_json_to_save):
    return SaveToJson("test_name", test_list_dict_for_json_to_save)
