import unittest
from unittest import mock
import numworksLibs
import main

class TestStringMethods(unittest.TestCase):

    @unittest.mock.patch("builtins.input")
    def test_simplify_fraction_01(self, mocked_input):
        mocked_input.side_effect = ['1', '3', '7']
        self.assertEqual(main.page1(), '3/7')
    @unittest.mock.patch("builtins.input")
    def test_simplify_fraction_02(self, mocked_input):
        mocked_input.side_effect = ['1', '99', '33']
        self.assertEqual(main.page1(), '3')
    @unittest.mock.patch("builtins.input")
    def test_simplify_fraction_03(self, mocked_input):
        mocked_input.side_effect = ['1', '5', '1']
        self.assertEqual(main.page1(), '5')
    @unittest.mock.patch("builtins.input")
    def test_simplify_fraction_04(self, mocked_input):
        mocked_input.side_effect = ['1', '5', '0']
        self.assertEqual(main.page1(), 'Division by 0 - result undefined')
    @unittest.mock.patch("builtins.input")
    def test_factor_quadratic_01(self, mocked_input):
        mocked_input.side_effect = ['2', '1', '5', '4']
        self.assertEqual(main.page1(), '(1x+1)(1x+4)')
    @unittest.mock.patch("builtins.input")
    def test_factor_quadratic_02(self, mocked_input):
        mocked_input.side_effect = ['2', '1', '99', '23']
        self.assertEqual(main.page1(), 'No factorization')
    @unittest.mock.patch("builtins.input")
    def test_factor_quadratic_03(self, mocked_input):
        mocked_input.side_effect = ['2', '1', '2', '3']
        self.assertEqual(main.page1(), 'Solutions are imaginary')
    @unittest.mock.patch("builtins.input")
    def test_solve_linear_func_01(self, mocked_input):
        mocked_input.side_effect = ['3', 'f', '1', '2', '3']
        self.assertEqual(main.page1(), 'f(2)= 5')
    @unittest.mock.patch("builtins.input")
    def test_solve_linear_func_02(self, mocked_input):
        mocked_input.side_effect = ['3', 'g', '23', '1', '2']
        self.assertEqual(main.page1(), 'g(1)= 25')
    @unittest.mock.patch("builtins.input")
    def test_solve_linear_func_03(self, mocked_input):
        mocked_input.side_effect = ['3', 'a', '4', '4', '13']
        self.assertEqual(main.page1(), 'a(4)= 29')
    def test_find_dr_ordered_pair_01(self):
        self.assertEqual(numworksLibs.find_domain_range_ordered(['1', '3'], ['2', '4']), "Domain: 1, 3\nRange: 2, 4")
    def test_find_dr_ordered_pair_02(self):
        self.assertEqual(numworksLibs.find_domain_range_ordered(['1', '3', '3', '4'], ['2', '4', '2', '4']), "Domain: 1, 3, 4\nRange: 2, 4")
    def test_represents_float_01(self):
        self.assertTrue(numworksLibs.RepresentsFloat('4.9789'))
    def test_represents_float_02(self):
        self.assertTrue(numworksLibs.RepresentsFloat('9'))
    def test_represents_float_03(self):
        self.assertFalse(numworksLibs.RepresentsFloat('f'))
    def test_represents_float_04(self):
        self.assertFalse(numworksLibs.RepresentsFloat('fght'))
    @unittest.mock.patch("builtins.input")    
    def test_solve_pythagorean_01(self, mocked_input):
        mocked_input.side_effect = ['5', 'a', '2', '7']
        self.assertEqual(main.page1(), 'a ≈ 6.71')
    @unittest.mock.patch("builtins.input")
    def test_solve_pythagorean_02(self, mocked_input):
        mocked_input.side_effect = ['5', 'b', '6.7082', '7']
        self.assertEqual(main.page1(), 'b ≈ 2.0')
    @unittest.mock.patch("builtins.input")
    def test_solve_pythagorean_03(self, mocked_input):
        mocked_input.side_effect = ['5', 'c', '6.7082', '2.00001']
        self.assertEqual(main.page1(), 'c ≈ 7.0')

if __name__ == '__main__':
    unittest.main()