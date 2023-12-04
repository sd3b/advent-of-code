from collections import defaultdict as dd

data = open("input.txt").readlines()
x, y = 0, 0
parts = []
adj = dd(list)

while y < len(data) and x < len(data[y]):
    if data[y][x] == "\n":
        y += 1
        x = 0

    if data[y][x].isdigit():
        current_part_number = ""
        adj_to_symbol = False

        while x < len(data[y]) and data[y][x].isdigit():
            current_part_number += data[y][x]
            neighbours = [(y, x - 1), (y, x + 1), (y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]
            x += 1

            for coord in neighbours:
                if 0 <= coord[0] < len(data[y]) and 0 <= coord[1] < len(data):
                    if (char := data[coord[0]][coord[1]]) not in "0123456789.":
                        adj_to_symbol = True

                    if char == "*":
                        adj_to_star = True
                        gear_coord = coord

        if adj_to_star:
            adj[gear_coord[0], gear_coord[1]].append(int(current_part_number))
            adj_to_star = False

        if adj_to_symbol:
            parts.append(int(current_part_number))
            adj_to_symbol = False
    else:
        x += 1

total = sum(gear[0] * gear[1] for gear in adj.values() if len(gear) == 2)

print("Part 1:", sum(parts))
print("Part 2:", total)
