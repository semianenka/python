import argparse


class SimpleCalculator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process some arguments and flag eg. \n'
                                                          '--add (addition)\n'
                                                          '--sub (subtraction)\n'
                                                          '--mul (multiply)\n '
                                                          '--div (division)')
        self.parser.add_argument('numbers', type=int, metavar='N', nargs='+')
        self.parser.add_argument('-a', '--add', dest='addition', action='store_true')
        self.parser.add_argument('-s', '--sub', dest='subtraction', action='store_true')
        self.parser.add_argument('-m', '--mul', dest='multiply', action='store_true')
        self.parser.add_argument('-d', '--div', dest='division', action='store_true')
        self.args = self.parser.parse_args()
        self.result = 0

    def calculate(self):
        if self.args.addition:
            self.addition()
        if self.args.subtraction:
            self.subtraction()
        if self.args.multiply:
            self.multiply()
        if self.args.division:
            self.division()

    def addition(self):
        self.result = sum(self.args.numbers)

    def subtraction(self):
        self.result = self.args.numbers[0] - sum(self.args.numbers[1:])

    def multiply(self):
        self.result = 1
        for i in self.args.numbers:
            self.result *= i

    def division(self):
        try:
            self.result = self.args.numbers[0]
            for i in self.args.numbers[1:]:
                self.result /= i
        except ZeroDivisionError as e:
            print(f'An error {e} was occurred\n')
        finally:
            print('Последнее успешно полученное значение:')

    def get_result(self):
        return self.result


calc = SimpleCalculator()
calc.calculate()
print(calc.get_result())
