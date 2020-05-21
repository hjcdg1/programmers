def solution(phone_book):
	N = len(phone_book)
	S = max(1, len(str(N)) - 1)

	hash_table = {}
	for phone in phone_book:
		prefix = phone[:S]
		if prefix not in hash_table:
			hash_table[prefix] = [phone]
		else:
			for compare in hash_table[prefix]:
				if (compare in phone) or (phone in compare):
					return False
	return True