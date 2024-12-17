from heapq import heappush, heappop

f = open("inputs/16.txt")
grid = []

for y, line in enumerate(f):
    grid.append(line)

    for x, char in enumerate(line):
        if char == "S":     pq = [(0, y, x, 0, bytes([y, x]))]
        elif char == "E":   dest = (y, x)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
distances = {}

best_score = float("inf")
best_paths = bytes()

# y and x should fit in a byte each

while pq:
    score, y, x, idx, path = heappop(pq)
    distances[(y, x, idx)] = score

    if score > best_score:  break

    if (y, x) == dest:
        best_score = min(best_score, score)
        best_paths += path

    for jdx in [(idx - 1) % 4, idx, (idx + 1) % 4]:
        dy, dx = dirs[jdx]
        ny, nx = y + dy, x + dx
        new_score = score + 1 + 1000 * (1 if idx != jdx else 0)

        if grid[ny][nx] != "#" and new_score < distances.get((ny, nx, jdx), float("inf")):
            heappush(pq, (new_score, ny, nx, jdx, path + bytes([ny, nx])))

print("Part A:", best_score)
coords = set(best_paths[idx:idx+2] for idx in range(0, len(best_paths), 2))
print("Part B:", len(coords))