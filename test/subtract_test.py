import unittest
import coc_package


class TestSubtractFunction(unittest.TestCase):

    def test_add_for_ints(self):
        self.assertEqual(coc_package.subtract(3, 5), 3 - 5)

    def test_add_error(self):
        with self.assertRaises(AttributeError):
            coc_package.subtract(3, "5")


if __name__ == '__main__':
    unittest.main()
