#!/usr/bin/python3


import os
import time
import timeit

import jk_utils





DIRECTORY_TO_SCAN = os.path.abspath("..")











print("Scanning:", DIRECTORY_TO_SCAN)
n = jk_utils.fsutils.getFolderSize(DIRECTORY_TO_SCAN)
print(n)
print(jk_utils.formatBytes(n))

n = jk_utils.fsutils.getFolderSize(DIRECTORY_TO_SCAN, mode="exact")
print(n)
print(jk_utils.formatBytes(n))







