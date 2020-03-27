import unittest
import SPD1i2i3 as rpq


class TestRPQ1(unittest.TestCase):

    def setUp(self):
        self.zadania = rpq.loadData("data/data100.txt")

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 3936)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 3936)


if __name__ == '__main__':
    unittest.main()