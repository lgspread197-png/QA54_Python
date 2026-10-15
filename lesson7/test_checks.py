import unittest


class TestChecks(unittest.TestCase):
    def setUp(self):
        print("SetUp called")

    def tearDown(self):
        print("Tear Down called")

    def test_start(self):
        print("test_start")
    def test_end(self):
        print("test_end")
    def test_end2(self):
        print("test_end2")

# тесты отрабатываются пока в алфавитном порядке