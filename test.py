import unittest
from unittest import result

from main import rep

class TestListaDiccionario(unittest.TestCase):

    def test_1(self):

        salida =  rep([0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(salida, {0:10})

    def test_2(self):

        self.assertEqual(rep([9,7,8,6,5,5,1,4,7,0]),{9:1,7:2,8:1,6:1,5:2,1:1,4:1,0:1})
    
    def test_3(self):

        self.assertEqual(rep([1,2,3,4,5,6,7,8,9]),{1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1})

    def test_4(self):

        self.assertEqual(rep([2,4,6,8]),{2:1,4:1,6:1,8:1})

if __name__=='__main__':
    unittest.main()