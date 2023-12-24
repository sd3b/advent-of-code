from collections import OrderedDict

def HASH(string):
    hash_value = 0

    for char in string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256

    return hash_value

BOXES = [OrderedDict() for _ in range(256)]

for step in open("input.txt").readline().split(","):
    if step[-1] == "-":
        lens_label = step[:-1]
        box_no = HASH(lens_label)

        if lens_label in BOXES[box_no]:
            del BOXES[box_no][lens_label]
    else:
        lens_label, focal_length = step.split("=")
        focal_length = int(focal_length)
        box_no = HASH(lens_label)
        BOXES[box_no][lens_label] = focal_length

total_focusing_power = 0

for box_no, box in enumerate(BOXES, start = 1):
    for slot_no, focal_length in enumerate(box.values(), start = 1):
        total_focusing_power += box_no * slot_no * focal_length

print("Part 2:", total_focusing_power)
