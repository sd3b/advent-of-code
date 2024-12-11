from functools import cache
from math import floor, log10

@cache
def blink(n, iters):
    s = str(n)

    if iters == MAX_ITERS:
        return 1

    if n == 0:
        return blink(1, iters + 1)
    elif (length := floor(log10(n)) + 1) & 1:
        return blink(n * 2024, iters + 1)
    else:
        l, r = divmod(n, 10 ** (length // 2))
        return blink(l, iters + 1) + blink(r, iters + 1)

stones = list(map(int, open("inputs/11.txt").read().split()))

MAX_ITERS = 25
print("Part A:", sum(map(lambda x: blink(x, 0), stones)))

blink.cache_clear()
MAX_ITERS = 75
print("Part B:", sum(map(lambda x: blink(x, 0), stones)))