import matplotlib.path

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

delta = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST]
}

maze = []

for y, line in enumerate(open("input.txt")):
    maze.append(line.strip())

    for x, char in enumerate(line.strip()):
        if char == "S":
            sy = y
            sx = x

stack = []

for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    char = maze[sy + dy][sx + dx]

    if char in delta:
        for dyy, dxx in delta[char]:
            if dx == -dxx and dy == -dyy: # check if pipe connected (go back and forth)
                stack.append((1, (sy + dy, sx + dx)))

distances = {(sy, sx): 0}

while stack:
    distance, (y, x) = stack.pop()

    if (y, x) in distances:
        continue

    distances[(y, x)] = distance

    for dy, dx in delta[maze[y][x]]:
        stack.append((distance + 1, (y + dy, x + dx)))

print("Part 1:", (max(distances.values()) + 1) // 2)
nodes = list(distances.keys())

loop = matplotlib.path.Path(nodes)
nodes = set(nodes)

enclosed_tiles = 0

for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[0]) - 1):
        if (y, x) not in nodes and loop.contains_point((y, x)):
            enclosed_tiles += 1

print('Part 2:', enclosed_tiles)
