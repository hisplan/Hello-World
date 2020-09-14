from unittest import TestCase
import increment

class TestSimple(TestCase):

    def test_should_increment_by_2(self):

        x = 4
        n = 3
        actual = increment.inc2(x, n)

        self.assertEqual(x + n, actual)
        
