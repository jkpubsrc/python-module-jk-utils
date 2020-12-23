


import typing
import re





#
# This class represents a specific amount of bytes.
#
class AmountOfBytes(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, value):
		self.__n = AmountOfBytes.__parseBytesFromStr(value)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __repr__(self):
		return "AmountOfBytes<(" + AmountOfBytes.__bytesToStr(self.__n) + ")>"
	#

	def __str__(self):
		return AmountOfBytes.__bytesToStr(self.__n)
	#

	def __int__(self):
		return self.__n
	#

	def __add__(self, other):
		if isinstance(other, AmountOfBytes):
			return AmountOfBytes(self.__n + other.__n)
		elif isinstance(other, int):
			return AmountOfBytes(self.__n + other)
		elif isinstance(other, float):
			return self.__n + other
		else:
			raise TypeError(repr(other))
	#

	def __sub__(self, other):
		if isinstance(other, AmountOfBytes):
			return AmountOfBytes(self.__n - other.__n)
		elif isinstance(other, int):
			return AmountOfBytes(self.__n - other)
		elif isinstance(other, float):
			return self.__n - other
		else:
			raise TypeError(repr(other))
	#

	def __mul__(self, other):
		if isinstance(other, AmountOfBytes):
			raise TypeError(repr(other))
		elif isinstance(other, int):
			return AmountOfBytes(self.__n * other)
		elif isinstance(other, float):
			return self.__n * other
		else:
			raise TypeError(repr(other))
	#

	def __div__(self, other):
		if isinstance(other, AmountOfBytes):
			raise TypeError(repr(other))
		elif isinstance(other, int):
			return self.__n / other
		elif isinstance(other, float):
			return self.__n / other
		else:
			raise TypeError(repr(other))
	#

	def __eq__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n == other.__n
		elif isinstance(other, int):
			return self.__n == other
		else:
			return False
	#

	def __ne__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n != other.__n
		elif isinstance(other, int):
			return self.__n != other
		else:
			return False
	#

	def __gt__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n > other.__n
		elif isinstance(other, (int, float)):
			return self.__n > other
		else:
			return False
	#

	def __ge__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n >= other.__n
		elif isinstance(other, (int, float)):
			return self.__n >= other
		else:
			return False
	#

	def __lt__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n < other.__n
		elif isinstance(other, (int, float)):
			return self.__n < other
		else:
			return False
	#

	def __le__(self, other):
		if isinstance(other, AmountOfBytes):
			return self.__n <= other.__n
		elif isinstance(other, (int, float)):
			return self.__n <= other
		else:
			return False
	#

	################################################################################################################################
	## Static Helper Methods
	################################################################################################################################

	@staticmethod
	def __parseBytesFromStr(v:typing.Union[int,str]) -> int:
		if isinstance(v, int):
			assert v >= 0
			return v

		vText = v.strip().upper()

		m = re.match("^([0-9.]+)\s*([KMGT]B?)$", vText)
		if m:
			try:
				n = float(m.group(1))
			except:
				raise Exception("Value does not specify bytes: " + repr(vText))

			sFactor = m.group(2)
			if sFactor.startswith("K"):
				n *= 1024
			elif sFactor.startswith("M"):
				n *= 1024*1024
			elif sFactor.startswith("G"):
				n *= 1024*1024*1024
			elif sFactor.startswith("T"):
				n *= 1024*1024*1024*1024
			else:
				pass

			return int(n)

		else:
			try:
				return int(vText)
			except Exception as ee:
				raise Exception("Value does not specify bytes: " + repr(vText))
	#

	@staticmethod
	def __bytesToStr(n:int) -> str:
		if (n >= 1024*1024*1024*1024) and ((n % (1024*1024*1024*1024)) == 0):
			return str(n // (1024*1024*1024*1024)) + "T"
		elif (n >= 1024*1024*1024) and ((n % (1024*1024*1024)) == 0):
			return str(n // (1024*1024*1024)) + "G"
		elif (n >= 1024*1024) and ((n % (1024*1024)) == 0):
			return str(n // (1024*1024)) + "M"
		elif (n >= 1024) and ((n % 1024) == 0):
			return str(n // 1024) + "K"
		else:
			return str(n)
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

	@staticmethod
	def parseFromStr(v:str):
		assert isinstance(v, str)
		return AmountOfBytes(v)
	#

	@staticmethod
	def parse(v:typing.Union[int,str]):
		assert isinstance(v, (int,str))
		return AmountOfBytes(v)
	#

#














