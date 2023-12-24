import re

def create_workflow(workflow_name, conditions):
    check = ""

    for idx, c in enumerate(conditions):
        try:
            cond, dest = c.split(":")
        except ValueError:
            pass

        if idx == 0:
            check += f"\tif {cond}: return {dest.upper()!r}\n"
        elif idx == len(conditions) - 1:
            check += f"\telse: return {c.upper()!r}\n"
        else:
            check += f"\telif {cond}: return {dest.upper()!r}\n"

    check = f"def {workflow_name.upper()}(x=0, m=0, a=0, s=0):\n" + check
    exec(check, globals())

workflows, ratings = open("input.txt").read().strip().split("\n\n")
new_ratings = [[int(x) for x in re.findall("\d+", r)] for r in ratings.split("\n")]

for w in workflows.split("\n"):
    workflow_name, conditions = re.findall(r"(.*){(.*)}", w)[0]
    conditions = conditions.split(",")
    create_workflow(workflow_name, conditions)

ratings_sum = 0

for x, m, a, s in new_ratings:
    new_function = "IN"

    while new_function not in "AR":
        new_function = eval(f"{new_function}({x}, {m}, {a}, {s})")

    if new_function == "A":
        ratings_sum += x + m + a + s

print("Part 1:", ratings_sum)
