class Calculator:
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def multy(a, b):
        return a * b

    def div(a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError
