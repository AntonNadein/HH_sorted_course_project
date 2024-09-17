import unittest
from unittest.mock import patch

import pytest

from src.utils import selection_condition, tuple_value_filtering


class TestSelectionCondition(unittest.TestCase):
    """Тест функции логики выбора"""

    @patch("builtins.input", side_effect=["1", "2", "3", "4", "5", "0"])
    def test_selection_condition(self, mock_input):
        result = selection_condition("question", "1", "2", "3", "4", "5")
        self.assertEqual(result, "1")

        result = selection_condition("question", "1", "2", "3")
        self.assertEqual(result, "2")

        result = selection_condition("question", "1", "2", "3", "4")
        self.assertEqual(result, "3")

        result = selection_condition("question", "1", "2", "3", "4")
        self.assertEqual(result, "4")

        result = selection_condition("question", "1", "2", "3", "4", "5")
        self.assertEqual(result, "5")

        result = selection_condition("question", "1", "2")
        self.assertEqual(result, "exit")


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1, 2", (1, 2)),
        ("2, 1", (1, 2)),
        ("", (None, None)),
        ("-50, 50", (None, None)),
        ("-50, -50", (None, None)),
        (" , 50", (None, None)),
        ("50", (None, None)),
        ("-50", (None, None)),
        (", 50", (None, None)),
    ],
)
def test_tuple_value_filtering(input_data, expected):
    """Тест функции для отсеивания значений кортежа"""
    assert tuple_value_filtering(input_data) == expected
