from functools import cache
from math import floor, log10

@cache
def blink(n, iters):
    s = str(n)

    if iters == 0:
        return 1
    elif n == 0:
        return blink(1, iters - 1)
    elif (length := floor(log10(n)) + 1) & 1:
        return blink(n * 2024, iters - 1)
    else:
        l, r = divmod(n, 10 ** (length // 2))
        return blink(l, iters - 1) + blink(r, iters - 1)

stones = list(map(int, open("inputs/11.txt").read().split()))

print("Part A: ", sum(map(lambda x: blink(x, 25), stones)))
print("Part B: ", sum(map(lambda x: blink(x, 75), stones)))
