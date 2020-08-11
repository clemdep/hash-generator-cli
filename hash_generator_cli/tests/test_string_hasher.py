import string_hasher as s
import unittest
import sys
import os
testdir = os.path.dirname(__file__)
srcdir = '../lib'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))


class TestStringHasher(unittest.TestCase):

    def setUp(self):
        self.string_hasher = s.StringHasher("hello", "md5")

    def test_hasher(self):
        # TODO Testing with a variety of hashes and strings
        self.assertEqual(
            self.string_hasher.hasher(),
            "5d41402abc4b2a76b9719d911017c592")
