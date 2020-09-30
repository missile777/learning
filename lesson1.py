import unittest


def get_evens(n: list):
    return [i for i in n if i % 2 == 0]


def get_odds(n: list):
    return [i for i in n if i % 2 == 1]


class TestEvenMethod(unittest.TestCase):
    def test_get_evens(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.assertListEqual(get_evens(nums), [2, 4, 6, 8, 10, 12, 14, 16])

    def test_get_odds(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.assertListEqual(get_odds(nums), [1, 3, 5, 7, 9, 11, 13, 15, 17])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(get_evens(nums))
print(get_odds(nums))

unittest.main()
