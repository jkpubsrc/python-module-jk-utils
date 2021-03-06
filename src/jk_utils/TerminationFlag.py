



from .InterruptedException import InterruptedException


#
# This class implements a termination flag for long running tasks.
#
class TerminationFlag(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self):
		self.__bTerminate = False
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def terminate(self):
		self.__bTerminate = True
	#

	#
	# Check if the current activity is to be interrupted. In that case an InterruptedException is raised.
	#
	def check(self):
		if self.__bTerminate:
			raise InterruptedException()
	#

#









