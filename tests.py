import unittest
import numworksLibs

class TestStringMethods(unittest.TestCase):

    def test_simplify_fraction_01(self):
        self.assertEqual(numworksLibs.simplify_fraction(3, 7), '3/7')
    def test_simplify_fraction_02(self):
        self.assertEqual(numworksLibs.simplify_fraction(99, 33), '3')
    def test_simplify_fraction_03(self):
        self.assertEqual(numworksLibs.simplify_fraction(5, 1), '5')
    def test_factor_quadratic_01(self):
        self.assertEqual(numworksLibs.quadratic_function(1, 5, 4), '(1x+1)(1x+4)')
    def test_factor_quadratic_02(self):
        self.assertEqual(numworksLibs.quadratic_function(1, 99, 23), 'No factorization')
    def test_factor_quadratic_03(self):
        self.assertEqual(numworksLibs.quadratic_function(1, 2, 3), 'Solutions are imaginary')
    def test_solve_linear_func_01(self):
        self.assertEqual(numworksLibs.solve_linear_func('f', 1, 2, 3), 'f(2)= 5')
    def test_solve_linear_func_02(self):
        self.assertEqual(numworksLibs.solve_linear_func('g', 23, 1, 2), 'g(1)= 25')
    def test_solve_linear_func_03(self):
        self.assertEqual(numworksLibs.solve_linear_func('a', 4, 4, 13), 'a(4)= 29')
    def test_find_dr_ordered_pair_01(self):
        self.assertEqual(numworksLibs.find_domain_range_ordered(['1', '3'], ['2', '4']), "Domain: 1, 3\nRange: 2, 4")
    def test_find_dr_ordered_pair_02(self):
        self.assertEqual(numworksLibs.find_domain_range_ordered(['1', '3', '3', '4'], ['2', '4', '2', '4']), "Domain: 1, 3, 4\nRange: 2, 4")

if __name__ == '__main__':
    unittest.main()