from collections import defaultdict as dd
import re

ROCK = "#"
AIR = "."
SAND = "o"
bottom = float("-inf")

cave = dd(lambda: AIR)

# Load rocks

for l in open("input.txt").readlines():
    path = l.strip().split(" -> ")
    
    for idx in range(1, len(path)):
        prev_x, prev_y = [int(n) for n in path[idx - 1].split(",")]
        x, y = [int(n) for n in path[idx].split(",")]
        dx = dy = False

        if prev_x != x:
            rock_range = range(prev_x, x + 1) if prev_x < x else range(prev_x, x - 1, -1)
            dx = True
        elif prev_y != y:
            rock_range = range(prev_y, y + 1) if prev_y < y else range(prev_y, y - 1, -1)
            dy = True

        for rock in rock_range:
            if dx:      cave[(rock, y)] = ROCK; bottom = max(bottom, y)
            elif dy:    cave[(x, rock)] = ROCK; bottom = max(bottom, rock)

def print_grid():
    for y in range(10):
        for x in range(494, 504):
            print(cave[(x, y)], end = "")
        print()

def get_possible_moves(x, y):
    if cave[(x, y + 1)] == AIR and y + 1:
        return (x, y + 1)
    elif cave[(x - 1, y + 1)] == AIR:
        return (x - 1, y + 1)
    elif cave[(x + 1, y + 1)] == AIR:
        return (x + 1, y + 1)

units = 0
overflowing = False

while not overflowing:
    pos_x, pos_y = (500, 0) # start at source
    can_move = True

    while can_move:
        move = get_possible_moves(pos_x, pos_y)

        if move is not None:
            pos_x, pos_y = move

            if pos_y > bottom: # overflowing
                overflowing = True
                can_move = False

        else:   can_move = False

    cave[(pos_x, pos_y)] = SAND
    
    if not overflowing and not can_move:
        units += 1

print(units)
