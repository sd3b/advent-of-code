from operator import mul, add, sub, truediv as div
from copy import deepcopy

ops = {"+": add, "-": sub, "*": mul, "/": div}

def evaluate(monkey):
    if monkey in vals:
        return vals[monkey]

    job = jobs[monkey]

    if job.strip().isdigit():
        vals[monkey] = int(job)
        return vals[monkey]

    a, op, b = job.split()
    a_val = evaluate(a)
    b_val = evaluate(b)

    vals[monkey] = ops[op](a_val, b_val)

    return vals[monkey]


# use binary search to get the difference as small as possible

start = 0
end = 2 ** 64

j = {}

for line in open("input.txt").readlines():
    monkey, job = line.strip().split(":")
    j[monkey] = job

p, _, q = j["root"].split() # two monkeys connected to root
diff = -1

while diff != 0:
    jobs = deepcopy(j)
    vals = {}
    mid = start + (end - start) // 2
    jobs["humn"] = str(mid)
    diff = evaluate(p) - evaluate(q)

    if diff < 0:     end = mid
    elif diff > 0:   start = mid

print(mid)
