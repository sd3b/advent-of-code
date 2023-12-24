grid = []
ans = 0
for y, line in enumerate(open("input.txt")):
    grid.append(line.strip())

    for x, char in enumerate(line):
        if char == "S":
            start = (y, x)

HEIGHT = len(grid)
WIDTH = len(grid[0])

stack = [(start, 0)]
visited = set()

while stack:
    state = stack.pop()

    if state in visited:
        continue

    visited.add(state)
    pos, steps = state

    if steps == 64:
        ans += 1
        continue

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        y, x = pos[0] + dy, pos[1] + dx

        if y in range(HEIGHT) and x in range(WIDTH) and grid[y][x] != "#":
            stack.append(((y, x), steps + 1))

print("Part 1:", ans)
