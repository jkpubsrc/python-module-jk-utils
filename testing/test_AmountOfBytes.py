#!/usr/bin/python3


from jk_utils import AmountOfBytes
from jk_testing import Assert



"""

This program performs some tests on the implementation of AmountOfBytes.

"""



b1 = AmountOfBytes("1K")		# 1 KByte
print(repr(b1))

assert int(b1) == 1024
assert str(b1) == "1K"



b2 = AmountOfBytes("1048576")		# 1 MByte
print(repr(b2))

assert int(b2) == 1048576
assert str(b2) == "1M"



b3 = AmountOfBytes("1049600")		# 1 MByte + 1 KByte
print(repr(b3))

assert int(b3) == 1049600
assert str(b3) == "1025K"



assert b1 + b2 == b3
assert b2 + 1024 == b3
assert isinstance(b2 - b1, AmountOfBytes)
assert b2 > b1
assert b2 > 1024
assert b1 < 1025





print()
print("Success.")
print()






