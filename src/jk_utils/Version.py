








################################################################################################################################
## class Version
################################################################################################################################


class Version(object):

	#
	# Constructor
	#
	# @param		versionStr				The version string this object should represent
	#
	def __init__(self, versionStr = '0'):
		self.__numbers = []
		try:
			for s in versionStr.split('.'):
				while (len(s) > 1) and (s[0] == '0'):		# remove trailing zeros to allow accidental specification of dates as version information
					s = s[1:]
				self.__numbers.append(int(s))
		except ValueError:
			raise Exception('Failed to parse version number: \'' + versionStr + '\'')
	#

	def __str__(self):
		ret = ''
		bFirst = True
		for v in self.__numbers:
			if bFirst:
				bFirst = False
			else:
				ret += '.'
			ret += str(v)
		return ret
	#

	def __repr__(self):
		return self.__str__()
	#

	def compareTo(self, other):
		aNumbers = list(self.__numbers)
		bNumbers = list(other.__numbers)

		length = len(bNumbers)
		if len(aNumbers) < length:
			while len(aNumbers) < length:
				aNumbers.append(0)
		else:
			length = len(aNumbers)
			while len(bNumbers) < length:
				bNumbers.append(0)

		for i in range(0, length):
			na = aNumbers[i]
			nb = bNumbers[i]
			x = (na > nb) - (na < nb)
			# print('> ' + str(na) + '  ' + str(nb) + '  ' + str(x))
			if x != 0:
				return x
		return 0
	#

	def __cmp__(self, other):
		n = self.compareTo(other)
		return n
	#

	def __lt__(self, other):
		n = self.compareTo(other)
		#print '???? a=' + str(self)
		#print '???? b=' + str(other)
		#print '???? ' + str(n)
		return n < 0
	#

	def __le__(self, other):
		n = self.compareTo(other)
		#print '???? a=' + str(self)
		#print '???? b=' + str(other)
		#print '???? ' + str(n)
		return n <= 0
	#

	def __gt__(self, other):
		n = self.compareTo(other)
		return n > 0
	#

	def __ge__(self, other):
		n = self.compareTo(other)
		return n >= 0
	#

	def __eq__(self, other):
		n = self.compareTo(other)
		return n == 0
	#

	def __ne__(self, other):
		n = self.compareTo(other)
		return n != 0
	#

#

















