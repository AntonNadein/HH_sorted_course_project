import json
import tempfile
from unittest.mock import patch

import pytest

from src.class_sorting_vacancy import SortingVacancyHeadHunter
from src.save_to_file import SaveToJson


def test_save_to_file_init(test_init_save_to_json_1, test_init_save_to_json_2):
    """Тест инициализации"""
    assert test_init_save_to_json_1.file_name == "Vacancies.json"
    assert test_init_save_to_json_1.list_to_save == []
    assert test_init_save_to_json_2.file_name == "test_name.json"
    assert test_init_save_to_json_2.list_to_save == [
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


@patch("json.load")
def test_open_json_file_for_class(mock_file, test_init_save_to_json_1):
    """Тест преобразование json в список для
    класса SortingVacancyHeadHunter"""
    mock_file.return_value = [
        {"id": "1", "name": "Менеджер", "salary": 86000, "city": "Санкт-Петербург", "url": "https://test"}
    ]
    result = test_init_save_to_json_1.open_json_file_for_class()
    assert result == [
        {
            "id": "1",
            "name": "Менеджер",
            "salary": 86000,
            "area": {"name": "Санкт-Петербург"},
            "alternate_url": "https://test",
        }
    ]


def test_open_json_file_for_class_error_1(test_init_save_to_json_2):
    """Тест преобразование json в список для"""
    with pytest.raises(TypeError):
        test_init_save_to_json_2.open_json_file_for_class()


def test_add_vacancy_to_file():
    """Тест сохранения данных в файл json"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file_path = temp_file.name
    # Создаем экземпляр класса и сохраняем
    vacancy = SortingVacancyHeadHunter("1", "разработчик", 3000, "Санкт-Петербург", "https://hh.ru/")
    obj = SaveToJson(temp_file_path, [vacancy])
    obj.save_to_new_file()

    with open(f"{temp_file_path}.json", "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == [
        {"city": "Санкт-Петербург", "id": "1", "name": "разработчик", "salary": 3000, "url": "https://hh.ru/"}
    ]


def test_unique_vacancy_to_file():
    """Тест добавления уникальных данных в файл json"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file_path = temp_file.name
    # Создаем экземпляр класса и сохраняем
    vacancy_1 = SortingVacancyHeadHunter("1", "разработчик", 3000, "Санкт-Петербург", "https://hh.ru/")
    vacancy_2 = SortingVacancyHeadHunter("2", "разработчик", 3000, "Санкт-Петербург", "https://hh.ru/")
    vacancy_3 = SortingVacancyHeadHunter("3", "разработчик", 3000, "Санкт-Петербург", "https://hh.ru/")
    obj = SaveToJson(temp_file_path, [vacancy_1, vacancy_2])
    obj.save_to_new_file()
    obj2 = SaveToJson(temp_file_path, [vacancy_2, vacancy_3, vacancy_1])
    obj2.add_unique_vacancy_to_file()

    with open(f"{temp_file_path}.json", "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == [
        {"id": "1", "name": "разработчик", "salary": 3000, "city": "Санкт-Петербург", "url": "https://hh.ru/"},
        {"id": "2", "name": "разработчик", "salary": 3000, "city": "Санкт-Петербург", "url": "https://hh.ru/"},
        {"id": "3", "name": "разработчик", "salary": 3000, "city": "Санкт-Петербург", "url": "https://hh.ru/"},
    ]
