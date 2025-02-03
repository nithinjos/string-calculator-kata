import pytest

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


def test_add_newline_delimiter():
    assert add("1\n2,3") == 6
    assert add("1\n2\n3") == 6
    assert add("1,2,3\n4") == 10


def test_add_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//|\n1|2|3") == 6
    assert add("//.\n1.2.3.4") == 10
    assert add("//.\n1.2\n3.4") == 10
    assert add("//.\n1.2\n3\n4") == 10


def test_add_negative_numbers():

    with pytest.raises(ValueError) as e:
        add("-1,2")
    assert str(e.value) == "negative numbers not allowed: -1"

    with pytest.raises(ValueError) as e:
        add("1,-2,-3,-6,7,-3")
    assert str(e.value) == "negative numbers not allowed: -2, -3, -6, -3"


def test_add_numbers_bigger_than_1000():
    assert add("1001,2") == 2
    assert add("1000,2") == 1002
    assert add("1000,1000") == 2000
    assert add("1001,1001") == 0
