import re

f = open("input.txt")
data = [int(s) for s in re.findall("\d+", f.readline())]
seed_ranges = []

for i in range(0, len(data), 2):
    start, length = data[i:i+2]
    seed_ranges.append([start, start + length])

stages = f.read().strip().split("\n\n")
mappings = [[int(x) for x in re.findall("\d+", mapping)] for mapping in stages]

for idx, mapping in enumerate(mappings):
    new_ranges = []

    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()

        new_range = False

        for i in range(0, len(mapping), 3):
            dest, src, range_len = mapping[i:i+3]

            overlap_start = max(start, src)
            overlap_end = min(end, src + range_len)

            if overlap_start < overlap_end:
                new_range = True
                new_ranges.append([overlap_start - src + dest, overlap_end - src + dest])

                if overlap_start > start:
                    seed_ranges.append([start, overlap_start])
                if end > overlap_end:
                    seed_ranges.append([overlap_end, end])

                break

        if not new_range:
            new_ranges.append([start, end])

    seed_ranges = new_ranges

print(min(seed_ranges)[0])
