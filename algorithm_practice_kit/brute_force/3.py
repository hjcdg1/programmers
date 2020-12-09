import math


def solution(brown, yellow):
	area = brown + yellow

	for h in range(3, math.floor(area ** (1 / 2)) + 1):
		if area % h == 0:
			w = area // h
			if yellow == area - 2 * w - 2 * (h - 2):
				return [w, h]