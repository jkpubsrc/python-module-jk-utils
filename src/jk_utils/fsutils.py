

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


