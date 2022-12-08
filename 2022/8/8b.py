from collections import defaultdict as dd

grid = dd(lambda: -1)

file = [line.strip() for line in open("input.txt").readlines()]
height = len(file)
width = len(file[0])

for y in range(height):
    for x in range(width):
        grid[(y, x)] = int(file[y][x])

best = float("-inf")

for dy in range(1, height - 1):
    for dx in range(1, width - 1):
        top = [(y, dx) for y in range(dy)][::-1]
        bottom = [(y, dx) for y in range(dy + 1, height)]
        right = [(dy, x) for x in range(dx + 1, width)]
        left = [(dy, x) for x in range(dx)][::-1]
        current_tree = grid[(dy, dx)]
        
        scenic_score = 1

        for direction in (top, bottom, right, left):
            blocked_by_trees = 0

            for tree in direction:
                if grid[tree] < current_tree:
                    blocked_by_trees += 1
                else:
                    blocked_by_trees += 1
                    break

            scenic_score *= blocked_by_trees

        best = max(best, scenic_score)

print(best)