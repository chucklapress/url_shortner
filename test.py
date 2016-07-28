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
    hashid = hashids.encode(random.randint(1, 10))
    print(hashid)

    ints = hashids.decode('V6')
    print(ints)

hasher()
