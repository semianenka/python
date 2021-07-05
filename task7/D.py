# Dependency inversion principle
class Item:
    def __init__(self, name):
        self.name = name


class Payment:
    def __init__(self, name):
        self.name = name

    def create_account(self, price, count):
        pass

    def get_payment_info(self):
        pass

    def get_success_url(self):
        pass

    def get_failure_url(self):
        pass

    def refund(self):
        pass


class CryptoPayment(Payment):
    def __init__(self, name):
        super().__init__(name)


class CardPayment(Payment):
    def __init__(self, name):
        super().__init__(name)


class PayPalPayment(Payment):
    def __init__(self, name):
        super().__init__(name)
