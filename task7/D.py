# Dependency inversion principle
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

    # and similar funcs
    def get_success_url(self):
        pass


class CardPayment(Payment):
    def __init__(self, name):
        super().__init__(name)

        # and similar funcs
        def get_success_url(self):
            pass


class PayPalPayment(Payment):
    def __init__(self, name):
        super().__init__(name)

        # and similar funcs
        def get_success_url(self):
            pass


class Shop:
    def __init__(self, name):
        self.name = name

    def get_success_url(self, payment):
        return payment.get_success_url()
