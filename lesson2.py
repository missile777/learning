import unittest


def reverse(n: list):
    # do this function
    return list(reversed(n))


class TestListMethod(unittest.TestCase):
    def test_get_reverse1(self):
        nums = [10, 20, 40, 80]
        self.assertListEqual(reverse(nums), [80, 40, 20, 10])

    def test_get_reverse2(self):
        nums = [10, 20, 40, 40, 80]
        self.assertListEqual(reverse(nums), [80, 40, 40, 20, 10])


if __name__ == '__main__':
    unittest.main()
