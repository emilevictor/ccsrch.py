from panscan import panscan, luhn
import unittest

class TestScanner(unittest.TestCase):

    def test_invalid_mastercard(self):
        text = "8293396262570410"
        self.assertEqual(panscan(text), [])

    def test_valid_mastercard(self):
        text = "5162702975322904\n"
        self.assertEqual(panscan(text), [(0, "5162702975322904")])

    def test_invalid_visa(self):
        text = "4109 4533 4898 8520\n"
        self.assertEqual(panscan(text), [])

    def test_valid_visa(self):
        text = "4109 4533 4898 8521\n"
        self.assertEqual(panscan(text), [(0, "4109 4533 4898 8521")])

    def test_valid_short_visa(self):
        text = "4410 5535 6357 5 "
        self.assertEqual(panscan(text), [(0, "4410 5535 6357 5")])

    def test_invalid_short_visa(self):
        text = "4410 5535 6357 6 "
        self.assertEqual(panscan(text), [])

    def test_valid_amex34(self):
        text = "3401 1825 3784 804 "
        self.assertEqual(panscan(text), [(0, "3401 1825 3784 804")])

    def test_invalid_amex34(self):
        text = "3401 1825 3784 805 "
        self.assertEqual(panscan(text), [])

    def test_valid_amex37(self):
        text = "3730 4625 0745 132 "
        self.assertEqual(panscan(text), [(0, "3730 4625 0745 132")])

    def test_invalid_amex37(self):
        text = "3730 4625 0745 133 "
        self.assertEqual(panscan(text), [])

    def test_valid_diners(self):
        text = "3001 7970 1170 97 "
        self.assertEqual(panscan(text), [(0, "3001 7970 1170 97")])

    def test_invalid_diners(self):
        text = "3001 7970 1170 99 "
        self.assertEqual(panscan(text), [])

    def test_invalid_jcb(self):
        text = "3096 6798 2217 1741 "
        self.assertEqual(panscan(text), [])

    def test_valid_jcb(self):
        text = "3096 6798 2217 1740 "
        self.assertEqual(panscan(text), [(0, "3096 6798 2217 1740")])

    def test_valid_jcb2(self):
        text = "2 1 3 1 1 8 0 0 0 4 0 8 5 6 0 "
        self.assertEqual(panscan(text), [(0, "2 1 3 1 1 8 0 0 0 4 0 8 5 6 0")])

    def test_invalid_jcb2(self):
        text = "213118001438560 "
        self.assertEqual(panscan(text), [])

    def test_no_numbers(self):
        text = "wiubfoiranvquwrhruehig uhegw\nweowiuhwfe  weoif$%&wgoirgh\n"
        self.assertEqual(panscan(text), [])

    def test_all_numbers(self):
        text = "11238947524713897214 128951673475 435413  483576107"
        self.assertEqual(panscan(text), [])

    def test_multi(self):
        text = "aio blah blah  $$%^q 32 5432 3096 6798 2217 1740 \n"
        text += "CCNO: 4109 4533 4898 8521\n"
        text += "MY PAN%5162702975322904\n"
        self.assertEqual(panscan(text), [(29, "3096 6798 2217 1740"),
                                        (56, "4109 4533 4898 8521"),
                                        (83, "5162702975322904")])

    def test_valids(self):
        self.assertTrue(luhn("8293396262570410"))
        self.assertTrue(luhn("3508781513840310"))
        self.assertTrue(luhn("8407935923147325"))
        self.assertTrue(luhn("6868812170619338"))
        self.assertTrue(luhn("3809258669796865"))

    def test_invalids(self):
        self.assertFalse(luhn("5112345678912340"))
        self.assertFalse(luhn("5512345678912390"))
        self.assertFalse(luhn("30012345678903"))
        self.assertFalse(luhn("213118001438560"))

    def test_weirdos(self):
        self.assertFalse(luhn("word"))
        self.assertFalse(luhn("1234sdf45456cvbn567ivb6789o"))
        self.assertFalse(luhn(""))
        self.assertFalse(luhn("  123  4455 222  555"))

if __name__=="__main__":
    unittest.main()
