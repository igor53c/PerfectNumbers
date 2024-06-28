import unittest
from perfect_numbers import is_perfect_number, find_mersenne_primes, find_perfect_numbers


class TestPerfectNumbers(unittest.TestCase):

    def test_is_perfect_number_6(self):
        expected_result = {
            'divisors': [1, 2, 3],
            'total': 6,
            'is_perfect': True
        }
        result = is_perfect_number(6)
        self.assertEqual(result, expected_result)

    def test_is_perfect_number_10(self):
        expected_result = {
            'divisors': [1, 2, 5],
            'total': 8,
            'is_perfect': False
        }
        result = is_perfect_number(10)
        self.assertEqual(result, expected_result)

    def test_is_perfect_number_28(self):
        expected_result = {
            'divisors': [1, 2, 4, 7, 14],
            'total': 28,
            'is_perfect': True
        }
        result = is_perfect_number(28)
        self.assertEqual(result, expected_result)

    def test_is_perfect_number_496(self):
        expected_result = {
            'divisors': [1, 2, 4, 8, 16, 31, 62, 124, 248],
            'total': 496,
            'is_perfect': True
        }
        result = is_perfect_number(496)
        self.assertEqual(result, expected_result)

    def test_find_mersenne_primes(self):
        expected_result = [3, 7, 31, 127]
        result = find_mersenne_primes(1000)
        self.assertEqual(result, expected_result)

    def test_find_perfect_numbers(self):
        expected_result = [6, 28, 496, 8128]
        result = find_perfect_numbers(10000)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
