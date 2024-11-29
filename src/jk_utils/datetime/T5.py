

import re
import datetime






#
# This class represents a time value with 5 minutes accuracy.
#
class T5(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self):
		self._hour = 0
		self._minute = 0
		self._minuteTick = 0
		self._absoluteTick = 0
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def hour(self) -> int:
		return self._hour
	#

	@property
	def minute(self) -> int:
		return self._minute
	#

	@property
	def hourMinute(self) -> int:
		return self._hour * 100 + self._minute
	#

	@property
	def minuteTick(self) -> int:
		return self._minuteTick
	#

	@property
	def absoluteTick(self) -> int:
		return self._absoluteTick
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def clone(self):
		ret = T5()
		ret._hour = self._hour
		ret._minute = self._minute
		ret._minuteTick = self._minuteTick
		ret._absoluteTick = self._absoluteTick
		return ret
	#

	################################################################################################################################
	## Special Methods
	################################################################################################################################

	def __str__(self):
		return "{:02d}:{:02d}".format(self._hour, self._minute)
	#

	def __repr__(self):
		return "{:02d}:{:02d}".format(self._hour, self._minute)
	#

	################################################################################################################################
	## Operator Methods
	################################################################################################################################

	def __bool__(self):
		return self._absoluteTick != 0
	#

	def __eq__(self, other):
		if isinstance(other, T5):
			return self._absoluteTick == other._absoluteTick
		else:
			return False
	#

	def __ne__(self, other):
		if isinstance(other, T5):
			return self._absoluteTick != other._absoluteTick
		else:
			return True
	#

	def __ge__(self, other):
		assert isinstance(other, T5)
		return self._absoluteTick >= other._absoluteTick
	#

	def __gt__(self, other):
		assert isinstance(other, T5)
		return self._absoluteTick > other._absoluteTick
	#

	def __le__(self, other):
		assert isinstance(other, T5)
		return self._absoluteTick <= other._absoluteTick
	#

	def __lt__(self, other):
		assert isinstance(other, T5)
		return self._absoluteTick < other._absoluteTick
	#

	def __iadd__(self, other):
		if isinstance(other, int):
			self._absoluteTick += other
		elif isinstance(other, T5):
			self._absoluteTick += other._absoluteTick
		else:
			raise Exception(str(type(other)))
		self._hour = self._absoluteTick // 12
		self._minuteTick = self._absoluteTick % 12
		self._minute = self._minuteTick * 5
		return self
	#

	def __isub__(self, other):
		if isinstance(other, int):
			self._absoluteTick -= other
		elif isinstance(other, T5):
			self._absoluteTick -= other._absoluteTick
		else:
			raise Exception(str(type(other)))
		self._hour = self._absoluteTick // 12
		self._minuteTick = self._absoluteTick % 12
		self._minute = self._minuteTick * 5
		return self
	#

	def __add__(self, other):
		if isinstance(other, int):
			return T5.createFromAbsoluteTick(self._absoluteTick + other)
		elif isinstance(other, T5):
			return T5.createFromAbsoluteTick(self._absoluteTick + other._absoluteTick)
		else:
			raise Exception(str(type(other)))
	#

	def __sub__(self, other):
		if isinstance(other, int):
			return T5.createFromAbsoluteTick(self._absoluteTick - other)
		elif isinstance(other, T5):
			return T5.createFromAbsoluteTick(self._absoluteTick - other._absoluteTick)
		else:
			raise Exception(str(type(other)))
	#

	def __int__(self):
		return self._absoluteTick
	#

	################################################################################################################################
	## Static Methods
	################################################################################################################################

	@staticmethod
	def createFromTime(hour:int, minute:int):
		assert isinstance(hour, int)
		assert isinstance(minute, int)

		ret = T5()
		ret._hour = hour
		ret._minute = minute
		ret._minuteTick = ret._minute // 5
		ret._absoluteTick = ret._hour * 12 + ret._minuteTick
		return ret
	#

	@staticmethod
	def createFromAbsoluteTick(absoluteTick:int):
		assert isinstance(absoluteTick, int)

		ret = T5()
		ret._hour = absoluteTick // 12
		ret._minuteTick = absoluteTick % 12
		ret._minute = ret._minuteTick * 5
		ret._absoluteTick = absoluteTick
		return ret
	#

	@staticmethod
	def createFromHourMinutes(hourMinutes:int):
		assert isinstance(hourMinutes, int)

		ret = T5()
		ret._hour = hourMinutes // 100
		ret._minute = hourMinutes % 100
		if (ret._hour < 0) or (ret._hour > 23) or (ret._minute < 0) or (ret._minute > 59):
			raise Exception("Invalid time!")
		ret._minuteTick = ret._minute // 5
		ret._absoluteTick = ret._hour * 12 + ret._minuteTick
		return ret
	#

	@staticmethod
	def now():
		dt = datetime.datetime.now()

		ret = T5()
		ret._hour = dt.hour
		ret._minute = dt.minute
		ret._minuteTick = ret._minute // 5
		ret._absoluteTick = ret._hour * 12 + ret._minuteTick
		return ret
	#

#




