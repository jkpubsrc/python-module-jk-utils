



class TextOutputBuffer(object):

	def __init__(self):
		self.__buf = []
	#

	def writeLn(self, *args):
		for a in args:
			self.__buf.append(str(a))
		self.__buf.append("\n")
	#

	def write(self, *args):
		for a in args:
			self.__buf.append(str(a))
	#

	def writeNewLines(self, n:int):
		for i in range(0, n):
			self.__buf.append("\n")
	#

	def __str__(self):
		return "".join(self.__buf)
	#

	def saveToFile(self, filePath:str):
		with open(filePath, "w") as fout:
			fout.write(str(self))
	#

#





