from lib.single_readable_line import *
import pytest
def test_pytest_setup_complete():
    assert True

def test_blank_list():
    assert single_readable_line([]) == ""

def test_single_name():
    assert single_readable_line(["Bob"]) == "Bob"

def test_with_two_names():
    assert single_readable_line(["Bob", "Bart"]) == "Bob & Bart"

def test_with_three_or_more_names():
    assert single_readable_line(["Bob", "Bart", "Bill"]) == "Bob, Bart & Bill"

def test_not_list_entered():
    with pytest.raises(Exception) as e:
        single_readable_line(5) 
    assert str(e.value) == "Please enter a list"