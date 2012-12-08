#!/usr/bin/env python
import bcrypt
import sys
from Crypto.Hash import MD5

def main(args):
    '''Take in a bunch of strings, and hash the shit out of them'''
    for a in args:
        print bcrypt.hashpw(a, bcrypt.gensalt())
        print MD5.new(a).hexdigest()

if __name__ == '__main__':
    main(sys.argv[1:])
