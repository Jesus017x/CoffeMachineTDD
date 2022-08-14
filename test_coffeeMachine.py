import unittest
from coffeeMachine import get_coffee
from coffeeMachine import is_resource_sufficient
from coffeeMachine import process_coin
from coffeeMachine import is_transaction_okay
from coffeeMachine import get_sugar


class TestCupSelection(unittest.TestCase):
    def runTest(self):
        self.assertTrue(get_coffee)

class TestResourcesSufficient(unittest.TestCase):
    def runTest(self):
        self.assertTrue(is_resource_sufficient)

class TestProcessCoin(unittest.TestCase):
    def runTest(self):
        self.assertTrue(process_coin)

class TestIsTransactionOkay(unittest.TestCase):
    def runTest(self):
        self.assertTrue(is_transaction_okay)

class TestGetSugar(unittest.TestCase):
    def runTest(self):
        self.assertTrue(get_sugar)

if __name__ == '__main__':
    unittest.main()