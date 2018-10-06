

import os
import collections


DiskSpaceStats = collections.namedtuple("DiskSpaceStats", [ "total", "used", "freeSystem", "freeUser" ])

def getFileSystemStats(mountPointPath):
	statvfs = os.statvfs(mountPointPath)
	totalBytes = statvfs.f_frsize * statvfs.f_blocks		# Size of filesystem in bytes
	systemFreeBytes = statvfs.f_frsize * statvfs.f_bfree	# Actual number of free bytes
	userFreeBytes = statvfs.f_frsize * statvfs.f_bavail		# Number of free bytes that ordinary users are allowed to use (excl. reserved space)
	return DiskSpaceStats(totalBytes, totalBytes - systemFreeBytes, systemFreeBytes, userFreeBytes)
#



