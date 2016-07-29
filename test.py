from hashids import Hashids
hashids = Hashids()
import random

def hasher():
    hashids = Hashids(salt='www.smokingpipes.com')
    hashid = hashids.encode(random.randint(1, 1000))
    print(hashid)

    ints = hashids.decode('mVN')
    print(ints)


import hashlib
def Pyhasher():
    mystring = input('Enter String to hash: ')
    # Assumes the default UTF-8
    hash_object = hashlib.md5(mystring.encode())
    print(hash_object.hexdigest())

hasher()
Pyhasher()
