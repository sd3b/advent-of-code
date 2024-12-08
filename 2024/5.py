from collections import defaultdict as dd
from functools import cmp_to_key

rules = dd(set)

def cmp(x, y):
    return -1 if x in rules[y] else 0

total_a = 0
total_b = 0

r_data, u_data = open("inputs/5.txt").read().split("\n\n")

for line in r_data.split():
    x, y = map(int, line.split("|"))
    rules[y].add(x) # store backwards

for line in u_data.split():
    banned = set()
    update = [*map(int, line.split(","))]
    crap = False

    for n in update:
        if n in banned:
            crap = True
            break
        else:
            banned |= rules[n]

    if not crap:
        total_a += update[len(update) // 2]
    else:
        sorted_update = sorted(update, key = cmp_to_key(cmp))
        total_b += sorted_update[len(sorted_update) // 2]

print("Part A:", total_a)
print("Part B:", total_b)
