from collections import defaultdict as dd

grid = dd(lambda: -1)

file = [line.strip() for line in open("input.txt").readlines()]
height = len(file)
width = len(file[0])
visible_trees = 0

for y in range(height):
    for x in range(width):
        grid[(y, x)] = int(file[y][x])

for dy in range(height):
    for dx in range(width):
        top = [(y, dx) for y in range(dy)]
        bottom = [(y, dx) for y in range(dy + 1, height)]
        right = [(dy, x) for x in range(dx + 1, width)]
        left = [(dy, x) for x in range(dx)]
        current_tree = grid[(dy, dx)]

        if any((
            all([grid[height] < current_tree for height in top if grid[height] != -1]),
            all([grid[height] < current_tree for height in bottom if grid[height] != -1]),
            all([grid[height] < current_tree for height in right if grid[height] != -1]),
            all([grid[height] < current_tree for height in left if grid[height] != -1]),
        )):
            visible_trees += 1

print(visible_trees)