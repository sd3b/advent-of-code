from string import ascii_letters

priority_sum = 0

lines = open("input.txt").readlines()
groups = [[set(l.strip()) for l in lines[i:i+3]] for i in range(0, len(lines), 3)]

for first, second, third in groups:
	appears_in_both = (first & second & third).pop()
	priority_sum += ascii_letters.index(appears_in_both) + 1

print(priority_sum)
