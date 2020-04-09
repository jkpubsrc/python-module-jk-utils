#!/usr/bin/python3



from jk_utils.datetime import *
from jk_testing import Assert




d1 = D.now()
d2 = d1.nextDay().nextDay()
Assert.isEqual(d2 - d1, 2)
Assert.isEqual((d1.dayOfWeek + 2) % 7, d2.dayOfWeek)


d1 = D.now().startOfWeek()
d2 = d1.nextWeek()
Assert.isEqual(d2 - d1, 7)



d1 = D.now()
d2 = d1.nextWeek()
Assert.isTrue((d2 - d1) > 0)
Assert.isTrue((d2 - d1) <= 7)
Assert.isTrue(d2.dayOfWeek == 1)
Assert.isTrue((d2 - 1).dayOfWeek == 7)
Assert.isTrue(d2 >= d1)
Assert.isTrue(d1 <= d2)



d1 = D.now()
d2 = d1.nextWeek().previousWeek()
Assert.isTrue(d1 >= d2)



for d in dateRange(d1.startOfWeek(), d2.nextWeek()):
	print(d, "\t", d.toJSON())

Assert.isEqual(len(list(dateRange(d1.startOfWeek(), d2.nextWeek()))), 7)






