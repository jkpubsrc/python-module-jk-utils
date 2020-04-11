#!/usr/bin/python3



import datetime

import jk_utils.datetime
from jk_utils.datatypes import *
from jk_testing import Assert








t = getTypeAsStr(123)
print(t)
Assert.isEqual(t, "int")

t = getTypeAsStr(3.14)
print(t)
Assert.isEqual(t, "float")

t = getTypeAsStr("abc")
print(t)
Assert.isEqual(t, "str")

t = getTypeAsStr(True)
print(t)
Assert.isEqual(t, "bool")

t = getTypeAsStr(False)
print(t)
Assert.isEqual(t, "bool")

t = getTypeAsStr(datetime.datetime.now())
print(t)
Assert.isEqual(t, "datetime")

t = getTypeAsStr(jk_utils.datetime.D.now())
print(t)
Assert.isEqual(t, "D")

t = getTypeAsStr(datetime.datetime.now(), fqn=True)
print(t)
Assert.isEqual(t, "datetime.datetime")

t = getTypeAsStr(jk_utils.datetime.D.now(), fqn=True)
print(t)
Assert.isEqual(t, "jk_utils.datetime.D.D")



print()



t = getTypeAsStr([ 123 ])
print(t)
Assert.isEqual(t, "int[]")

t = getTypeAsStr([ 3.14 ])
print(t)
Assert.isEqual(t, "float[]")

t = getTypeAsStr([ "abc" ])
print(t)
Assert.isEqual(t, "str[]")

t = getTypeAsStr([ True ])
print(t)
Assert.isEqual(t, "bool[]")

t = getTypeAsStr([ False ])
print(t)
Assert.isEqual(t, "bool[]")

t = getTypeAsStr([ datetime.datetime.now() ])
print(t)
Assert.isEqual(t, "datetime[]")

t = getTypeAsStr([ jk_utils.datetime.D.now() ])
print(t)
Assert.isEqual(t, "D[]")

t = getTypeAsStr([ None, "January", "February", "March" ])
print(t)
Assert.isEqual(t, "str[]")



print()



t = getTypeAsStr(( 123, ))
print(t)
Assert.isEqual(t, "int[]")

t = getTypeAsStr(( 3.14, ))
print(t)
Assert.isEqual(t, "float[]")

t = getTypeAsStr(( "abc", ))
print(t)
Assert.isEqual(t, "str[]")

t = getTypeAsStr(( True, ))
print(t)
Assert.isEqual(t, "bool[]")

t = getTypeAsStr(( False, ))
print(t)
Assert.isEqual(t, "bool[]")

t = getTypeAsStr(( datetime.datetime.now(), ))
print(t)
Assert.isEqual(t, "datetime[]")

t = getTypeAsStr(( jk_utils.datetime.D.now(), ))
print(t)
Assert.isEqual(t, "D[]")



print()



t = getTypeAsStr({ "a" : 123 })
print(t)
Assert.isEqual(t, "dict<str,int>")

t = getTypeAsStr({ "a" : 3.14 })
print(t)
Assert.isEqual(t, "dict<str,float>")

t = getTypeAsStr({ "a" : "abc" })
print(t)
Assert.isEqual(t, "dict<str,str>")

t = getTypeAsStr({ "a" : True })
print(t)
Assert.isEqual(t, "dict<str,bool>")

t = getTypeAsStr({ "a" : False })
print(t)
Assert.isEqual(t, "dict<str,bool>")

t = getTypeAsStr({ "a": datetime.datetime.now() })
print(t)
Assert.isEqual(t, "dict<str,datetime>")

t = getTypeAsStr({ "a": jk_utils.datetime.D.now() })
print(t)
Assert.isEqual(t, "dict<str,D>")

t = getTypeAsStr({ "x": None, "1": "January", "2": "February", "3": "March" })
print(t)
Assert.isEqual(t, "dict<str,str>")









