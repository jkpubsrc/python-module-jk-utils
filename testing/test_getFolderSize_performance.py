#!/usr/bin/python3


import os
import time
import timeit

import jk_utils





DIRECTORY_TO_SCAN = os.path.abspath("..")

NUMBER_OF_REPEATS = 200







def avg(arr) -> float:
	return sum(arr) / len(arr)
#




print("Measuring variant 1 ...")
vals1 = []
for i in range(0, NUMBER_OF_REPEATS):
	t = time.time()
	jk_utils.fsutils.__old_getFolderSize(DIRECTORY_TO_SCAN)
	duration = time.time() - t
	if i > 0:
		vals1.append(duration)

print("Measuring variant 2 ...")
vals2 = []
for i in range(0, NUMBER_OF_REPEATS):
	t = time.time()
	jk_utils.fsutils.getFolderSize(DIRECTORY_TO_SCAN)
	duration = time.time() - t
	if i > 0:
		vals2.append(duration)

print("Measuring variant 2 using timeit ...")
duration2timeit = timeit.timeit(stmt=lambda: jk_utils.fsutils.getFolderSize(DIRECTORY_TO_SCAN), number=NUMBER_OF_REPEATS) / NUMBER_OF_REPEATS

print("Variant 1:", round(avg(vals1) * 1000, 6), "ms")
print("Variant 2:", round(avg(vals2) * 1000, 6), "ms")
print("Variant 2 timeit:", round(duration2timeit * 1000, 6), "ms")




"""
Typical results:

Measuring variant 1 ...
Measuring variant 2 ...
Measuring variant 2 using timeit ...
Variant 1: 8.257395 ms
Variant 2: 4.799469 ms
Variant 2 timeit: 4.815246 ms
"""












