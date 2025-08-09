from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    def __init__(self,amount):
        self.amount=amount
    @abstractmethod
    def  process_payment(self):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}")

class UPI(PaymentMethod):
    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}")

class Cash(PaymentMethod):
    def process_payment(self):
        print(f"Processing payment of ₹{self.amount}")

methods=[CreditCard(5000),UPI(1200),Cash(250)]
for method in methods:
    print(f"{method.__class__.__name__}:",end="")
    method.process_payment()
