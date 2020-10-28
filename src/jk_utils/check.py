

import typing



def allItemsHaveEqualLength(listOfSequences, expectedLength:int) -> bool:
	assert isinstance(expectedLength, int)

	it = iter(listOfSequences)
	firstLength = len(next(it))
	if not all( len(item) == firstLength for item in it ):
		return False
	return True
#










