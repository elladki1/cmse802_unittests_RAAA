# load_html_test.py
import unittest
from html import load_html

class LoadHtmlTests(unittest.TestCase):

    def test_fetch_valid_page(self):
        page = load_html("https://cal.msu.edu/contact-us/deans-office-directory/")
        self.assertIsNotNone(page)
        self.assertTrue(len(page) > 0)

    def test_fetch_invalid_page(self):
        content = load_html("http://abcd.not.real")
        self.assertIsNone(content)

if __name__ == "__main__":
    unittest.main()
