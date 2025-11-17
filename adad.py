class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b
    
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
