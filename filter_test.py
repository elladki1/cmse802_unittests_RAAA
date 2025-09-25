import unittest
from edufinder import filter_edu


class TestEduFinder(unittest.TestCase):
    def test_basic(self):
        emails = ["alice@msu.edu", "bob@gmail.com", "charlie@msu.edu"]
        self.assertEqual(filter_edu(emails), ["alice@msu.edu", "charlie@msu.edu"])

    def test_case_insensitive(self):
        emails = ["Alice@MSU.EDU", "Bob@outlook.com"]
        result = filter_edu(emails)
        self.assertIn("Alice@MSU.EDU", result)
        self.assertEqual(len(result), 1)


    def test_empty_list(self):
        self.assertEqual(filter_edu([]), [])

    def test_partial_match(self):
        emails = ["fake@msu.college", "admin@msu.ed", "student@msu.edu"]
        self.assertEqual(filter_edu(emails), ["student@msu.edu"])


    def test_fakes(self):
        emails = ["gena@harward.edu", "king@ucla.edu","sara@fsu.edu"]
        self.assertEqual(filter_edu(emails),[])
        