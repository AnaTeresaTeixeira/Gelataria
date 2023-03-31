import unittest
from iva import iva

class TestPreco(unittest.TestCase):

    def test_iva(self):
        self.assertEqual(iva(100),123)
        self.assertEqual(iva(10),12.3)
        self.assertEqual(iva('Ana'),12.3)

if __name__ == '__main__':
    unittest.main()


