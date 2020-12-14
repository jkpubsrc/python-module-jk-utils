#!/usr/bin/python3


from jk_utils import Bytes
from jk_testing import Assert



"""

This program performs some tests on the implementation of Bytes.

"""



b1 = Bytes("0022446688a0c0e0")
print(repr(b1))

b2 = Bytes("0022446688a0c0e0")
assert id(b1) != id(b2)

assert len(b1) == len(b2)
assert b1 == b2

b3 = b1 + b2
print(b3)

bb1 = bytes(b1)
assert isinstance(bb1, bytes)

bb2 = bytes(b2)
assert isinstance(bb2, bytes)

assert bb1 == bb2
assert bb1 == b1
assert bb1 == b2
assert bb2 == b1
assert bb2 == b2



c1 = Bytes(bb1)

assert c1 == bb1
assert c1 == b1









print()
print("Success.")
print()






