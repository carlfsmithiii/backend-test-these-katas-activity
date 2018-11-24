import unittest
from katas import add, multiply, power, factorial, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        # self.fail("TODO: Write add unit test")
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3, 6), 9)
        self.assertEqual(add(-3, 7), 4)

    def test_multiply(self):
        # self.fail("TODO: Write multiply unit test")
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(0, 2), 0)

    def test_power(self):
        # self.fail("TODO: Write power unit test")
        self.assertEqual(power(2, 8), 256)

    def test_factorial(self):
        # self.fail("TODO: Write factorial unit test")
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_fibonacci(self):
        # self.fail("TODO: Write fibonacci unit test")
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(4), 2)
        self.assertEqual(fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()
