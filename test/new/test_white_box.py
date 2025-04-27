import pytest
from my_project import some_internal_function

def test_internal_logic():
    result = some_internal_function(2, 3)
    assert result == 5, "Internal function logic failed"

