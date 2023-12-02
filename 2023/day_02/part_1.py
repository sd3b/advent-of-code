import re

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total_valid_ids = 0

for current_id, line in enumerate(open("input.txt"), start = 1):
    id_valid = True
    matches = re.findall("(\d+) (red|green|blue)", line)

    for n_cubes, colour in matches:
        if int(n_cubes) > LIMITS[colour]:
            id_valid = False
            continue

    if id_valid:
        total_valid_ids += current_id

print("Part 1:", total_valid_ids)
