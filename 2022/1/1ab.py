elfs = []

for elf in open("input.txt").read().split("\n\n"):
	calories = sum(map(int, elf.split()))
	elfs.append(calories)

elfs.sort()
print("Part A:", elfs[-1])
print("Part B:", sum(elfs[-3:]))