UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

forwards_mirror = {RIGHT: UP, UP: RIGHT, LEFT: DOWN, DOWN: LEFT}
backwards_mirror = {RIGHT: DOWN, DOWN: RIGHT, UP: LEFT, LEFT: UP}
grid = [line.strip() for line in open("input.txt")]
HEIGHT, WIDTH = len(grid), len(grid[0])

def move(pos, dir):
    return tuple(a + b for a, b in zip(pos, dir))

def part_1(start_pos, start_dir):
    beams = [(start_pos, start_dir)]
    history = set()
    energised = set()

    while beams:
        pos, dir = beams.pop()
        pos = move(pos, dir)
        y, x = pos

        if y in range(HEIGHT) and x in range(WIDTH) and (pos, dir) not in history:
            energised.add(pos)
            history.add((pos, dir))

            if grid[y][x] == "/":
                beams.append((pos, forwards_mirror[dir]))
                continue
            elif grid[y][x] == "\\":
                beams.append((pos, backwards_mirror[dir]))
                continue
            elif grid[y][x] == "|" and dir in (RIGHT, LEFT):
                beams.append((pos, UP))
                beams.append((pos, DOWN))
                continue
            elif grid[y][x] == "-" and dir in (UP, DOWN):
                beams.append((pos, LEFT))
                beams.append((pos, RIGHT))
                continue

            beams.append((pos, dir))

    return len(energised)

print("Part 1:", part_1((0, -1), RIGHT))
energy = 0

for x in range(WIDTH):  energy = max(energy, part_1((-1, x), DOWN))
for x in range(WIDTH):  energy = max(energy, part_1((HEIGHT, x), UP))
for y in range(HEIGHT): energy = max(energy, part_1((y, -1), RIGHT))
for y in range(HEIGHT): energy = max(energy, part_1((y, WIDTH), LEFT))

print("Part 2:", energy)