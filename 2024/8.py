from collections import defaultdict as dd
from itertools import combinations

antennas = dd(list)
antinodes = set()
antinodes_b = set()

for y, line in enumerate(open("inputs/8T.txt")):
    for x, char in enumerate(line.strip()):
        if char != ".":
            antennas[char].append(complex(y, x))

in_bound = lambda z: 0 <= z.real <= y and 0 <= z.imag <= x

for positions in antennas.values():
    for p1, p2 in combinations(positions, 2):
        dir_v = p2 - p1

        for antinode in (p2 + dir_v, p1 - dir_v):
            if in_bound(antinode):
                antinodes.add(antinode)

        for dir_vv in (dir_v, -dir_v):
            antinode = p1

            while in_bound(antinode):
                antinodes_b.add(antinode)
                antinode += dir_vv

print("Part A:", len(antinodes))
print("Part B:", len(antinodes_b))
