#!/usr/bin/python3




class ObservableEvent(object):

	def __init__(self, name:str = None, bCatchExceptions:bool = False):
		self.__name = name
		self.__listeners = tuple()
		self.__bCatchExceptions = bCatchExceptions
	#

	@property
	def catchExceptions(self):
		return self.__bCatchExceptions
	#

	@property
	def name(self):
		return self.__name
	#

	@property
	def listeners(self):
		return self.__listeners
	#

	def __len__(self):
		return len(self.__listeners)
	#

	def removeAllListeners(self):
		self.__listeners = tuple()
	#

	def __str__(self):
		if self.__name:
			ret = repr(self.__name)[1:][:-1] + "("
		else:
			ret = "Event("
		if len(self.__listeners) == 0:
			ret += "no listener)"
		elif len(self.__listeners) == 1:
			ret += "1 listener)"
		else:
			ret += str(len(self.__listeners)) + " listeners)"
		return ret
	#

	def __repr__(self):
		if self.__name:
			ret = repr(self.__name)[1:][:-1] + "("
		else:
			ret = "Event("
		if len(self.__listeners) == 0:
			ret += "no listener)"
		elif len(self.__listeners) == 1:
			ret += "1 listener)"
		else:
			ret += str(len(self.__listeners)) + " listeners)"
		return ret
	#

	def add(self, theCallable:callable):
		assert theCallable != None
		self.__listeners += (theCallable,)
		return self
	#

	def __iadd__(self, theCallable:callable):
		assert theCallable != None
		self.__listeners += (theCallable,)
		return self
	#

	def remove(self, theCallable:callable) -> bool:
		assert theCallable != None
		if theCallable in self.__listeners:
			n = self.__listeners.index(theCallable)
			self.__listeners = self.__listeners[:n] + self.__listeners[n + 1:]
			return True
		else:
			return False
	#

	def __isub__(self, theCallable:callable):
		assert theCallable != None
		if theCallable in self.__listeners:
			n = self.__listeners.index(theCallable)
			self.__listeners = self.__listeners[:n] + self.__listeners[n + 1:]
			return True
		else:
			return False
	#

	def __call__(self, *argv, **kwargs):
		if self.__bCatchExceptions:
			try:
				for listener in self.__listeners:
					listener(*argv, **kwargs)
			except Exception as ee:
				pass
		else:
			for listener in self.__listeners:
				listener(*argv, **kwargs)
	#

	def fire(self, *argv, **kwargs):
		if self.__bCatchExceptions:
			try:
				for listener in self.__listeners:
					listener(*argv, **kwargs)
			except Exception as ee:
				pass
		else:
			for listener in self.__listeners:
				listener(*argv, **kwargs)
	#

#
