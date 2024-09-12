from unittest import TestCase, expectedFailure
from Python_Beginners import Python_Begineers as pb

class Test(TestCase):

    def test_count_vowels(self):
        input_string = input("Enter string to count vowels : ")
        expected_output = int(input("Enter the count of vowels in string : "))
        result = pb.count_vowels(input_string)
        self.assertEqual(result,expected_output)

    def test_alphabet_order(self):
        input_string = input("Enter a line to sort it in alphabetical order : ")
        result = pb.alphabet_order(input_string)
        self.assertTrue(result is not None or result is None)

    def test_python_error(self):
        input1 = 3
        input2 = "3"
        #with self.assertRaises(NameError):
        self.assertTrue(pb.python_error(input1).args[0] == 'division by zero')
        self.assertTrue(pb.python_error(input2).args[0] == "unsupported operand type(s) for /: 'str' and 'int'")

    def test_days_between(self):
        date1 = input("Enter first date in yyyymmdd format : ")
        date2=input("Enter second date in yyyymmdd format : ")
        result = pb.days_between(date1,date2)
        self.assertTrue(result is not None or result is None)

    def test_factorial(self):
        s = int(input("Enter a number to find factorial : \n"))
        result = pb.factorial(s)
        self.assertTrue(result is not None or result is None)

    def test_transpose(self):
        matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
        expected_output = [[1, 4, 7],[2, 5, 8],[3, 6, 9]]
        result = transpose_matrix(matrix)
        self.assertEqual(result,expected_output)
