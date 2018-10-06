

import os
import collections


def makeAbsDirPathAndCheckDirExists(baseDir:str, dirPath:str):
	if baseDir:
		if not os.path.isdir(baseDir):
			raise Exception("Base directory does not exist: " + repr(baseDir))
	if not os.path.isabs(dirPath):
		if baseDir is None:
			dirPath = os.path.abspath(dirPath)
		else:
			dirPath = os.path.abspath(os.path.join(baseDir, dirPath))
	if not os.path.isdir(dirPath):
		raise Exception("Directory does not exist: " + repr(dirPath))
	return dirPath
#

def makeAbsFilePathAndCheckFileExists(baseDir:str, filePath:str):
	if baseDir:
		if not os.path.isdir(baseDir):
			raise Exception("Base directory does not exist: " + repr(baseDir))
	if not os.path.isabs(filePath):
		if baseDir is None:
			filePath = os.path.abspath(filePath)
		else:
			filePath = os.path.abspath(os.path.join(baseDir, filePath))
	if not os.path.isfile(filePath):
		raise Exception("File does not exist: " + repr(filePath))
	return filePath
#

def makeAbsFilePathAndCheckBaseDirExists(baseDir:str, filePath:str):
	if baseDir:
		if not os.path.isdir(baseDir):
			raise Exception("Base directory does not exist: " + repr(baseDir))
	if not os.path.isabs(filePath):
		if baseDir is None:
			filePath = os.path.abspath(filePath)
		else:
			filePath = os.path.abspath(os.path.join(baseDir, filePath))
	baseDir = os.path.dirname(filePath)
	if not os.path.isfile(baseDir):
		raise Exception("Base directory of file does not exist: " + repr(filePath))
	return filePath
#

def findMountPoint(path:str):
    path = os.path.abspath(path)
    orig_dev = os.stat(path).st_dev

    while path != '/':
        pdir = os.path.dirname(path)
        if os.stat(pdir).st_dev != orig_dev:
            # we crossed the device border
            break
        path = pdir
    return path
#




