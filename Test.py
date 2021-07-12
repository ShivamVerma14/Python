# Python program illustrating test cases checking using Unittest

import unittest
import Cap

class Test(unittest.TestCase):

    def test_one(self):
        text = 'python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two(self):
        text = 'shivam verma'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Shivam Verma')

if __name__ == '__main__':
    unittest.main()