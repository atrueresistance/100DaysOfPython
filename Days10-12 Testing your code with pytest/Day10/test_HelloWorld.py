import unittest
from HelloWorldTest import hello_name


class TestHello(unittest.TestCase):
    
    def test_hello_name(self):
        self.assertEqual(hello_name('bob'), 'Hello bob')

if __name__ == '__main__':
    unittest.main()