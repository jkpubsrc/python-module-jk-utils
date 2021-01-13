#!/usr/bin/python3



import jk_utils
from jk_testing import Assert




rawSeconds = [
	3*365*24*60*60 + 5*30*24*60*60 + 2*7*24*60*60 + 2*24*60*60 + 13*60*60 + 27*60 + 5,			# 3 years +
	5*30*24*60*60 + 2*7*24*60*60 + 2*24*60*60 + 13*60*60 + 27*60 + 5,							# 5 months +
	2*7*24*60*60 + 2*24*60*60 + 13*60*60 + 27*60 + 5,											# 2 weeks +
	2*24*60*60 + 13*60*60 + 27*60 + 5,															# 2 days +
	13*60*60 + 27*60 + 5,																		# 13 hours +
	27*60 + 5,																					# 27 minutes +
	5,																							# 5 seconds
	0,
]


for rs in rawSeconds:
	print(jk_utils.duration.secondsToHRStr(rs))



