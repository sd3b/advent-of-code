import re
import sympy as sym

results = re.findall(r"A: X\+(\d+), Y\+(\d+)\n.*X\+(\d+), Y\+(\d+)\n.*X=(\d+), Y=(\d+)", open("inputs/13.txt").read())
results = [map(int, vals) for vals in results]
a = sym.Symbol("a")
b = sym.Symbol("b")

ans = 0

for ax, ay, bx, by, x, y in results:
    result = sym.solvers.solve([sym.Eq(ax * a + bx * b, x + 10000000000000), sym.Eq(ay * a + by * b, y + 10000000000000)])

    if all(n == int(n) for n in result.values()):
        ans += 3 * result[a] + result[b]

print(ans)
