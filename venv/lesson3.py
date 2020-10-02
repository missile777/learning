
import unittest

def get_first(n: list):
    return n[0]

def get_second(n: list):
    return n[1]

def is_empty(n: list):
    return len(n) == 0


class TestListMethod(unittest.TestCase):
    def test_get_first(self):
        nums = [10, 20, 40, 80]
        self.assertEqual(get_first(nums), 10)

    def test_get_second(self):
        nums = [10, 20, 40, 40, 80]
        self.assertEqual(get_second(nums), 20)

    def test_if_empty(self):
        nums = []
        self.assertEqual(is_empty(nums), True)

    def test_if_empty(self):
        nums = [10, 20]
        self.assertEqual(is_empty(nums), False)



if __name__ == '__main__':
    unittest.main()