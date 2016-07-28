from hashids import Hashids


def hasher():
    #hashid = hashids.encode(123)
    #print(hashid)

    #ints = hashids.decode('xoz')
    #print(ints)

    #hashid = hashids.encode(8675309)
    #print(hashid)

    #ints = hashids.decode('r0BL02')
    #print(ints)

    hashids = Hashids(salt='user input is junk 1')
    hashid = hashids.encode(123997)
    print(hashid)

    ints = hashids.decode('y8ALv')
    print(ints)

hasher()
