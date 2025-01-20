import pytest
from um import count

@pytest.mark.parametrize("text, um_count",[
    ("", 0),
    (" ", 0)
])
def test_um_for_an_empty_text(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count",[
    ("um, um, um, hello, world", 3),
    ("um , um , um , hello, world", 3),
    ("um um um  hello world", 3),
    ("um hello world", 1),
    ("um, hello world", 1),
])
def test_um_appearing_at_the_start_of_the_string(text, um_count):
    assert count(text) == um_count

@pytest.mark.parametrize("text, um_count", [
    ("Hello world, um", 1),
    ("hello, world um, um", 2),
    ("hello world, um um ", 2)
])
def test_um_appearing_at_end_of_string(text, um_count):
    assert count(text) == um_count