import argparse


class SimpleCalculator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Simple console calculator welcomes you\n')
        self.parser.add_argument('numbers', type=int, metavar='N', nargs='+')
        self.parser.add_argument('-a', '--add', dest='addition', action='store_true', help='addition')
        self.parser.add_argument('-s', '--sub', dest='subtraction', action='store_true', help='subtraction')
        self.parser.add_argument('-m', '--mul', dest='multiply', action='store_true', help='multiply')
        self.parser.add_argument('-d', '--div', dest='division', action='store_true', help='division')
        self.args = self.parser.parse_args()

    def calculate(self):
        try:
            return self.call_funcs()
        except Exception as e:
            return f'An error {e} was occurred.'

    def call_funcs(self):
        if self.args.addition:
            return self.addition()
        elif self.args.subtraction:
            return self.subtraction()
        elif self.args.multiply:
            return self.multiply()
        elif self.args.division:
            return self.division()
        else:
            raise Exception('Flag is missing')

    def addition(self):
        return sum(self.args.numbers)

    def subtraction(self):
        return self.args.numbers[0] - sum(self.args.numbers[1:])

    def multiply(self):
        result = 1
        for i in self.args.numbers:
            result *= i
        return result

    def division(self):
        try:
            result = self.args.numbers[0]
            for i in self.args.numbers[1:]:
                result /= i
            return result
        except ZeroDivisionError as e:
            return f'An error {e} was occurred.'


print(SimpleCalculator().calculate())
