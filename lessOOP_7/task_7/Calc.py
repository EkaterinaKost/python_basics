import logging


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


class CalcPresenter:
    def __init__(self, model_1, view_1, number=90):
        self.model = model_1
        self.view = view_1
        self.operator = number

    def performCalculation(self):
        logging.basicConfig(level=logging.INFO, filename="calc_log_1.log",
                            filemode="w")

        logger = logging.getLogger("log_1")
        number = self.view.getInputOperator_1()
        self.operator = self.view.getInputOperator()
        number_2 = self.view.getInputOperator_2()
        self.model.setResult(number)

        if self.operator == "+":
            self.model.add(number_2)

        elif self.operator == '-':
            self.model.subtract(number_2)
        elif self.operator == "*":
            self.model.multiply(number_2)
        elif self.operator == "/":
            self.model.divide(number_2)
        elif self.operator == "stop":
            return
        logger.info('{0} {1} {2} = {3}'.format(number, self.operator, number_2,
                                               self.model.getResult()))
        self.view.displayResult(self.model.getResult())


class CalcView:

    def getInputOperator(self):
        print("Введите оператор (+, -, *, /, stop - для выхода из калькулятора): ")
        c = input()

        if c == "+" or c == "-" or c == "/" or c == "*" or c == "stop":
            return c
        print("! некорректная операция,попробуйте ещё раз")
        return self.getInputOperator()

    def displayResult(self, result):
        print("Result: " + str(result))

    def except_err(self):
        print("! Введено не число. Введите число")

    def getInputOperator_1(self):
        print("Ведите первое число: ")
        try:
            s = input()
            n = int(s)
            return n
        except (Exception):
            self.except_err()
            return self.getInputOperator_1()

    def getInputOperator_2(self):

        print("введите второе число: ")

        try:
            s = input()
            n = int(s)
            return n
        except (Exception):
            self.except_err()
            return self.getInputOperator_2()


view = CalcView()
model = CalcModel()
presenter = CalcPresenter(model, view)
while not (presenter.operator == "stop"):
    presenter.performCalculation()
