from hashids import Hashids
hashids = Hashids()
import random

def hasher():
    #hashid = hashids.encode(123)
    #print(hashid)

    #ints = hashids.decode('xoz')
    #print(ints)

    #hashid = hashids.encode(8675309)
    #print(hashid)

    #ints = hashids.decode('r0BL02')
    #print(ints)

    hashids = Hashids(salt='user input is junk')
    hashid = hashids.encode(random.randint(1, 100))
    print(hashid)

    ints = hashids.decode('b7g')
    print(ints)


import hashlib
def Pyhasher():
    mystring = input('Enter String to hash: ')
    # Assumes the default UTF-8
    hash_object = hashlib.md5(mystring.encode())
    print(hash_object.hexdigest())
    

Pyhasher()
