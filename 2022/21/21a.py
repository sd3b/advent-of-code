from operator import mul, add, sub, truediv as div

ops = {"+": add, "-": sub, "*": mul, "/": div}
jobs = {}

for line in open("input.txt").readlines():
    monkey, job = line.strip().split(":")
    jobs[monkey] = job

vals = {}

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

print(evaluate("root"))
