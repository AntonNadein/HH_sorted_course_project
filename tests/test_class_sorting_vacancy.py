import pytest

from src.class_sorting_vacancy import SortingVacancyHeadHunter


def test_class_sorting_vacancy_init_1():
    """Тест инициализации нормальных условий"""
    vacancy_1 = SortingVacancyHeadHunter("3", "Разработчик", 30000, "Уфа", "http://test_3")
    assert vacancy_1.id == "3"
    assert vacancy_1.name == "Разработчик"
    assert vacancy_1._salary == 30000
    assert vacancy_1.city == "Уфа"
    assert vacancy_1.url == "http://test_3"


def test_class_sorting_vacancy_init_2():
    """Тест получения разных данных по зарплате"""
    vacancy_1 = SortingVacancyHeadHunter("3", "Разработчик", None, "Уфа", "http://test_3")
    vacancy_2 = SortingVacancyHeadHunter("3", "Разработчик", {"from": None, "to": 5000}, "Уфа", "http://test_3")
    vacancy_3 = SortingVacancyHeadHunter("3", "Разработчик", {"from": 6000, "to": 5000}, "Уфа", "http://test_3")
    assert vacancy_1._salary == 0
    assert vacancy_2._salary == 5000
    assert vacancy_3._salary == 6000


def test_class_sorting_vacancy_init_error():
    """Тест получения разных данных по зарплате вызов ошибки"""
    with pytest.raises(TypeError):
        SortingVacancyHeadHunter("3", "Разработчик", "None", "Уфа", "http://test_3")


def test_cast_to_object_list(test_list_dict_for_class_sort):
    """Тест класс метода"""
    vacancy = SortingVacancyHeadHunter.cast_to_object_list(test_list_dict_for_class_sort)
    assert vacancy[0].id == "1"
    assert vacancy[1].id == "2"
    assert len(vacancy) == 2


def test_cast_to_object_list_error(test_list_dict_for_class_sort_error, capsys):
    """Тест ошибки полученых данных"""
    vacancy = SortingVacancyHeadHunter.cast_to_object_list(test_list_dict_for_class_sort_error)
    message = capsys.readouterr()
    assert message.out.strip() == "Введены не корретные данные: string indices must be integers, not 'str'"
    assert vacancy is None


def test_cast_to_object_list_getter(test_list_dict_for_class_sort):
    """Тест геттера и сеттера зарплаты"""
    vacancy = SortingVacancyHeadHunter.cast_to_object_list(test_list_dict_for_class_sort)
    assert vacancy[0]._salary == 86000
    vacancy[0]._salary = 45000
    assert vacancy[0]._salary == 45000


def test_cast_to_object_list_comparison(test_list_dict_for_class_sort):
    """Тест методов сравнения"""
    vacancy = SortingVacancyHeadHunter.cast_to_object_list(test_list_dict_for_class_sort)
    assert vacancy[0] > vacancy[1]
    assert vacancy[0] > 20000
    assert vacancy[1] < vacancy[0]
    assert vacancy[1] < 40000
    vacancy[0]._salary = 30000
    result = vacancy[0] == vacancy[1]
    result_2 = vacancy[0] == 86000
    assert result is True
    assert result_2 is False


def test_cast_to_object_list_comparison_error(test_list_dict_for_class_sort):
    """Тест методов сравнения"""
    with pytest.raises(TypeError):
        vacancy = SortingVacancyHeadHunter.cast_to_object_list(test_list_dict_for_class_sort)
        print(vacancy[0] > "20000")


def test_sorting_vacancy_print():
    """Тест вывода информации"""
    vacancy_1 = SortingVacancyHeadHunter("3", "Разработчик", 30000, "Уфа", "http://test_3")
    assert str(vacancy_1) == "Вакансия: Разработчик Зарплата: 30000 Город: Уфа Ссылка: http://test_3"
