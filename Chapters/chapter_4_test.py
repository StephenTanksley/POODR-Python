import unittest
from chapter_4 import Customer, Trip, Bicycle

"""
    I have three classes in this chapter which need to be tested. 
    1) Customer
        a) 
    2) Trip
    3) Bicycle


"""


class CustomerTests(unittest.TestCase):

    def setUp(self):
        self.moe = Customer('01/01/2021', 'Easy', True)

    def tearDown(self):
        del self.moe

    def test_customer_attributes(self):
        self.assertEqual(len(self.moe.__dict__), 3)
        self.assertTrue(hasattr(self.moe, "date"))
        self.assertTrue(hasattr(self.moe, "difficulty"))
        self.assertTrue(hasattr(self.moe, "need_bike"))
        self.assertFalse(hasattr(self.moe, "trips"))

    def test_attribute_values(self):
        self.assertEqual(self.moe.date, '01/01/2021')
        self.assertEqual(self.moe.difficulty, 'Easy')
        self.assertEqual(self.moe.need_bike, True)


# if __name__ == 'main':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
if __name__ == '__main__':
    unittest.main()
