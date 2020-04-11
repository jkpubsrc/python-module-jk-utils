

def _fullname(o):
	module = o.__class__.__module__
	if module is None or module == str.__class__.__module__:
		return o.__class__.__name__		# Avoid reporting __builtin__
	else:
		#items = module.split(".")
		#if items[-1] == o.__class__.__name__:
		#	return module
		#else:
		#	return module + '.' + o.__class__.__name__
		return module + '.' + o.__class__.__name__
#




def getTypeAsStr(value, fqn:bool = False):
	assert isinstance(fqn, bool)

	if isinstance(value, bool):
		return "bool"

	if isinstance(value, int):
		return "int"

	if isinstance(value, float):
		return "float"

	if isinstance(value, str):
		return "str"

	if isinstance(value, (list, tuple)):
		assert len(value) > 0

		elementType = None
		firstValue = None
		for v in value:
			if elementType is None:
				elementType = type(v)
				firstValue = v
			else:
				assert elementType == type(v)

		return getTypeAsStr(v, fqn) + "[]"

	if isinstance(value, dict):
		assert len(value) > 0
		keyType = None
		elementType = None
		firstKey = None
		firstValue = None
		for k in value.keys():
			assert isinstance(k, str)
			v = value[k]
			if elementType is None:
				keyType = type(k)
				firstKey = k
				elementType = type(v)
				firstValue = v
			else:
				assert keyType == type(k)
				assert elementType == type(v)
		return "dict<" + getTypeAsStr(firstKey, fqn) + "," + getTypeAsStr(firstValue, fqn) + ">"

	if fqn:
		s = _fullname(value)
	else:
		s = value.__class__.__name__
		pos = s.rfind(".")
		if pos:
			s = s[pos + 1:]
	return s
#




