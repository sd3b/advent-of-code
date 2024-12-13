import re
from sympy.solvers import solve
from sympy import Symbol, Eq
fro

results = re.findall(r"A: X\+(\d+), Y\+(\d+)\n.*X\+(\d+), Y\+(\d+)\n.*X=(\d+), Y=(\d+)", open("inputs/13.txt").read())
results = [map(int, vals) for vals in results]
a = Symbol("a")
b = Symbol("b")

ans = 0

for ax, ay, bx, by, x, y in results:
    result = solve([Eq(ax * a + bx * b, x + 10000000000000), Eq(ay * a + by * b, y + 10000000000000)])

    if all(n == int(n) for n in result.values()) and a in result.keys():
        ans += 3 * result[a] + result[b]

print(ans)
