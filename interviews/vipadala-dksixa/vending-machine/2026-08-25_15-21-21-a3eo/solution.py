from abc import ABC, abstractmethod
from enum import Enum

class Solution:
    def run(self) -> None:
        print("Hello from your LLD design!")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class MachineState(Enum):
    IDLE = "idle"
    DISPLAY_ITEMS = "display items"
    SELECT_ITEMS = "select items"
    TRANSACTION = "transaction"
    SELECT_PAYMENT_TYPE = "payment_type"
    VALIDATE_PAYMENT = "validate_payment"
    DISPENSE = "dispense"

class VendingMachine:
    def __init__(self):
        self.products = [] ## Here we should add the products into machine
        self.state = None

    def set_state(self, state):
        self.state = state

    def fill_machine(self, products):
        self.products = products

    def execute(self, state):
        self.state.execute()

    ### Add other states



if __name__ == "__main__":
    Solution().run()
