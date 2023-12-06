import re

f = open("input.txt")
seeds = [int(s) for s in re.findall("\d+", f.readline())]

stages = f.read().strip().split("\n\n")
mappings = [[int(x) for x in re.findall("\d+", mapping)] for mapping in stages]

for idx, seed in enumerate(seeds):
    for nums in mappings:
        for i in range(0, len(nums), 3):
            dest, src, range_len = nums[i:i+3]

            if src <= seed <= src + range_len - 1:
                seed = dest + seed - src
                break

    seeds[idx] = seed

print(min(seeds))