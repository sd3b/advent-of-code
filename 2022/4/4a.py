import re

overlaps = 0

for line in open("input.txt"):
	line = line.strip()
	a, b, c, d = [int(x) for x in re.findall("(\d+)-(\d+),(\d+)-(\d+)", line)[0]]

	if a >= c and b <= d:
		overlaps += 1
	elif c >= a and d <= b:
		overlaps += 1

print(overlaps)
