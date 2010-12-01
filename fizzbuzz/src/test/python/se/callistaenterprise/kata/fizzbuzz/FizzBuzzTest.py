# Module FizzBuzzTest

import unittest
from se.callistaenterprise.kata.fizzbuzz.FizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    fizzbuzz = FizzBuzz()

    tuple_of_1_2 = (1, 2)
    tuple_of_2_fizz = (2, "Fizz")
    tuple_of_fizz_7_8_fizz = ("Fizz", 7, 8, "Fizz")
    tuple_of_buzz = ("Buzz",)
    tuple_of_fizzbuzz = ("FizzBuzz",)
    tuple_of_15_to_30 = ("FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, "Fizz", "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz")
    tuple_of_31_to_40 = ("Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz", "Fizz", "Fizz", "Fizz", "Fizz", "Buzz")
    tuple_of_41_to_50 = (41, "Fizz", "Fizz", 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz")
    tuple_of_51_to_60 = ("FizzBuzz", "Buzz", "FizzBuzz", "FizzBuzz", "Buzz", "Buzz", "FizzBuzz", "Buzz", "Buzz", "FizzBuzz")
    tuple_of_61_to_70 = (61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz")
    tuple_of_71_to_80 = (71, "Fizz", "Fizz", 74, "FizzBuzz", 76, 77, "Fizz", 79, "Buzz")
    tuple_of_81_to_90 = ("Fizz", 82, "Fizz", "Fizz", "Buzz", 86, "Fizz", 88, 89, "FizzBuzz")
    tuple_of_91_to_100 = (91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz")

    list_1_100 = range(1,101)

    def testReturn1And2AsIs(self):
        self.assertEqual(list(self.tuple_of_1_2), self.fizzbuzz.filter(self.list_1_100[0:2]))

    def testConvert3ToFizz(self):
        self.assertEqual(list(self.tuple_of_2_fizz), self.fizzbuzz.filter(self.list_1_100[1:3]))

    def testConvert6And9ToFizz(self):
        self.assertEqual(list(self.tuple_of_fizz_7_8_fizz), self.fizzbuzz.filter(self.list_1_100[5:9]))

    def testConvert5ToBuzz(self):
        self.assertEqual(list(self.tuple_of_buzz), self.fizzbuzz.filter(self.list_1_100[4:5]))

    def testConvert15ToFizzBuzz(self):
        self.assertEqual(list(self.tuple_of_fizzbuzz), self.fizzbuzz.filter(self.list_1_100[14:15]))

    def testConvert15To30Correctly(self):
        self.assertEqual(list(self.tuple_of_15_to_30), self.fizzbuzz.filter(self.list_1_100[14:30]))

    def testConvert31To40Correctly(self):
        self.assertEqual(list(self.tuple_of_31_to_40), self.fizzbuzz.filter(self.list_1_100[30:40]))

    def testConvert41To50Correctly(self):
        self.assertEqual(list(self.tuple_of_41_to_50), self.fizzbuzz.filter(self.list_1_100[40:50]))

    def testConvert51To60Correctly(self):
        self.assertEqual(list(self.tuple_of_51_to_60), self.fizzbuzz.filter(self.list_1_100[50:60]))

    def testConvert61To70Correctly(self):
        self.assertEqual(list(self.tuple_of_61_to_70), self.fizzbuzz.filter(self.list_1_100[60:70]))

    def testConvert71To80Correctly(self):
        self.assertEqual(list(self.tuple_of_71_to_80), self.fizzbuzz.filter(self.list_1_100[70:80]))

    def testConvert81To90Correctly(self):
        self.assertEqual(list(self.tuple_of_81_to_90), self.fizzbuzz.filter(self.list_1_100[80:90]))

    def testConvert71To80Correctly(self):
        self.assertEqual(list(self.tuple_of_91_to_100), self.fizzbuzz.filter(self.list_1_100[90:100]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FizzBuzzTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
