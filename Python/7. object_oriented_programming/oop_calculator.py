# Create OOP Calculator

class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, num):
        self.total += num

    def subtract(self, num):
         self.total -= num

    def multiply(self, num):
        self.total *= num

    def divide(self, num):
        self.total /= num

    def equals(self):
        return_value = self.total
        self.total = 0
        return return_value


calc = Calculator()
calc.add(5)
