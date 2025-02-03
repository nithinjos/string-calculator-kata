from src.string_calculator import add


def test_add_empty_string():
    assert add("") == 0


def test_add_single_number_1():
    assert add("1") == 1


def test_add_single_number_2():
    assert add("2") == 2
