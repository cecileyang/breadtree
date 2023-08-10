import unittest

from decision import decision


class TestDecision(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = ["2 years", "0", "0", "Strongly agree", "0", "0", "0", "0", "0"]
        actual_result = decision(data)
        expected_result = ['Based on your answer, we recommend:', 'You keep your current portfolio and reduce spending by 10%']
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()