from src.string_calculator import add


def test_add_empty_string():
    assert add("") == 0


def test_add_single_number_1():
    assert add("1") == 1


def test_add_single_number_2():
    assert add("2") == 2


def test_add_two_numbers():
    assert add("1,2") == 3


def test_add_three_numbers():
    assert add("1,2,3") == 6


def test_add_several_numbers():
    assert add("1,2,3,4,5,6,7,8,9") == 45


