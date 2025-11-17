import math
from datetime import datetime

class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []
    
    def add(self, a, b):
        """Сложение двух чисел"""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Возведение в степень"""
        result = a ** b
        self._add_to_history(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a):
        """Квадратный корень"""
        if a < 0:
            raise ValueError("Квадратный корень из отрицательного числа")
        result = math.sqrt(a)
        self._add_to_history(f"√{a} = {result}")
        return result
    
    def _add_to_history(self, operation):
        """Добавление операции в историю"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {operation}")
    
    def show_history(self):
        """Показать историю вычислений"""
        if not self.history:
            print("История пуста")
        else:
            for operation in self.history:
                print(operation)
    
    def clear_history(self):
        """Очистить историю вычислений"""
        self.history.clear()

# Пример использования
if __name__ == "__main__":
    calc = Calculator()
    
    # Тестирование функций
    print("10 + 5 =", calc.add(10, 5))
    print("10 - 5 =", calc.subtract(10, 5))
    print("10 * 5 =", calc.multiply(10, 5))
    print("10 / 5 =", calc.divide(10, 5))
    print("2 ^ 3 =", calc.power(2, 3))
    print("√16 =", calc.square_root(16))
    
    print("\nИстория операций:")
    calc.show_history()