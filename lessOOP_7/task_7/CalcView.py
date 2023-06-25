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
        print("! Введено не число. введите число")

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
