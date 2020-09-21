

import os
import collections


FileSystemStats = collections.namedtuple("FileSystemStats", [
	"bytesTotal", "bytesUsed", "bytesFreeSystem", "bytesFreeUser", "rateBytesUsed",
	"inodesTotal", "inodesUsed", "inodesFree", "rateInodesUsed"
])

def getFileSystemStats(mountPointPath):
	statvfs = os.statvfs(mountPointPath)

	bytesTotal = statvfs.f_frsize * statvfs.f_blocks		# Size of filesystem in bytes
	bytesFreeSystem = statvfs.f_frsize * statvfs.f_bfree	# Actual number of free bytes
	bytesFreeUser = statvfs.f_frsize * statvfs.f_bavail		# Number of free bytes that ordinary users are allowed to use (excl. reserved space)
	bytesUsed = bytesTotal - bytesFreeSystem
	rateBytesUsed = ((bytesTotal - bytesFreeUser) / bytesTotal) if bytesTotal > 0 else 1

	inodesTotal = statvfs.f_files    					    # inodes
	inodesFree = statvfs.f_ffree	   						# free inodes
	inodesUsed = inodesTotal - inodesFree
	rateInodesUsed = (inodesUsed / inodesTotal) if inodesTotal > 0 else 1

	return FileSystemStats(
		bytesTotal, bytesUsed, bytesFreeSystem, bytesFreeUser, rateBytesUsed,
		inodesTotal, inodesUsed, inodesFree, rateInodesUsed
		)
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

def getFolderSize(dirPath:str):
    total_size = os.path.getsize(dirPath)
    for item in os.listdir(dirPath):
        itempath = os.path.join(dirPath, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size
#







def getFileNameWithoutExtension(fileName:str) -> str:
	fileName = os.path.basename(fileName)
	pos = fileName.rfind(".")
	if pos < 0:
		return fileName
	else:
		return fileName[:pos]
#


#
# Get the file name extension.
#
def getFileNameExtension(fileName:str, bIncludeDot:bool = True) -> str:
	fileName = os.path.basename(fileName)
	pos = fileName.rfind(".")
	if pos < 0:
		return None
	else:
		if bIncludeDot:
			return fileName[pos:]
		else:
			return fileName[pos + 1:]
#


def _recursiveWalk0(baseDirPath:str, currentDirPath:str, subDirParts:tuple, dirFilter, fileFilter):
	# print(">>", currentDirPath)
	entries = sorted(list(os.scandir(currentDirPath)), key=lambda x: x.name)
	for fe in entries:
		# yield baseDirPath, subDirParts, fe
		# print(fe)
		if fe.is_dir():
			# print("DIR:", fe)
			bDescend = (dirFilter is None) or dirFilter(fe)
			if bDescend:
				yield from _recursiveWalk0(baseDirPath, fe.path, subDirParts + ( fe.name, ), dirFilter, fileFilter)
		elif fe.is_file():
			# print("FILE:", fe)
			bAccept = (fileFilter is None) or fileFilter(fe)
			if bAccept:
				yield baseDirPath, subDirParts, fe
		else:
			pass
#

#
# Generator that recursively returns files.
#
# @param	str dirPath				The directory to scan recursively
# @param	callable dirFilter		A delegate that receives a directory entry object and returns `True` or `False` depending wether to further descend into that directory
# @param	callable fileFilter		A delegate that receives a file entry object and returns `True` or `False` depending wether to return this entry or not
# @return	str baseDirPath			The directory that is the root of the recursive descend
# @return	str[] subDirParts		The name of the subdirectories
# @return	io.FileEntry fe			A file entry data structure as returned by `os.scan()`
#
def recursiveWalk(dirPath:str, dirFilter, fileFilter):
	assert isinstance(dirPath, str)
	assert os.path.isdir(dirPath)
	if dirFilter is not None:
		assert callable(dirFilter)
	if fileFilter is not None:
		assert callable(fileFilter)

	yield from _recursiveWalk0(dirPath, dirPath, tuple(), dirFilter, fileFilter)
#










