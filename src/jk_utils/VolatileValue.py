

import time



class VolatileValue(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, valueProviderCallback, keepSeconds:int):
		assert callable(valueProviderCallback)
		assert isinstance(keepSeconds, int)

		self.__keepSeconds = keepSeconds
		self.__valueProviderCallback = valueProviderCallback
		self.__value = None
		self.__t = 0
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def value(self):
		t = time.time()
		if (t - self.__t > self.__keepSeconds):
			self.__value = self.__valueProviderCallback()
			self.__t = t
		return self.__value
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def invalidate(self):
		self.__value = None
		self.__t = 0
	#

#














