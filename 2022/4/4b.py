import re

overlaps = 0

for line in open("input.txt"):
	line = line.strip()
	a, b, c, d = [int(x) for x in re.findall("(\d+)-(\d+),(\d+)-(\d+)", line)[0]]

	if set(range(a, b + 1)) & set(range(c, d + 1)):
		overlaps += 1

print(overlaps)
