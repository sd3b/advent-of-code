import re
from math import floor, ceil

with open("input.txt") as f:
    times = map(int, re.findall("\d+", f.readline()))
    distances = map(int, re.findall("\d+", f.readline()))

ways = 1

for t, d in zip(times, distances):
    x_1 = (t - (t**2 - 4 * d)**.5) / 2
    x_2 = (t + (t**2 - 4 * d)**.5) / 2

    n = floor(x_2) - ceil(x_1) + 1

    if x_1.is_integer():  n -= 1
    if x_2.is_integer():  n -= 1

    ways *= n

print("Part 1:", ways)
