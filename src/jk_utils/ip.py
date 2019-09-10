


import os
import sys
import netifaces





#
# Retrieve all IP addresses from all active network adapters (excluding local host)
#
def getIPs():
	ret = []
	for i in netifaces.interfaces():
		addrs = netifaces.ifaddresses(i)
		try:
			if_mac = addrs[netifaces.AF_LINK][0]['addr']
			if_ip = addrs[netifaces.AF_INET][0]['addr']
			if if_ip == "127.0.0.1":
				continue
			ret.append(if_ip)
		except IndexError as e:
			pass
		except KeyError as e:
			pass
	return ret
#




class LocalIPAddressDetector(object):

	def __init__(self, localIPAddressFilters:list):
		self.__localIPAddressRegExes = []
		for s in localIPAddressFilters:
			pos = s.index("*")
			if pos < 0:
				sRegex = "^" + s + "$"
			elif pos == 0:
				sRegex = "^.+" + s + "$"
			elif pos == len(s) - 1:
				sRegex = "^" + s + ".+$"
			else:
				raise Exception("Invalid network card pattern: " + repr(s))
			self.__localIPAddressRegExes.append(re.compile(sRegex))
	#

	def __call__(self):
		return self.getIPAddresses()
	#

	#
	# Retrieve all local IP addresses this service might be concated in a local network.
	#
	def getIPAddresses(self):
		ret = []

		ipAddrTuples = []
		for ifaceName in netifaces.interfaces():
			addrs = netifaces.ifaddresses(ifaceName)
			try:
				#if_mac = addrs[netifaces.AF_LINK][0]['addr']
				ipAddr = addrs[netifaces.AF_INET][0]['addr']
				if ipAddr == "127.0.0.1":
					continue
				ipAddrTuples.append([ifaceName, ipAddr, False])
			except IndexError as e:
				pass
			except KeyError as e:
				pass

		for ipAddrRegEx in self.__localIPAddressRegExes:
			for r in ipAddrTuples:
				if r[2]:
					continue
				if ipAddrRegEx.match(r[0]):
					r[2] = True
					ret.append(r[1])
		
		return ret
	#

#



