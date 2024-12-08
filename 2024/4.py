grid = open("inputs/4.txt").read().split("\n")
height, width = len(grid), len(grid[0])
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

xmas_count = 0
target = "XMAS"
part_a = part_b = 0

for y in range(height):
    for x in range(width):
        if 0 <= y <= height - 3 and 0 <= x <= width - 3 and all([
            grid[y + 1][x + 1] == "A",
            grid[y][x] != grid[y + 2][x + 2],
            grid[y + 2][x] != grid[y][x + 2],
            grid[y][x] not in "AX",
            grid[y][x + 2] not in "AX",
            grid[y + 2][x] not in "AX",
            grid[y + 2][x + 2] not in "AX"
        ]):
            part_b += 1

        for dy, dx in dirs:
            flag = True

            for idx in range(len(target)):
                ny, nx = y + dy * idx, x + dx * idx

                if not (0 <= ny < height and 0 <= nx < width and grid[ny][nx] == target[idx]):
                    flag = False
                    break

            if flag:
                part_a += 1

print("Part A:", part_a)
print("Part B:", part_b)
