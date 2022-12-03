from string import ascii_letters

priority_sum = 0

for line in open("input.txt"):
	mid = len(line) // 2
	first_com, second_com = set(line[:mid]), set(line[mid:])
	appears_in_both = (first_com & second_com).pop()
	priority_sum += ascii_letters.index(appears_in_both) + 1

print(priority_sum)
