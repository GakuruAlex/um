import pytest
from um import count

@pytest.mark.parametrize("text, um_count",[
    ("", 0),
    (" ", 0)
])
def test_um_for_an_empty_text(text, um_count):
    assert count(text) == um_count

