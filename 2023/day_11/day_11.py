from itertools import combinations

universe = [list(line.strip()) for line in open("input.txt")]


def expand(expansion):
    expansion -= 1
    
    count = 0
    galaxies = []
    column_offset = []
    row_offset = 0

    for y in list(zip(*universe)):
        column_offset.append(count)

        if "#" not in y:
            count += expansion

    for y, line in enumerate(universe):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((y + row_offset, x + column_offset[x]))

        if "#" not in line:
            row_offset += expansion

    total = 0

    for galaxy_1, galaxy_2 in combinations(galaxies, 2):
        total += abs(galaxy_2[0] - galaxy_1[0]) + abs(galaxy_2[1] - galaxy_1[1])

    return total

print("Part 1:", expand(2))
print("Part 1:", expand(1000000))