

import typing
import time






_GREGORIAN_CALENDAR_YEAR_IN_DAYS = 365.2425
_GREGORIAN_CALENDAR_YEAR_IN_SECONDS = 365.2425 * 24*60*60
_GREGORIAN_CALENDAR_AVG_DAYS_PER_MONTH = _GREGORIAN_CALENDAR_YEAR_IN_DAYS / 12
_GREGORIAN_CALENDAR_AVG_SECONDS_PER_MONTH = _GREGORIAN_CALENDAR_YEAR_IN_DAYS * 24*60*60 / 12
_GREGORIAN_CALENDAR_SECONDS_PER_WEEK = 24*60*60*7
_GREGORIAN_CALENDAR_SECONDS_PER_DAY = 24*60*60
_GREGORIAN_CALENDAR_SECONDS_PER_HOUR = 60*60
_GREGORIAN_CALENDAR_SECONDS_PER_MINUTE = 60










#
# Splits the specified number of seconds into years, months, weeks, days, hours, minutes and seconds.
#
# As long as the time remains below the amount of one month all return values can be calculated absolutely accurately. In that case
# <c>(0, 0, weeks, days, hours, minutes, seconds)</c> is returned.
#
# If the time is greater or equal to the duration of one month this can no longer be calculated accurately, as the length of the months differ. In that case 
# <c>(years, months, weeks, -1, -1, -1, -1)</c> is returned.
# As this function is intended to calculate values for displaying time durations, a better accuracy doesn't make any sense anyway.
#
def secondsToDHMSf(fSeconds:float) -> typing.Tuple[int,int,int,float]:
	assert isinstance(fSeconds, (float,int))
	assert fSeconds >= 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_DAY:
		days = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_DAY)
		fSeconds = fSeconds - days * _GREGORIAN_CALENDAR_SECONDS_PER_DAY
	else:
		days = 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_HOUR:
		hours = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_HOUR)
		fSeconds = fSeconds - hours * _GREGORIAN_CALENDAR_SECONDS_PER_HOUR
	else:
		hours = 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE:
		minutes = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE)
		fSeconds = fSeconds - minutes * _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE
	else:
		minutes = 0

	return (days, hours, minutes, fSeconds)
#



#
# Splits the specified number of seconds into years, months, weeks, days, hours, minutes and seconds.
#
# As long as the time remains below the amount of one month all return values can be calculated absolutely accurately. In that case
# <c>(0, 0, weeks, days, hours, minutes, seconds)</c> is returned.
#
# If the time is greater or equal to the duration of one month this can no longer be calculated accurately, as the length of the months differ. In that case 
# <c>(years, months, weeks, -1, -1, -1, -1)</c> is returned.
# As this function is intended to calculate values for displaying time durations, a better accuracy doesn't make any sense anyway.
#
def secondsToDHMS(fSeconds:float) -> typing.Tuple[int,int,int,int]:
	days, hours, minutes, fSeconds = secondsToDHMSf(fSeconds)

	seconds = int(fSeconds)

	return (days, hours, minutes, seconds)
#



#
# Splits the specified number of seconds into years, months, weeks, days, hours, minutes and seconds.
#
# As long as the time remains below the amount of one month all return values can be calculated absolutely accurately. In that case
# <c>(0, 0, weeks, days, hours, minutes, seconds)</c> is returned.
#
# If the time is greater or equal to the duration of one month this can no longer be calculated accurately, as the length of the months differ. In that case 
# <c>(years, months, weeks, -1, -1, -1, -1)</c> is returned.
# As this function is intended to calculate values for displaying time durations, a better accuracy doesn't make any sense anyway.
#
def secondsToYMWDHMSf(fSeconds:float) -> typing.Tuple[int,int,int,int,int,int,float]:
	assert isinstance(fSeconds, (float,int))
	assert fSeconds >= 0

	if fSeconds >= _GREGORIAN_CALENDAR_YEAR_IN_SECONDS:
		years = int(fSeconds / _GREGORIAN_CALENDAR_YEAR_IN_SECONDS)
		fSeconds = fSeconds - years * _GREGORIAN_CALENDAR_YEAR_IN_SECONDS
	else:
		years = 0

	if fSeconds >= _GREGORIAN_CALENDAR_AVG_SECONDS_PER_MONTH:
		months = int(fSeconds / _GREGORIAN_CALENDAR_AVG_SECONDS_PER_MONTH)
		fSeconds = fSeconds - months * _GREGORIAN_CALENDAR_AVG_SECONDS_PER_MONTH
	else:
		months = 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_WEEK:
		weeks = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_WEEK)
		fSeconds = fSeconds - weeks * _GREGORIAN_CALENDAR_SECONDS_PER_WEEK
	else:
		weeks = 0

	if (years > 0) or (months > 0):
		return (years, months, weeks, -1, -1, -1, -1)

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_DAY:
		days = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_DAY)
		fSeconds = fSeconds - days * _GREGORIAN_CALENDAR_SECONDS_PER_DAY
	else:
		days = 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_HOUR:
		hours = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_HOUR)
		fSeconds = fSeconds - hours * _GREGORIAN_CALENDAR_SECONDS_PER_HOUR
	else:
		hours = 0

	if fSeconds >= _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE:
		minutes = int(fSeconds / _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE)
		fSeconds = fSeconds - minutes * _GREGORIAN_CALENDAR_SECONDS_PER_MINUTE
	else:
		minutes = 0

	return (years, months, weeks, days, hours, minutes, fSeconds)
#



#
# Splits the specified number of seconds into years, months, weeks, days, hours, minutes and seconds.
#
# As long as the time remains below the amount of one month all return values can be calculated absolutely accurately. In that case
# <c>(0, 0, weeks, days, hours, minutes, seconds)</c> is returned.
#
# If the time is greater or equal to the duration of one month this can no longer be calculated accurately, as the length of the months differ. In that case 
# <c>(years, months, weeks, -1, -1, -1, -1)</c> is returned.
# As this function is intended to calculate values for displaying time durations, a better accuracy doesn't make any sense anyway.
#
def secondsToYMWDHMS(fSeconds:float) -> typing.Tuple[int,int,int,int,int,int,int]:
	years, months, weeks, days, hours, minutes, fSeconds = secondsToYMWDHMSf(fSeconds)

	seconds = int(fSeconds)

	return (years, months, weeks, days, hours, minutes, seconds)
#






_NAMES_EN = {
	"second": ( "1 second", "{} seconds" ),
	"minute": ( "1 minute", "{} minutes" ),
	"hour": ( "1 hour", "{} hours" ),
	"day": ( "1 day", "{} days" ),
	"week": ( "1 week", "{} weeks" ),
	"month": ( "1 month", "{} months" ),
	"year": ( "1 year", "{} years" ),
}



def secondsToHRStr(fSeconds:float) -> str:
	y, m, w, d, h, m2, s = secondsToYMWDHMS(fSeconds)

	bNoWeeks = False
	bNoHours = False
	bNoMinutes = False
	bNoSeconds = False

	if y <= 0:
		sYears = ""
	else:
		_names = _NAMES_EN["year"]
		sYears = _names[0] if y == 1 else _names[1].format(y)
		bNoWeeks = True
		bNoHours = True
		bNoMinutes = True
		bNoSeconds = True

	if m <= 0:
		sMonths = ""
	else:
		_names = _NAMES_EN["month"]
		sMonths = _names[0] if m == 1 else _names[1].format(m)
		bNoHours = True
		bNoMinutes = True
		bNoSeconds = True

	if bNoWeeks or (w <= 0):
		sWeeks = ""
	else:
		_names = _NAMES_EN["week"]
		sWeeks = _names[0] if w == 1 else _names[1].format(w)
		bNoHours = True
		bNoMinutes = True
		bNoSeconds = True

	if d <= 0:
		sDays = ""
	else:
		_names = _NAMES_EN["day"]
		sDays = _names[0] if d == 1 else _names[1].format(d)
		bNoMinutes = True
		bNoSeconds = True

	if bNoHours or (h <= 0):
		sHours = ""
	else:
		_names = _NAMES_EN["hour"]
		sHours = _names[0] if h == 1 else _names[1].format(h)
		bNoSeconds = True

	if bNoMinutes or (m2 <= 0):
		sMinutes = ""
	else:
		_names = _NAMES_EN["minute"]
		sMinutes = _names[0] if m2 == 1 else _names[1].format(m2)

	if bNoSeconds or (s <= 0):
		sSeconds = ""
	else:
		_names = _NAMES_EN["second"]
		sSeconds = _names[0] if s == 1 else _names[1].format(s)

	col = [
		sYears,
		sMonths,
		sWeeks,
		sDays,
		sHours,
		sMinutes,
		sSeconds,
	]
	ret = ", ".join([ item for item in col if item ])
	if ret:
		return ret
	else:
		return "now"
#





class DurationMeter(object):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self, nRepeats:int = 1, factor:typing.Union[int,float] = 1):
		assert isinstance(nRepeats, int)
		assert nRepeats > 0
		assert isinstance(factor, (int, float))

		self.__nRepeats = nRepeats
		self.__factor = factor
		self.__tStart:float = -1
		self.__tEnd:float = -1
		self.__tDuration:float = 0
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def tStart(self) -> float:
		return self.__tStart
	#

	@property
	def tDuration(self) -> float:
		return self.__tDuration
	#

	@property
	def tEnd(self) -> float:
		return self.__tEnd
	#

	@property
	def durationStr(self, defaultValue = "not_started"):
		if self.__tStart < 0:
			return defaultValue
		days, hours, minutes, fSeconds = secondsToDHMSf(self.__tDuration)

		return f"{days:02d}:{hours:02d}:{minutes:02d}:{fSeconds:02f}"
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self):
		if self.__tStart < 0:
			return "not_started"
		return f"{self.__tDuration}"
	#

	def __repr__(self):
		return "DurationMeter<( " + self.__str__() + ")>"
	#

	def __enter__(self):
		self.__tEnd = -1
		self.__tStart = time.time()
		return self
	#

	def __exit__(self, type, value, traceback):
		self.__tEnd = time.time()
		self.__tDuration = (self.__tEnd - self.__tStart) * self.__factor / self.__nRepeats
	#

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

#










