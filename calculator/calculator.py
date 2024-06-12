class Calculator:
    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append(('add', a, b, result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append(('subtract', a, b, result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append(('multiply', a, b, result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(('divide', a, b, result))
        return result

    @classmethod
    def get_last_calculation(cls):
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()
