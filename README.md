# HH.ru sorted!

## Описание:

HH.ru sorted! - это сортировщик вакансий сайта hh.ru на Python. И курсойвой проект для SkyPro.

## Использование:
* Клонируем репозитроий *git@github.com:AntonNadein/HH_sorted_course_project.git*
* Устанавливаем зависимоти **pyproject.toml**
* Запускаем функционал при помощи файлов **main.py**


## Документация:
1. Модуль *class_get_API.py* содержит класс для работы с API сервиса с вакансиями hh.ru. 
Класс подключается к API и получает вакансии.

2. Модуль *class_sorting_vacancy.py* класс для работы с вакансиями: поддерживает методы сравнения
вакансий между собой.

3. Модуль *save_to_file.py* класс реализует методы для добавления вакансий в файл,
получения данных из файла и удаления информации о вакансиях.


## Тестирование:
Для тестироваия используйте файлы 
**[test_class_get_API.py](tests%2Ftest_class_get_API.py)
[test_class_sorting_vacancy.py](tests%2Ftest_class_sorting_vacancy.py)
[test_save_to_file.py](tests%2Ftest_save_to_file.py)
[test_utils.py](tests%2Ftest_utils.py)**

test coverage 97%

## Лицензия:

Этот проект не имеет лицензий.