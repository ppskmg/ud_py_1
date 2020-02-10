import unittest
import upper

class TestUpper(unittest.TestCase):
    def test_upper(self):
        text = "hello"
        result = upper.text_upper(text)
        self.assertEquals(result, 'HELLO')


if __name__ == '__main__':
    unittest.main()