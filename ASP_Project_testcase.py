import unittest
import Project as crt

class TestMyProgram(unittest.TestCase):
    def test_Equal(self):
        g = crt.Country()
        print(g.findTop3())
        self.assertEqual(g.findTop3(), [' Japan ' ,  ' Taiwan ', ' Hong Kong '])

    def test_False(self):
        h = crt.Country()
        k = h.findTop3()
        self.assertFalse(' USA' in  k, False)

if __name__=='__main__':
    unittest.main()