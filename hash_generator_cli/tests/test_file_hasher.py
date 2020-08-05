import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../lib'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import file_hasher as f

class TestFileHasher(unittest.TestCase):

    def setUp(self):
        self.file_hasher = f.FileHasher("./test_file.txt", "sha1")
    
    def test_file_hasher(self):
        self.assertEqual(self.file_hasher.hasher(), "da39a3ee5e6b4b0d3255bfef95601890afd80709")

