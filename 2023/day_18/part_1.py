from collections import deque

DIR = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
pos = (0, 0)
min_y, min_x = float('inf'), float('inf')
max_y, max_x = float('-inf'), float('-inf')
lagoon = set()

for line in open("input.txt"):
    d, n, _ = line.strip().split()
    dir = DIR[d]
    n = int(n)

    match d:
        case "U":   min_y = min(min_y, pos[0] - n)
        case "D":   max_y = max(max_y, pos[0] + n)
        case "L":   min_x = min(min_x, pos[1] - n)
        case "R":   max_x = max(max_x, pos[1] + n)

    for _ in range(n):
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        lagoon.add(pos)

queue = deque()
queue.appendleft(((min_y + max_y) // 2, (min_x + max_x) // 2))
lagoon.add(queue[0])

while queue:
    y, x = queue.popleft()

    for dy, dx in DIR.values():
        new_pos = (y + dy, x + dx)

        if new_pos not in lagoon and new_pos[0] in range(min_y, max_y + 1) and new_pos[1] in range(min_x, max_x + 1):
            lagoon.add(new_pos)
            queue.append(new_pos)

print("Part 1:", len(lagoon))
