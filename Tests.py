import unittest
import SPD1i2i3 as rpq


class TestRPQ_data10(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data10.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 927)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 746)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 746)

class TestRPQ_data20(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data20.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 1905)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 1594)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 1594)

class TestRPQ_data50(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data50.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 2843)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 1915)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 1915)

class TestRPQ_data100(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data100.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 5324)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 3936)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 3936)

class TestRPQ_data200(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data200.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 11109)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 8210)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 8210)

class TestRPQ_data500(unittest.TestCase):
    def setUp(self):
        self.zadania = rpq.loadData("data/data500.txt")

    def test_1234(self):
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 26706)

    def test_sortR(self):
        rpq.sortR(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 19609)

    def test_sortRQ(self):
        rpq.sortRQ(self.zadania)
        self.assertEqual(rpq.calculate_Cmax(self.zadania), 19609)



# ----- Main ----- #
if __name__ == '__main__':
    unittest.main()