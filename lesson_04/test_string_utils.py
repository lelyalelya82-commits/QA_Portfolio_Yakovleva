

import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# ========== ФУНКЦИЯ 1: capitalize (2 существующих теста, расширены) ==========

def test_capitalize_positive(utils):
    """Позитивный: обычная строка в нижнем регистре"""
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_negative_empty(utils):
    """Негативный/граничный: пустая строка остаётся пустой"""
    assert utils.capitalize("") == ""


# ========== ФУНКЦИЯ 2: trim (2 новых теста) ==========

def test_trim_positive_leading_spaces(utils):
    """Позитивный: удаляет пробелы в начале строки"""
    assert utils.trim("   skypro") == "skypro"


def test_trim_negative_no_spaces(utils):
    """Граничный/негативный: строка без пробелов в начале не меняется"""
    assert utils.trim("skypro") == "skypro"


# ========== ФУНКЦИЯ 3: contains (2 новых теста) ==========

def test_contains_positive_symbol_present(utils):
    """Позитивный: символ присутствует в строке"""
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative_symbol_absent(utils):
    """Негативный: символа нет в строке — возвращает False"""
    assert utils.contains("SkyPro", "U") is False


# ========== ФУНКЦИЯ 4: delete_symbol (2 новых теста) ==========

def test_delete_symbol_positive_single_char(utils):
    """Позитивный: удаление одного символа"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_negative_symbol_absent(utils):
    """Негативный: символа нет — строка не меняется"""
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"