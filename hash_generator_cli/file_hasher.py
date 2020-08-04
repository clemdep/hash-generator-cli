import hashlib
import os

class FileHasher(object):

    def __init__(self, path, hashtype):
        self.path = path
        self.file_hash = getattr(hashlib, hashtype)()

    def hasher(self):
        block_size = 262144
        with open(self.path, "rb") as file:
            fileblock = file.read(block_size)
            while len(fileblock) > 0:
                self.file_hash.update(fileblock)
                fileblock = file.read(block_size)
        return self.file_hash
