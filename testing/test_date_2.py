#!/usr/bin/python3



from jk_utils.datetime import *
from jk_testing import Assert




DATE_DATA = (

	(	D.parseFromStr("2001-01-01"),	1,	1	),
	(	D.parseFromStr("2001-01-02"),	2,	1	),
	(	D.parseFromStr("2001-01-03"),	3,	1	),
	(	D.parseFromStr("2001-01-04"),	4,	1	),
	(	D.parseFromStr("2001-01-05"),	5,	1	),
	(	D.parseFromStr("2001-01-06"),	6,	1	),
	(	D.parseFromStr("2001-01-07"),	7,	1	),
	(	D.parseFromStr("2001-01-08"),	1,	2	),

	(	D.parseFromStr("2020-01-01"),	3,	1	),
	(	D.parseFromStr("2020-01-02"),	4,	1	),
	(	D.parseFromStr("2020-01-03"),	5,	1	),
	(	D.parseFromStr("2020-01-04"),	6,	1	),
	(	D.parseFromStr("2020-01-05"),	7,	1	),
	(	D.parseFromStr("2020-01-06"),	1,	2	),

	(	D.parseFromStr("2021-01-01"),	5,	1	),
	(	D.parseFromStr("2021-01-02"),	6,	1	),
	(	D.parseFromStr("2021-01-03"),	7,	1	),
	(	D.parseFromStr("2021-01-04"),	1,	2	),

)


for d, dayOfWeek, weekNo in DATE_DATA:
	print(d)
	print("dayOfWeek")
	Assert.isEqual(d.dayOfWeek, dayOfWeek)
	print("weekNo")
	Assert.isEqual(d.weekNo, weekNo)

for y in range(2000, 2200):
	d = D.createFrom(y, 1, 1)
	Assert.isEqual(d.weekNo, 1)
	d = d.nextWeek()
	Assert.isEqual(d.weekNo, 2)

print()
print("Success!")

