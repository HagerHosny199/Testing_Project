import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils as ut
class UtilsTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
        
    def test_age(self):
        #Decision Coverage criteria
        
        age = ut.age_restricted(3,5)
        self.assertEqual(age , False)
        
        age = ut.age_restricted(3,None)
        self.assertEqual(age , False)
        
        age = ut.age_restricted(None,5)
        self.assertEqual(age , False)
        
        age = ut.age_restricted(5,3)
        self.assertEqual(age , True)

    def test_format_bytes(self):
        #Branch Coverage criteria
        
        bytes_ = ut.format_bytes(None)
        self.assertEqual(bytes_ , 'N/A')

        bytes_ = ut.format_bytes('0.0')
        self.assertEqual(bytes_ , '0.00B')
        
        bytes_ = ut.format_bytes(33)
        self.assertEqual(bytes_ , '33.00B')
        

    def test_bytes_to_intlist(self):
        """Testing utils/bytes_to_intlist function
        Applying branch coverage"""
        
        """First branch: bs = None"""
        bs = None
        result = ut.bytes_to_intlist(bs)
        self.assertEqual(result, [])
        
        """Second branch: isinstance(bs[0], int) = True """        
        bs = (7).to_bytes(1, 'little')
        result = ut.bytes_to_intlist(bs)
        self.assertEqual(result, [7])
        
        """Third branch: isinstance(bs[0], int) = False"""
        bs = bytes("bytes", 'utf-8')
        result = ut.bytes_to_intlist(bs)
        self.assertEqual(result, [98, 121, 116, 101, 115])
        
if __name__ == '__main__':
    unittest.main()
