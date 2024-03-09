import unittest
from demo.main import count_characters, is_leap


class TestMain(unittest.TestCase):
    def test_count_characters(self):
        # Existing test cases
        self.assertEqual(count_characters("John"), 4)
        self.assertEqual(count_characters("Doe"), 3)
        self.assertEqual(count_characters("John Doe"), 8)
        self.assertEqual(count_characters(""), 0)
        self.assertEqual(count_characters(" "), 1)
        self.assertEqual(count_characters("12345"), 5)
        self.assertEqual(count_characters("!@#$%"), 5)
        self.assertEqual(count_characters("John Doe Smith"), 14)
        self.assertEqual(count_characters("John Doe Smith Jr."), 18)
        self.assertEqual(count_characters("Hello, World!"), 13)
        self.assertEqual(count_characters("GitHub"), 6)
        self.assertEqual(count_characters("Copilot"), 7)
        self.assertEqual(count_characters("Python"), 6)
        self.assertEqual(count_characters("is"), 2)
        self.assertEqual(count_characters("awesome"), 7)
        self.assertEqual(count_characters("12345"), 5)
        self.assertEqual(count_characters("67890"), 5)
        self.assertEqual(count_characters("!@#$%"), 5)
        self.assertEqual(count_characters("^&*()"), 5)
        self.assertEqual(count_characters("Lorem"), 5)
        self.assertEqual(count_characters("ipsum"), 5)
        self.assertEqual(count_characters("dolor"), 5)
        self.assertEqual(count_characters("sit"), 3)
        self.assertEqual(count_characters("amet"), 4)
        self.assertEqual(count_characters("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(count_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(count_characters("Hello"), 5)
        self.assertEqual(count_characters("World"), 5)
        self.assertEqual(count_characters("!"), 1)
        self.assertEqual(count_characters("@"), 1)
        self.assertEqual(count_characters("#"), 1)
        self.assertEqual(count_characters("$"), 1)
        self.assertEqual(count_characters("%"), 1)
        self.assertEqual(count_characters("^"), 1)
        self.assertEqual(count_characters("&"), 1)
        self.assertEqual(count_characters("*"), 1)
        self.assertEqual(count_characters("("), 1)
        self.assertEqual(count_characters(")"), 1)
        self.assertEqual(count_characters(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit"), 55)
        self.assertEqual(count_characters(
            "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"), 72)
        self.assertEqual(count_characters("GitHub Copilot"), 14)
        self.assertEqual(count_characters("Python is awesome"), 17)
        self.assertEqual(count_characters("1234567890"), 10)
        self.assertEqual(count_characters("!@#$%^&*()"), 10)
        self.assertEqual(count_characters("Lorem ipsum dolor sit amet"), 26)
        self.assertEqual(count_characters("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(count_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_is_leap(self):
        # Leap years
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2004))
        self.assertTrue(is_leap(2008))
        self.assertTrue(is_leap(2012))
        self.assertTrue(is_leap(2016))
        self.assertTrue(is_leap(2020))
        self.assertTrue(is_leap(2024))
        self.assertTrue(is_leap(2028))
        self.assertTrue(is_leap(2032))
        self.assertTrue(is_leap(2036))
        self.assertTrue(is_leap(2040))
        self.assertTrue(is_leap(2044))
        self.assertTrue(is_leap(2048))
        self.assertTrue(is_leap(2052))
        self.assertTrue(is_leap(2056))
        self.assertTrue(is_leap(2060))
        self.assertTrue(is_leap(2064))
        self.assertTrue(is_leap(2068))
        self.assertTrue(is_leap(2072))
        self.assertTrue(is_leap(2076))
        self.assertTrue(is_leap(2080))
        self.assertTrue(is_leap(2084))
        self.assertTrue(is_leap(2088))
        self.assertTrue(is_leap(2092))
        self.assertTrue(is_leap(2096))
        # Non-leap years
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(2100))
        self.assertFalse(is_leap(2200))

    def test_empty_name(self):
        self.assertEqual(count_characters(""), 0)

    def test_single_character_name(self):
        self.assertEqual(count_characters("A"), 1)

    def test_long_name(self):
        self.assertEqual(count_characters(
            "This is a very long name with spaces and special characters like !@#$%^&*()"), 75)


if __name__ == '__main__':
    unittest.main()


    def test_leap_year(self):
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2004))
        self.assertTrue(is_leap(2008))
        self.assertTrue(is_leap(2012))
        self.assertTrue(is_leap(2016))
        self.assertTrue(is_leap(2020))
        self.assertTrue(is_leap(2024))
        self.assertTrue(is_leap(2028))
        self.assertTrue(is_leap(2032))
        self.assertTrue(is_leap(2036))
        self.assertTrue(is_leap(2040))
        self.assertTrue(is_leap(2044))
        self.assertTrue(is_leap(2048))
        self.assertTrue(is_leap(2052))
        self.assertTrue(is_leap(2056))
        self.assertTrue(is_leap(2060))
        self.assertTrue(is_leap(2064))
        self.assertTrue(is_leap(2068))
        self.assertTrue(is_leap(2072))
        self.assertTrue(is_leap(2076))
        self.assertTrue(is_leap(2080))
        self.assertTrue(is_leap(2084))
        self.assertTrue(is_leap(2088))
        self.assertTrue(is_leap(2092))
        self.assertTrue(is_leap(2096))
        # make some false assertions
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(2100))
        self.assertFalse(is_leap(2200))
        self.assertFalse(is_leap(2300))
        self.assertFalse(is_leap(2400))
        self.assertFalse(is_leap(2500))
        self.assertFalse(is_leap(2600))
        self.assertFalse(is_leap(2700))
        self.assertFalse(is_leap(2800))

    # test some limit cases
    def test_leap_year_limit(self):
        self.assertTrue(is_leap(0))
        self.assertTrue(is_leap(4))
        self.assertTrue(is_leap(8))
        self.assertTrue(is_leap(12))
        self.assertTrue(is_leap(16))
        self.assertTrue(is_leap(20))
        self.assertTrue(is_leap(24))
        self.assertTrue(is_leap(28))
        self.assertTrue(is_leap(32))
        self.assertTrue(is_leap(36))
        self.assertTrue(is_leap(40))
        self.assertTrue(is_leap(44))
        self.assertTrue(is_leap(48))
        self.assertTrue(is_leap(52))
        self.assertTrue(is_leap(56))
        self.assertTrue(is_leap(60))
        self.assertTrue(is_leap(64))
        self.assertTrue(is_leap(68))
        self.assertTrue(is_leap(72))
        self.assertTrue(is_leap(76))
        self.assertTrue(is_leap(80))
        self.assertTrue(is_leap(84))
        self.assertTrue(is_leap(88))
        self.assertTrue(is_leap(92))
        self.assertTrue(is_leap(96))


if __name__ == '__main__':
    unittest.main()
