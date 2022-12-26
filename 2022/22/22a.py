import re
from collections import defaultdict as dd

grid_data, instructions = open("input.txt").read().split("\n\n")
instructions = re.findall("(\d+)(R|L)", instructions)
grid = dd(dict)

for y, line in enumerate(grid_data.split("\n")):
    for x, char in enumerate(line):
        if char != " ": # no need to store whitespace
            grid[y][x] = char

y, x = 0, grid_data.index(".")
dir_ = 0

for mv_by, rotate in instructions:
    for _ in range(int(mv_by)):
        dy = [0, 1, 0, -1][dir_]
        dx = [1, 0, -1, 0][dir_]

        py, px = y + dy, x + dx

        if px > x and px > max(grid[y]): # right
            px = min(grid[y])
        elif px < x and px < min(grid[y]): # left
            px = max(grid[y])
        elif py > y and py > max(key for key in grid if x in grid[key]): # down
            py = min(key for key in grid if x in grid[key])
        elif py < y and py < min(key for key in grid if x in grid[key]): # up
            py = max(key for key in grid if x in grid[key])

        if grid[py][px] == "#":
            break

        y, x = py, px

    dir_ += 1 if rotate == "R" else -1
    dir_ %= 4

print((y + 1) * 1000 + (x + 1) * 4 + dir_)
