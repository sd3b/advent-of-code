from z3 import Solver, Int, Abs
import re

max_ = 4000000

s = Solver()
x = Int("dx")
y = Int("dy")
sol = Int("sol")

s.add(0 <= x, x <= max_)
s.add(0 <= y, y <= max_)
s.add(sol == max_ * x + y)

for line in open("input.txt"):
	sx, sy, bx, by = map(int, re.findall("-?\d+", line))
	dist = abs(sx - bx) + abs(sy - by)
	s.add(Abs(sx - x) + Abs(sy - y) > dist)

s.check()
print(s.model())
