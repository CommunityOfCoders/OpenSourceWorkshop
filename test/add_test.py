import unittest
import coc_package


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(coc_package.add(3, 5), 3 + 5)
        with self.assertRaises(AttributeError):
            coc_package.add(3, "5")


if __name__ == '__main__':
    unittest.main()
