import hashlib


class StringHasher(object):
    
    def __init__(self, string_, hashtype):
        self.string_ = string_
        self.hashtype = hashtype

    def encoder(self):
        return self.string_.encode("utf-8")

    def hasher(self):
        try:
            return getattr(hashlib, self.hashtype)(self.encoder())
        except:
            raise AttributeError(f"Please provide a valid hash. \n Valid hashes are: {hashlib.algorithms_available}")
            



