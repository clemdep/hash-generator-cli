import sys
import os
import argparse

import hashlib

from . import string_hasher as s
from . import file_hasher as f

def run():
    parser = argparse.ArgumentParser(prog="hasher",
                                     usage="%(prog)s [options] path",
                                     description="Computes the hash of a string or a file")
    parser.add_argument("Path",
                        metavar="path",
                        type=str,
                        help="the path to the file or string to hash")
    parser.add_argument("Hash",
                        metavar="hash",
                        type=str,
                        help=f"hash to use among {hashlib.algorithms_guaranteed}")
    args = parser.parse_args()

    fileflag = False
    if os.path.exists(args.Path):
        fileflag = True

    if fileflag:
        hashed_file = f.FileHasher(args.Path, args.Hash)
        final_hash = hashed_file.hasher()

    else:
        hashed_string = s.StringHasher(args.Path, args.Hash)
        final_hash = hashed_string.hasher()

    print(final_hash)
