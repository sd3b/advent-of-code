import re

def part_a():
    matches = re.findall(r"mul\((\d+),(\d+)\)", f)
    print("Part A:", sum(int(x) * int(y) for x, y in matches))

def part_b():
    enabled = True
    matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", f)
    total = 0

    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            x, y = map(int, re.findall(r"mul\((\d+),(\d+)\)", m)[0])
            total += x * y

    print("Part B:", total)

f = open("inputs/3.txt").read()

part_a()
part_b()
