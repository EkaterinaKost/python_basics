import CalcView


class CalcModel:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number

    def subtract(self, number):
        print(number)
        a = self.result - number
        self.result = a

    def divide(self, number):
        localNumber = CalcView()
        while number == 0:
            print("!на ноль делить НЕЛЬЗЯ")
            number = localNumber.getInputOperator_2()
        self.result /= number

    def multiply(self, number):
        self.result *= number

    def getResult(self):
        return self.result

    def setResult(self, result):
        self.result = result
