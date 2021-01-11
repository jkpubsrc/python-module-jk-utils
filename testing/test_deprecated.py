#!/usr/bin/python3


from jk_utils import deprecated



"""

This program is ment to test marking functions or methods as deprecated.

"""




@deprecated
def myFuncA():
	print("myFuncA")
#

@deprecated
def myFuncB():
	print("myFuncB")
#



myFuncA()
myFuncA()

myFuncB()
myFuncB()





