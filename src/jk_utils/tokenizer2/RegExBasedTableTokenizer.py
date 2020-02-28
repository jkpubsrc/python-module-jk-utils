


import re
import collections
import typing

from .Token import Token







class _TokenizationState(object):

	def __init__(self, initialState:str):
		self.lineNo = 1
		self.line_start = 0
		self.pos = 0
		self.currentState = initialState
	#

#




#
# RegEx based tokenizer: This tokenizer uses regular expressions in order to create tokens.
#
class RegExBasedTokenizingTable(object):

	#
	# Initialization method
	#
	# @param		object[] patternDefs	A list of pattern definitions. Each pattern definition should be a tuple or list of one of the following stcutrues:
	#										* 4 items
	#											* (required) str: the token type to use on match
	#											* (required) str: the pattern to match
	#											* (optional) str: next state
	#											* (optional) callable: parsing delegate
	#										* 6 items
	#											* (required) str: the token type to use on match
	#											* (optional) str: if not None a pattern to match but that will not be part of the token content
	#											* (required) str: the pattern to match (which will be the content of the token)
	#											* (optional) str: if not None a pattern to match but that will not be part of the token content
	#											* (optional) str: next state
	#											* (optional) callable: parsing delegate
	#
	def __init__(self, stateName:str, patternDefs):
		assert isinstance(stateName, str)
		assert stateName

		assert isinstance(patternDefs, (tuple, list))
		assert len(patternDefs) > 0

		self.__stateName = stateName

		self.__pattern2StateMap = {}
		self.__tokenParsingDelegatesMap = {}
		rawPatternsList = []
		for patternDef in patternDefs:
			assert isinstance(patternDef, (tuple, list))

			if len(patternDef) == 4:
				tokenType, pattern, nextState, parsingDelegate = patternDef
				patternPre = None
				patternPost = None
			elif len(patternDef) == 6:
				tokenType, patternPre, pattern, patternPost, nextState, parsingDelegate = patternDef
			else:
				raise Exception("Invalid pattern definition: " + str(patternDef))

			p2 = []
			if patternPre:
				p2.extend(("(?:", patternPre, ")"))
			p2.extend(("(?P<", tokenType, ">", pattern, ")"))
			if patternPost:
				p2.extend(("(?:", patternPost, ")"))

			rawPatternsList.append("".join(p2)),
			self.__pattern2StateMap[tokenType] = nextState
			self.__tokenParsingDelegatesMap[tokenType] = parsingDelegate

		self.__compiledPatterns = None

		rawPatterns = "|".join(rawPatternsList)
		rawPatterns += "|(?P<NEWLINE>\n)"
		rawPatterns += "|(?P<SPACE>[\t ]+)"
		rawPatterns += "|(?P<ERROR>.)"
		try:
			self.__compiledPatterns = re.compile(rawPatterns)
		except Exception as e:
			print("==== COMPILE ERROR")
			print("==== " + e.msg)
			print("==== " + rawPatterns)
			s = ""
			for i in range(0, e.colno):
				s += " "
			s += "^"
			print(s)
			raise
	#



	def addStateTransition(self, tokenType:str, nextState:str):
		self.__pattern2StateMap[tokenType] = nextState
		return self
	#



	@property
	def stateName(self):
		return self.__stateName
	#



	def _getNextToken(self, state:_TokenizationState, text:str) -> tuple:
		mo = self.__compiledPatterns.match(text, state.pos)
		columnNo = state.pos - state.line_start + 1
		if (not mo) or (state.pos != mo.start()):
			raise RuntimeError("Syntay error encountered at " + str(state.lineNo) + ":" + str(columnNo) + "!")

		tokenType = mo.lastgroup
		value = mo.group(tokenType)
		if tokenType == "NEWLINE":
			ret = Token(tokenType, value, state.lineNo, columnNo, mo.end() - state.pos)
			state.line_start = mo.end()
			state.lineNo += 1
		elif tokenType == "SPACE":
			ret = Token(tokenType, value, state.lineNo, columnNo, mo.end() - state.pos)
		elif tokenType == "ERROR":
			raise RuntimeError("Parse error encountered at " + str(state.lineNo) + ":" + str(columnNo) + "!")
		else:
			d = self.__tokenParsingDelegatesMap.get(tokenType)
			if d != None:
				value = d(value)
			ret = Token(tokenType, value, state.lineNo, columnNo, mo.end() - state.pos)

		#print(">>EMITTING:", ret)
		nextState = self.__pattern2StateMap.get(tokenType)
		if nextState:
			#print(">>SWITCHING FROM STATE", repr(state.currentState), "TO STATE", repr(nextState))
			state.currentState = nextState

		state.pos = mo.end()

		return ret
	#



	def _getAllResultStates(self) -> list:
		return [ x for x in self.__pattern2StateMap.values() if x is not None ]
	#



#




class RegExBasedTableTokenizer(object):

	def __init__(self, initialState:str, tokenizationTables:typing.Union[list,tuple,typing.Sequence]):
		assert isinstance(initialState, str)
		assert initialState

		tokenizationTables = list(tokenizationTables)
		self.__tokenizationTableMap = {}

		allStates = set()
		allResultStates = set()
		for table in tokenizationTables:
			assert isinstance(table, RegExBasedTokenizingTable)
			if table.stateName in self.__tokenizationTableMap:
				raise Exception("Duplicate table: " + table.stateName)
			for s in table._getAllResultStates():
				allResultStates.add(s)
			allStates.add(table.stateName)
			self.__tokenizationTableMap[table.stateName] = table
		#print("allStates:", allStates)
		#print("allResultStates:", allResultStates)
		wrongResultStates = allResultStates - allStates
		if wrongResultStates:
			raise Exception("No such states: " + str(sorted(wrongResultStates)))

		if initialState not in self.__tokenizationTableMap:
			raise Exception("No such initial state: " + repr(initialState))

		self.__initialState = initialState
	#



	#
	# @return		Token,str[] tokens			Returns token objects according to the pattern defined during initialization.
	#
	def tokenize(self, text, bEmitWhiteSpaces:bool = False, bEmitNewLines:bool = False):
		assert isinstance(text, str)
		assert isinstance(bEmitWhiteSpaces, bool)
		assert isinstance(bEmitNewLines, bool)

		state = _TokenizationState(self.__initialState)
		maxPos = len(text)
		while state.pos < maxPos:
			currentTable = self.__tokenizationTableMap[state.currentState]
			t = currentTable._getNextToken(state, text)
			if t.type == "NEWLINE":
				if bEmitNewLines:
					yield t
			elif t.type == "SPACE":
				if bEmitWhiteSpaces:
					yield t
			else:
				yield t
	#



#




