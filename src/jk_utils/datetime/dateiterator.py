


import datetime
import re





class D(object):

	def __init__(self):
		self._dt = None
	#

	# ================================================================================================================================
	# ==== Properties
	# ================================================================================================================================

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
		return self._dt.weekday() + 1
	#

	@property
	def yearMonthDay(self) -> int:
		return self._dt.year * 10000 + self._dt.month * 100 + self._dt.day
	#

	@property
	def yearMonth(self) -> int:
		return self._dt.year * 100 + self._dt.month
	#

	#
	# Calculates the week number
	#
	@property
	def weekNo(self):
		d = datetime.datetime(self.year, 1, 1)

		# the week day of the first day in this year:
		# 1 = monday, 2 = tuesday, ..., 7 = sunday
		firstJanWeekDay = ((d.weekday() + 1) + 7) % 7
		correction = 0 if firstJanWeekDay == 0 else (7 - (- firstJanWeekDay + 1))
		td = self._dt - d
		return (td.days + correction) // 7
	#

	# ================================================================================================================================
	# ==== Special Methods
	# ================================================================================================================================

	def __str__(self):
		return "{:04d}-{:02d}-{:02d}".format(self._dt.year, self._dt.month, self._dt.day)
	#

	def __repr__(self):
		return "{:04d}-{:02d}-{:02d}".format(self._dt.year, self._dt.month, self._dt.day)
	#

	# ================================================================================================================================
	# ==== Operator Methods
	# ================================================================================================================================

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

	def __add__(self, other):
		if isinstance(other, int):
			return D.createFrom(dt=int(self._dt.timestamp() + 24*60*60*other))
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
		if isinstance(other, int):
			return D.createFrom(dt=int(self._dt.timestamp() - 24*60*60*other))
		elif isinstance(other, D):
			return int(datetime.datetime.fromtimestamp(self._dt.timestamp() - 24*60*60*other)) // (24*60*60)
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

	# ================================================================================================================================
	# ==== Methods
	# ================================================================================================================================

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

	#
	# Creates a D object representing the first of january of this year
	#
	def startOfYear(self):
		ret = D()
		ret._dt = datetime.datetime(self.year, 1, 1)
		return ret
	#

	def nextYear(self):
		ret = D()
		ret._dt = datetime.datetime(self.year + 1, self.month, self.day)
		return ret
	#

	def previousYear(self):
		if self.year <= 1:
			raise Exception()
		ret = D()
		ret._dt = datetime.datetime(self.year - 1, self.month, self.day)
		return ret
	#

	def nextMonth(self):
		y = self.year
		m = self.month
		d = self.day

		if m == 12:
			m = 1
			y += 1
		else:
			m += 1

		ret = D()
		while True:
			try:
				ret._dt = datetime.datetime(y, m, d)
				break
			except ValueError as ee:
				d -= 1
		return ret
	#

	def previousMonth(self):
		y = self.year
		m = self.month
		d = self.day

		if m == 1:
			m = 12
			y -= 1
		else:
			m -= 1

		ret = D()
		while True:
			try:
				ret._dt = datetime.datetime(y, m, d)
				break
			except ValueError as ee:
				d -= 1
		return ret
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

	def clone(self):
		ret = D()
		ret._dt = self._dt
		return ret
	#

	#
	# @return	D[]		Returns a list of date objects containing all seven days of this week.
	#
	def generateWeekDates(self) -> list:
		d = self.startOfWeek()
		ret = [ d ]
		for i in range(0, 6):
			d = d.nextDay()
			ret.append(d)
		return ret
	#

	# ================================================================================================================================
	# ==== Static Methods
	# ================================================================================================================================

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

	@staticmethod
	def tryParseFromStr(s:str):
		if isinstance(s, str):
			s = s.strip()
			for dt, year, month, day in D.__tryParse(s):
				if dt is None:
					if year is None:
						d0 = D.now()
						year = d0._dt.year
						try:
							d1 = D.createFrom(yearMonthDayTuple=(year, month, day))
							if d1 < d0:
								d1 = D.createFrom(yearMonthDayTuple=(year + 1, month, day))
							return d1
						except:
							pass
					else:
						try:
							return D.createFrom(yearMonthDayTuple=(year, month, day))
						except:
							pass
				else:
					try:
						return D.createFrom(dt=dt)
					except:
						pass
		return None
	#

	@staticmethod
	def parseFromStr(s:str):
		d = D.tryParseFromStr(s)
		if d is None:
			raise Exception("Failed to parse: " + repr(s))
		return d
	#

	@staticmethod
	def __tryParse(s:str):
		for patternType, pattern in [
			("ymd", r"(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)"),
			("ymd", r"(?P<day>\d\d?).(?P<month>\d\d?).(?P<year>\d\d\d\d)"),
			("ymd", r"(?P<month>\d\d?)/(?P<day>\d\d?)/(?P<year>\d\d\d\d)"),
			("md", r"(?P<day>\d\d?).(?P<month>\d\d?)."),
			("ts", r"(?P<ts>-?\d+)"),
		]:
			m = re.match("^" + pattern + "$", s)
			if m:
				if patternType == "ts":
					try:
						yield (int(s), None, None, None)
					except:
						pass
				elif patternType == "ymd":
					year = int(m.group("year"))
					month = int(m.group("month"))
					day = int(m.group("day"))
					if (1 <= month <= 12) and (1 <= day <= 31) and (100 <= year <= 2999):
						yield (None, year, month, day)
				elif patternType == "md":
					month = int(m.group("month"))
					day = int(m.group("day"))
					if (1 <= month <= 12) and (1 <= day <= 31):
						yield (None, None, month, day)
				else:
					raise Exception()
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








