import unittest
from calculator import cal, add

class TestCalculator(unittest.TestCase):
    '''Testing the calculator'''

    def setUp(self):
        '''Set up testing objects'''
        self.a = 439
        self.b = 4

    def test_add(self):
        '''Testing add menthod'''
        calculator = cal(self.a, self.b)
        # print(calculator.add())

        self.assertEqual(calculator.add(),443)

    def test_subtract(self):
        '''Testing subtract method'''
        calculator = cal(self.a, self.b)
        self.assertEqual(calculator.sub(), 435)

        
    def test_multiply(self):
        '''Testing multiply method'''
        calculator = cal(self.a, self.b)
        self.assertEqual(calculator.mul(), 1756)

    def test_multiply(self):
        '''Testing divide method'''
        calculator = cal(self.a, self.b)
        self.assertEqual(calculator.div(), 109.75)

    # This test will fail
    # TODO: Improve the add function to ensure only array of numbers
   
    def test_add_function(self):
        self.assertEqual(add([1,2,3]), 6)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
