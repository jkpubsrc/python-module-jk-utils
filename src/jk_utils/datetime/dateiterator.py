


import datetime
import re

from .D import D












def dateRange(fromDate:D, toDate:D, includeRightBorder:bool = False):
	assert isinstance(fromDate, D)
	assert isinstance(toDate, D)
	assert isinstance(includeRightBorder, bool)

	i = fromDate.clone()
	assert isinstance(i, D)
	while i < toDate:
		yield i.clone()
		i += 1
	if i == toDate:
		if includeRightBorder:
			yield i.clone()
#








