from unittest import TestCase
import increment


class TestSimple(TestCase):

    def setUp(self):
        with open("data.txt", "rt") as fin:
            self.x = int(fin.read())

    def tearDown(self):
        pass

    def test_should_increment_by_2(self):

        actual = increment.inc1(self.x)

        self.assertEqual(self.x + 1, actual)

    def test_should_increment2_by_2(self):
        actual = increment.inc1(self.x)

        self.assertEqual(self.x + 1, actual)