from queue import PriorityQueue

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

grid = [[int(n) for n in line.strip()] for line in open("input.txt")]
HEIGHT = len(grid)
WIDTH = len(grid[0])

def is_within_grid(pos):
    return pos[0] in range(HEIGHT) and pos[1] in range(WIDTH)

def dijkstra():
    visited = set()
    queue = PriorityQueue()
    queue.put((0, (0, 0), (0, 0), 0))

    while queue:
        heat_loss, pos, dir, steps = queue.get()
        y, x = pos

        if pos == (HEIGHT - 1, WIDTH - 1) and steps >= 4:
            return heat_loss

        if (pos, dir, steps) in visited:
            continue

        visited.add((pos, dir, steps))

        for dy, dx in (UP, DOWN, LEFT, RIGHT):
            if (dy == -dir[0] and dx == -dir[1]):
                continue
            
            if (dy, dx) == dir and steps >= 10:
                continue

            new_pos = (y + dy, x + dx)

            if is_within_grid(new_pos):
                if (dy, dx) == dir and steps < 4:
                    queue.put((
                        heat_loss + grid[y + dy][x + dx],
                        new_pos,
                        dir,
                        steps + 1
                    ))
                elif steps >= 4 or dir == (0, 0):
                    queue.put((
                        heat_loss + grid[y + dy][x + dx],
                        new_pos,
                        (dy, dx),
                        steps + 1 if (dy, dx) == dir else 1
                    ))

print("Part 2:", dijkstra())
