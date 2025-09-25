# Unit test for extract_emails() function
import unittest
from extract import extract_emails
import re # for re.findall

class TestEmailExtract(unittest.TestCase):
  def test_duplicates(self):
    # Test whether duplicate emails will be removed
    html = "Email: test@example.com, test@example.com"
    result = extract_emails(html)
    self.assertEqual(result, ["test@example.com"])

  def test_no_emails(self):
    # Test whether an empty list is returned if no emails are found
    html = "No emails here!"
    result = extract_emails(html)
    self.assertEqual(result, [])

  def test_uppercase(self):
    # Test whether emails including uppercase letters are returned
    html = "USER@Example.COM"
    result = extract_emails(html)
    self.assertEqual(result, ["USER@Example.COM"])

  def test_invalid_email(self):
    # Test whether invalid emails are returned 
    html = "Not an email: user@com"
    result = extract_emails(html)
    self.assertEqual(result, [])

