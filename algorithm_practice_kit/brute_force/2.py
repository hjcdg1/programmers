from itertools import permutations
from math import floor

def solution(numbers):
	N = len(numbers)
	prime_numbers = set()

	for i in range(1, N + 1):
		for p in permutations(numbers, i):
			number = int(''.join(p))
			
			if number < 2:
				is_prime_number = False
			else:
				is_prime_number = True
				for j in range(2, floor(number ** (1 / 2)) + 1):
					if number % j == 0:
						is_prime_number = False
						break
				if is_prime_number:
					prime_numbers.add(number)
	return len(prime_numbers)