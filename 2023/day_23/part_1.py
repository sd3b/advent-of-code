grid = [line.strip() for line in open("input.txt")]
HEIGHT = len(grid)
WIDTH = len(grid[0])

stack = [((0, 1), (1, 0), frozenset())]
visited = set()

SLOPES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

max_dist = -1

while stack:
    state = stack.pop()

    if state in visited:
        continue

    current_pos, current_dir, visited_tiles = state

    if current_pos == (HEIGHT - 1, WIDTH - 2):
        max_dist = max(max_dist, len(visited_tiles))

    for dy, dx in SLOPES.values():
        new_y, new_x = new_pos = current_pos[0] + dy, current_pos[1] + dx

        if new_y in range(HEIGHT) and new_x in range(WIDTH):
            char = grid[new_y][new_x]

            if char == "#" or new_pos in visited_tiles or (char in SLOPES and SLOPES[char] != (dy, dx)):
                continue

            stack.append((new_pos, (dy, dx), visited_tiles | {new_pos}))
            visited.add((current_pos, current_dir))

print("Part 1:", max_dist)
