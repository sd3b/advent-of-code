import re
from operator import add, mul

ops = {"+": add, "*": mul}
info = []

# parsing (bruh)

for monkey in open("input.txt").read().split("\n\n"):
	lines = monkey.split("\n")
	items = [int(x) for x in re.findall("\d+", lines[1])]
	operation = re.findall("Operation: new = old (\*|\+) (old|new|\d+)", lines[2])[0]
	test = int(lines[3].split()[-1])
	true = int(lines[4].split()[-1])
	false = int(lines[5].split()[-1])
	info.append({
		"items": items,
		"operation": operation,
		"test": test,
		"if_true": true,
		"if_false": false
	})

activity = [0] * len(info)

for round in range(20):
	for monkey_idx, monkey in enumerate(info):
		to_move = []
		idxs_to_throw = []

		for item_idx, item in enumerate(monkey["items"]):
			activity[monkey_idx] += 1
			sign, operand = monkey["operation"]

			if operand == "old":
				new = ops[sign](item, item)
			else:
				new = ops[sign](item, int(operand))

			new //= 3

			to_move.append((new, item_idx, monkey["if_true"] if new % monkey["test"] == 0 else monkey["if_false"]))
			idxs_to_throw.append(item_idx)

		for new, idx, dest in to_move:
			info[dest]["items"].append(new)

		# throw away items
		info[monkey_idx]["items"] = [item for idx, item in enumerate(info[monkey_idx]["items"]) if idx not in idxs_to_throw]

activity = sorted(activity)
print(activity[-1] * activity[-2])
