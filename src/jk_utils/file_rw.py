

import os
import gzip
import bz2
import lzma




class openReadBinary(object):

	def __init__(self, filePath):
		self.__filePath = filePath
		if filePath.endswith(".gz") or filePath.endswith(".gzip"):
			self.__open = gzip.open
		elif filePath.endswith(".bz2") or filePath.endswith(".bzip2"):
			self.__open = bz2.open
		elif filePath.endswith(".lzma"):
			self.__open = lzma.open
		else:
			self.__open = open
	#

	def __enter__(self):
		self.__f = self.__open(self.__filePath, "rb")
		return self.__f
	#

	def __exit__(self, *args):
		self.__f.close()
	#

#

class openReadText(object):

	class _BinaryWrapper(object):

		def __init__(self, f):
			self.__f = f
		#

		def read(self, length = None):
			data = self.__f.read()
			return data.decode("utf-8")
		#

		def close(self):
			self.__f.close()
		#

	#

	def __init__(self, filePath):
		self.__filePath = filePath
		if filePath.endswith(".gz") or filePath.endswith(".gzip"):
			self.__open = gzip.open
			self.__bToText = True
		elif filePath.endswith(".bz2") or filePath.endswith(".bzip2"):
			self.__open = bz2.open
			self.__bToText = True
		elif filePath.endswith(".lzma"):
			self.__open = lzma.open
			self.__bToText = True
		else:
			self.__open = open
			self.__bToText = False
	#

	def __enter__(self):
		if self.__bToText:
			self.__f = openReadText._BinaryWrapper(self.__open(self.__filePath, "rb"))
		else:
			self.__f = self.__open(self.__filePath, "r")
		return self.__f
	#

	def __exit__(self, *args):
		self.__f.close()
	#

#





class openWriteBinary(object):

	def __init__(self, filePath, bSafeWrite:bool = True, compression:str = None):
		self.__filePath = filePath
		self.__bSafeWrite = bSafeWrite
		if self.__bSafeWrite:
			self.__filePathTmp = filePath + ".tmp"

		if compression:
			if (compression == "gzip") or (compression == "gz"):
				self.__open = gzip.open
			elif (compression == "bz2") or (compression == "bzip2"):
				self.__open = bz2.open
			elif compression == "lzma":
				self.__open = lzma.open
			else:
				raise Exception("Unknown compressor: " + compression)
		else:
			self.__open = open
	#

	def __enter__(self):
		if self.__bSafeWrite:
			self.__f = self.__open(self.__filePathTmp, "wb")
		else:
			self.__f = self.__open(self.__filePath, "wb")
		return self.__f
	#

	def __exit__(self, *args):
		self.__f.close()
		if self.__bSafeWrite:
			if os.path.isfile(self.__filePath):
				os.unlink(self.__filePath)
			os.rename(self.__filePathTmp, self.__filePath)
	#

#

class openWriteText(object):

	class _BinaryWrapper(object):

		def __init__(self, f):
			self.__f = f
		#

		def write(self, textData):
			self.__f.write(textData.encode("utf-8"))
		#

		def close(self):
			self.__f.close()
		#

	#

	def __init__(self, filePath, bSafeWrite:bool = True, compression:str = None):
		self.__filePath = filePath
		self.__bSafeWrite = bSafeWrite
		if self.__bSafeWrite:
			self.__filePathTmp = filePath + ".tmp"
		self.__bToBinary = False

		if compression:
			if (compression == "gzip") or (compression == "gz"):
				self.__open = gzip.open
				self.__bToBinary = True
			elif (compression == "bz2") or (compression == "bzip2"):
				self.__open = bz2.open
				self.__bToBinary = True
			elif compression == "lzma":
				self.__open = lzma.open
				self.__bToBinary = True
			else:
				raise Exception("Unknown compressor: " + compression)
		else:
			self.__open = open
	#

	def __enter__(self):
		if self.__bSafeWrite:
			if self.__bToBinary:
				self.__f = openWriteText._BinaryWrapper(self.__open(self.__filePathTmp, "wb"))
			else:
				self.__f = self.__open(self.__filePathTmp, "w")
		else:
			if self.__bToBinary:
				self.__f = openWriteText._BinaryWrapper(self.__open(self.__filePath, "wb"))
			else:
				self.__f = self.__open(self.__filePath, "w")
		return self.__f
	#

	def __exit__(self, *args):
		self.__f.close()
		if self.__bSafeWrite:
			if os.path.isfile(self.__filePath):
				os.unlink(self.__filePath)
			os.rename(self.__filePathTmp, self.__filePath)
	#

#













