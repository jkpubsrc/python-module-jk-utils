#!/usr/bin/env python3


import re

import jk_utils





regexStr = """
	^
	x			# letter "x"
	y			# letter "y"
	$
	"""


print(jk_utils.re.compactVerboseRegEx(regexStr))




#m = re.compile(regexStr, re.VERBOSE)

#print(m.match("xy"))


