#!/usr/bin/python3


import time

from jk_utils import TimeStamp
from jk_testing import Assert



"""

This program performs some tests on the implementation of TimeStamp.

"""



t1 = TimeStamp.now()
print(t1)

time.sleep(1)

t2 = TimeStamp.now()
print(t2)

fDiff = t2 - t1
print(fDiff)
assert isinstance(fDiff, float)
assert 1 <= fDiff <= 2

t3 = t1 + 1
print(t3)
assert isinstance(t3, TimeStamp)
fDiff = t2 - t3
print(fDiff)
assert isinstance(fDiff, float)
assert 0 <= fDiff <= 1

assert t3 > 0

t4 = TimeStamp(0)
assert t4 == 0









