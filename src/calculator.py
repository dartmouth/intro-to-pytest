from numbers import Number


class Calculator:

    def _validate_inputs(self, a, b):
        if not (isinstance(a, Number) and isinstance(b, Number)):
            raise TypeError("Inputs must be numbers")

    def add(self, a: Number, b: Number) -> Number:
        self._validate_inputs(a, b)
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        self._validate_inputs(a, b)
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        self._validate_inputs(a, b)
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        self._validate_inputs(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
