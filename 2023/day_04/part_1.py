import re

points = 0

for line in open("input.txt"):
    winning_nums, nums_on_card = (set(re.findall("\d+", nums)) for nums in line.split(":")[-1].split("|"))

    if (matches := len(winning_nums & nums_on_card)) > 0:
        points += 2 ** (matches - 1)

print("Part 1:", points)
