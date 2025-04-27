def add(a, b):
    """جمع دو عدد."""
    return a + b

def subtract(a, b):
    """تفریق دو عدد."""
    return a - b

def multiply(a, b):
    """ضرب دو عدد."""
    return a * b

def divide(a, b):
    """تقسیم دو عدد. اگر ب صفر باشد، خطا می‌دهد."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

