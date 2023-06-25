import logging


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
