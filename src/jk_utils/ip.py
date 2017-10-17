#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import netifaces





#
# Retrieve all IP addresses from all active network adapters (excluding local host)
#
def getIPs():
	ret = []
	for i in netifaces.interfaces():
		addrs = netifaces.ifaddresses(i)
		try:
			if_mac = addrs[netifaces.AF_LINK][0]['addr']
			if_ip = addrs[netifaces.AF_INET][0]['addr']
			if if_ip == "127.0.0.1":
				continue
			ret.append(if_ip)
		except IndexError as e:
			pass
		except KeyError as e:
			pass
	return ret
#




