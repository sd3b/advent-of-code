import re

target_y = 2000000
no_beacons = set()

for line in open("input.txt"):
	sx, sy, bx, by = map(int, re.findall("-?\d+", line))
	dist = abs(sx - bx) + abs(sy - by)

	y_dist_from_target = abs(sy - target_y)
	x = dist - y_dist_from_target

	for dx in range(sx - x, sx + x + 1):
		no_beacons.add(dx)

	if by == target_y:
		no_beacons.remove(bx)

print(len(no_beacons))
