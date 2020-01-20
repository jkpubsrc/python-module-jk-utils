#!/usr/bin/python3



from jk_utils.color import *
from jk_testing import Assert











length = 50
b = RGBSpectrumBuilder()
b.appendGradientBand(RGB(0.7, 0.7, 0.7), RGB(0.7, 0.7, 0), int(length * 0.1))
b.appendGradientBand(RGB(0.7, 0.7, 0),   RGB(1,   0.5, 0), int(length * 0.1))
b.appendGradientBand(RGB(1,   0.5, 0),   RGB(1,   0,   0), int(length * 0.1))
b.appendGradientBand(RGB(1,   0,   0),   RGB(1,   0,   0), int(length * 0.05))
b.insertFlatBand(0, RGB(0.7, 0.7, 0.7), length - len(b))
spectrum = b.compile()


for rgb in spectrum:
	print(rgb)

print()
print(RGB.parse("#b8c7d6"))
print(RGB.parse("#a9b8c7d6"))


