#!/usr/bin/python3


import jk_utils







for ifName, ipAddr, macAddr in jk_utils.ip.getIPsEx():
	print(ifName, "|", ipAddr, "|", macAddr)




