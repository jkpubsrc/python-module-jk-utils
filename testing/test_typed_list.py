#!/usr/bin/python3


from jk_utils.typed import TypedList
from jk_testing import Assert






listAstr = TypedList([ "a", "b", "c" ], dataType=str)
listBstr = TypedList([ "a", "b", "c" ], dataType=str)
listCint = TypedList([ 1, 2, 3 ], dataType=int)
assert isinstance(listAstr, TypedList)
assert isinstance(listBstr, TypedList)
assert isinstance(listCint, TypedList)

assert listAstr == listBstr
assert listAstr != listCint
assert listBstr != listCint
listAstr.isCompatibleCollectionE(listBstr)
assert not listAstr.isCompatibleCollection(listCint)
assert len(listAstr) == 3
assert len(listBstr) == 3

listABstr = listAstr + listBstr
assert isinstance(listABstr, TypedList)
assert id(listABstr) != id(listAstr)
assert id(listABstr) != id(listBstr)
assert len(listABstr) == 6


someStrings = [ "x", "y", "z" ]

# __add__()
z = listAstr + someStrings
assert isinstance(z, TypedList)
assert z != listAstr
assert id(z) != id(listAstr)
assert id(z) != id(someStrings)

# __radd__()
z = someStrings + listAstr
assert isinstance(z, list)					# NOTE: this can not be TypedList as the standard left hand side list.__add__() method is used here.
assert z != listAstr
assert id(z) != id(listAstr)
assert id(z) != id(someStrings)

listZstr = listAstr.clone()
assert isinstance(listZstr, TypedList)
assert listAstr == listZstr
assert id(listAstr) != id(listZstr)

# __iadd__()
listZstr += listAstr
assert isinstance(listZstr, TypedList)
assert len(listZstr) == 6
assert id(listAstr) != id(listZstr)


# __mul__()
listAAstr1 = listAstr * 2
assert isinstance(listAAstr1, TypedList)
assert listAAstr1 == (listAstr + listAstr)
assert len(listAAstr1) != len(listAstr)
assert len(listAAstr1) == 2 * len(listAstr)

# __rmul__()
listAAstr2 = 2 * listAstr
assert isinstance(listAAstr2, TypedList)
assert listAAstr2 == (listAstr + listAstr)
assert len(listAAstr2) != len(listAstr)
assert len(listAAstr2) == 2 * len(listAstr)

assert listAAstr1 == listAAstr2

# TODO: test __imul__()

# __setitem__()
try:
	listAstr[0] = 123
	raise Exception("ValueError expected!")
except TypeError:
	pass













