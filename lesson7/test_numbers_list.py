import unittest

class TestNumbersList(unittest.TestCase):
    def setUp(self):
        print("Preparing the list")
        self.numbers = [1,2,3,4,5]

    def tearDown(self):
        print("Removing numbers")

    def test_list_has_five_numbers(self):
        self.assertEqual(len(self.numbers),5)

    def test_list_has_four_number(self):
        self.assertIn(4,self.numbers)
        # self.assertEqual(self.numbers[4],5)
