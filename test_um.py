import pytest
from um import count

@pytest.mark.parametrize("text, um_count",[
    ("", 0),
    (" ", 0)
])
def test_count_for_an_empty_text(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count",[
    ("um, um, um, hello, world", 3),
    ("um , um , um , hello, world", 3),
    ("um um um  hello world", 3),
    ("um hello world", 1),
    ("um, hello world", 1),
])
def test_count_appearing_at_the_start_of_the_string(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count", [
    ("Hello world, um", 1),
    ("hello, world um, um", 2),
    ("hello world, um um ", 2)
])
def test_count_appearing_at_end_of_string(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count", [
    ("hello, world um, i am learning python", 1),
    ("My name is Doe, um um, hello world", 2)
])
def test_count_appearing_at_middle_of_string(text, um_count):
    assert count(text) == um_count

def test_count_as_a_sub_string_of_another_word():
    assert count("This food is yummy") == 0

@pytest.mark.parametrize("text, um_count",[
    ("UM, hello world", 1),
    ("um, hello world", 1)
])
def test_count_case_insensitivley(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count", [
    ("Hello world", 0),
    ("Learning Python is smooth", 0)
])
def test_count_with_no_um_present(text, um_count):
    assert count(text) == um_count