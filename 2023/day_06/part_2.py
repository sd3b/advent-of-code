import re
from math import floor, ceil

with open("input.txt") as f:
    times = re.findall("\d+", f.readline())
    distances = re.findall("\d+", f.readline())

t = int("".join(times))
d = int("".join(distances))

x_1 = (t - (t**2 - 4 * d)**.5) / 2
x_2 = (t + (t**2 - 4 * d)**.5) / 2

ways = floor(x_2) - ceil(x_1) + 1

if x_1.is_integer():  ways -= 1
if x_2.is_integer():  ways -= 1

print("Part 2:", ways)
