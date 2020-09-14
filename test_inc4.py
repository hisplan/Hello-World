from unittest import TestCase, mock
import increment

class TestSimple(TestCase):

    @mock.patch("increment.randint", return_value=3)
    def test_should_increment_by_random_num(self, mock_randint):

        x = 4
        actual = increment.inc3(x)
        expected = 4 + 3

        self.assertEqual(expected, actual)

        mock_randint.assert_called()
        mock_randint.assert_called_with(1, 100)
