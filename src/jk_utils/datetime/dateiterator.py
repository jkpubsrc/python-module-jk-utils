


import datetime





class D(object):

	def __init__(self):
		self._dt = None
	#

	@property
	def ts(self) -> int:
		return int(self._dt.timestamp())
	#

	@property
	def year(self) -> int:
		return self._dt.year
	#

	@property
	def month(self) -> int:
		return self._dt.month
	#

	@property
	def day(self) -> int:
		return self._dt.day
	#

	@property
	def dayOfWeek(self) -> int:
		return self._dt.weekday()
	#

	@staticmethod
	def now():
		ret = D()
		dt = datetime.datetime.now()
		y = dt.year
		m = dt.month
		d = dt.day
		ret._dt = datetime.datetime(y, m, d)
		return ret
	#

	def __str__(self):
		return "{:04d}-{:02d}-{:02d}".format(self._dt.year, self._dt.month, self._dt.day)
	#

	def __repr__(self):
		return "{:04d}-{:02d}-{:02d}".format(self._dt.year, self._dt.month, self._dt.day)
	#

	def clone(self):
		ret = D()
		ret._dt = self._dt
		return ret
	#

	def __eq__(self, other):
		if isinstance(other, D):
			return self._dt == other._dt
		else:
			return False
	#

	def __ne__(self, other):
		if isinstance(other, D):
			return self._dt != other._dt
		else:
			return True
	#

	def __ge__(self, other):
		assert isinstance(other, D)
		return self._dt >= other._dt
	#

	def __gt__(self, other):
		assert isinstance(other, D)
		return self._dt > other._dt
	#

	def __le__(self, other):
		assert isinstance(other, D)
		return self._dt <= other._dt
	#

	def __lt__(self, other):
		assert isinstance(other, D)
		return self._dt < other._dt
	#

	def startOfWeek(self):
		wd = self._dt.weekday()
		dt = self._dt.timestamp() - 24*60*60*wd
		d = D()
		d._dt = datetime.datetime.fromtimestamp(dt)
		return d
	#

	def nextWeek(self):
		wd = self._dt.weekday()
		dt = self._dt.timestamp() - 24*60*60*wd
		d = D()
		d._dt = datetime.datetime.fromtimestamp(dt + 7 *24*60*60)
		return d
	#

	def previousWeek(self):
		wd = self._dt.weekday()
		dt = self._dt.timestamp() - 24*60*60*wd
		d = D()
		d._dt = datetime.datetime.fromtimestamp(dt - 7 *24*60*60)
		return d
	#

	def nextDay(self):
		d = D()
		d._dt = datetime.datetime.fromtimestamp(self._dt.timestamp() + 24*60*60)
		return d
	#

	def previousDay(self):
		d = D()
		d._dt = datetime.datetime.fromtimestamp(self._dt.timestamp() - 24*60*60)
		return d
	#

	def __add__(self, other):
		if isinstance(other, int):
			return datetime.datetime.fromtimestamp(self._dt.timestamp() + 24*60*60*other)
		else:
			raise Exception(str(type(other)))
	#

	def __iadd__(self, other):
		if isinstance(other, int):
			self._dt = datetime.datetime.fromtimestamp(self._dt.timestamp() + 24*60*60*other)
			return self
		else:
			raise Exception(str(type(other)))
	#

	def __sub__(self, other):
		if isinstance(other, D):
			return int((self._dt.timestamp() - other._dt.timestamp()) / (24*60*60))
		elif isinstance(other, int):
			return datetime.datetime.fromtimestamp(self._dt.timestamp() - 24*60*60*other)
		else:
			raise Exception(str(type(other)))
	#

	def __isub__(self, other):
		if isinstance(other, int):
			self._dt = datetime.datetime.fromtimestamp(self._dt.timestamp() - 24*60*60*other)
			return self
		else:
			raise Exception(str(type(other)))
	#

	def __int__(self):
		return int(self._dt.timestamp())
	#

	def __float__(self):
		return self._dt.timestamp()
	#

	@property
	def yearMonthDay(self) -> int:
		return self._dt.year * 10000 + self._dt.month * 100 + self._dt.day
	#

	@property
	def yearMonth(self) -> int:
		return self._dt.year * 100 + self._dt.month
	#

	def toJSON(self) -> dict:
		return {
			"year": self._dt.year,
			"month": self._dt.month,
			"day": self._dt.day,
			"ts": int(self._dt.timestamp()),
			"yearMonth": self.yearMonth,
			"yearMonthDay": self.yearMonthDay,
			"isostr": str(self),
		}
	#

	@staticmethod
	def createFrom(dt:int = None, yearMonthDay:int = None, yearMonth:int = None, yearMonthDayTuple:list = None):
		ret = D()
		if dt is not None:
			dt = datetime.datetime.fromtimestamp(dt)
			y = dt.year
			m = dt.month
			d = dt.day
			ret._dt = datetime.datetime(y, m, d)
		elif yearMonthDay is not None:
			year = yearMonthDay // 10000
			month = (yearMonthDay // 100) % 100
			day = yearMonthDay % 100
			ret._dt = datetime.datetime(year, month, day)
		elif yearMonth is not None:
			year = yearMonthDay // 100
			month = yearMonthDay % 100
			day = 1
			ret._dt = datetime.datetime(year, month, day)
		elif yearMonthDayTuple is not None:
			assert isinstance(yearMonthDayTuple, (list, tuple))
			assert len(yearMonthDayTuple) == 3
			assert isinstance(yearMonthDayTuple[0], int)
			assert isinstance(yearMonthDayTuple[1], int)
			assert isinstance(yearMonthDayTuple[2], int)
			ret._dt = datetime.datetime(yearMonthDayTuple[0], yearMonthDayTuple[1], yearMonthDayTuple[2])
		else:
			raise Exception()
		return ret
	#



#









def dateRange(fromDate:D, toDate:D, includeRightBorder:bool = False):
	i = fromDate.clone()
	while i < toDate:
		yield i.clone()
		i += 1
	if i == toDate:
		if includeRightBorder:
			yield i.clone()
#








