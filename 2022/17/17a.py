from collections import defaultdict as dd

AIR = ".."
chamber = dd(lambda: AIR)
highest_rock = 0

rocks = (
    lambda : tuple((highest_rock + 3, x) for x in range(2, 6)), # horizontal line
    lambda : tuple((highest_rock + 4, x) for x in range(2, 5)) + ((highest_rock + 3, 3), (highest_rock + 5, 3)), # cross
    lambda : tuple((highest_rock + 3, x) for x in range(2, 5)) + ((highest_rock + 4, 4), (highest_rock + 5, 4)), # L (rev.)
    lambda : tuple((y, 2) for y in range(highest_rock + 3, highest_rock + 7)), # vertical line
    lambda : ((highest_rock + 3, 2), (highest_rock + 3, 3), (highest_rock + 4, 2), (highest_rock + 4, 3)) # square
)

order = 0

class Rock:
    def __init__(self, shape):
        self.shape = shape

    def can_move_down(self):
        return all(chamber[(y - 1, x)] == AIR and y > 0 for y, x in self.shape)

    def can_move_right(self):
        return all(chamber[(y, x + 1)] == AIR and x < 6 for y, x in self.shape)

    def can_move_left(self):
        return all(chamber[(y, x - 1)] == AIR and x > 0 for y, x in self.shape)


def chamber_print():
    print()
    for y in range(highest_rock + 5, -1, -1):
        print("\t|", end = "")

        for x in range(7):
            print(chamber[(y, x)], end = "")

        print("|")

    print("\t+--------------+")

instructions = open("input.txt").read().strip()
i = 0

shape = rocks[order]()
r = Rock(shape)
at_rest = 0

colors = [f"\033[{color}m██\033[0m" for color in range(31, 36)]

while at_rest != 2022:
    if instructions[i] == ">":
        if r.can_move_right():
            r.shape = [(y, x + 1) for y, x in r.shape]
    elif instructions[i] == "<":
        if r.can_move_left():
            r.shape = [(y, x - 1) for y, x in r.shape]

    i += 1
    i %= len(instructions)

    if r.can_move_down():
        r.shape = [(y - 1, x) for y, x in r.shape]
    else:
        at_rest += 1
        h = max(r.shape, key = lambda unit: unit[0])[0] + 1
        highest_rock = max(highest_rock, h)

        for y, x in r.shape:
            chamber[(y, x)] = colors[order]

        order += 1
        order %= 5
        shape = rocks[order]()
        r = Rock(shape)

chamber_print()
print(f"Peak: {highest_rock}")
