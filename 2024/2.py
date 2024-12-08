safe = 0
kinda_safe = 0

def is_safe(level):
    diffs = [level[idx + 1] - level[idx] for idx in range(0, len(level) - 1)]
    all_inc = all(1 <= x <= 3 for x in diffs)
    all_dec = all(-3 <= x <= -1 for x in diffs)
    return all_inc or all_dec

for line in open("inputs/2.txt"):
    level = [int(x) for x in line.split()]
    safe += is_safe(level)
    level_removed = [level[:idx] + level[idx + 1:] for idx in range(len(level))]
    kinda_safe += any(map(is_safe, level_removed))

print("Part A:", safe)
print("Part B:", kinda_safe)
