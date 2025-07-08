import pytest

# نمونه تابع برای تست واحد
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    """تست تابع جمع اعداد"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_numbers_invalid_input():
    """تست ورودی نامعتبر"""
    with pytest.raises(TypeError):
        add_numbers("2", 3)