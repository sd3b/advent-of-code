from collections import defaultdict as dd
from functools import cache

f = open("inputs/19.txt")
available = dd(list)

for w in f.readline().split(","):
    towel = w.strip()
    available[towel[0]].append(towel)

f.readline()

@cache
def ways(towel):
    if towel == "":
        return 1
    
    n = 0

    for substr in available[towel[0]]:
        if towel.startswith(substr):
            n += ways(towel[len(substr):])

    return n

part_1 = part_2 = 0

for line in f:
    w = ways(line.strip())
    part_1 += 1 if w else 0
    part_2 += w

print("Part 1:", part_1)
print("Part 2:", part_2)
