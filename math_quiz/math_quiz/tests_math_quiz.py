import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = choose_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the operator is among the one's mentioned
        operator=choose_operator()
        if operator in ['+', '-', '*']:
            print("The operator is one among these")
        else:
             print("Different operator!!!")
             

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 4, '-', '10 - 4', 6),
                (11, 6, '*', '11 * 6', 66)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation (num1, num2, operator)
                self.assertEqual(problem,expected_problem)
                

if __name__ == "__main__":
    unittest.main()
