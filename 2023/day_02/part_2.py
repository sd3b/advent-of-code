import re

total_power = 0

for line in open("../inputs/day_02"):
    max_cubes = {"red": -1, "green": -1, "blue": -1}
    matches = re.findall("(\d+) (red|green|blue)", line)

    for n_cubes, colour in matches:
        max_cubes[colour] = max(max_cubes[colour], int(n_cubes))

    total_power += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

print("Part 2:", total_power)
