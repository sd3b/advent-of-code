from collections import deque, defaultdict as dd

grid = dict()

starting_positions = []

for line_no, line in enumerate(open("input.txt")):
	for idx, c in enumerate(line.strip()):
		if c == "E":	c = "z"; target = (line_no, idx)
		elif c == "S":	c = "a"; start = (line_no, idx)

		if c == "a":	starting_positions.append((line_no, idx))
		
		grid[(line_no, idx)] = ord(c)

minimum = float("inf")

for start in starting_positions:
	queue = deque()
	queue.append((start, 0))
	visited = set()

	while queue:
		selected, dist = queue.pop()
	
		if selected == target:
			minimum = min(minimum, dist)
			# print("Distance:", minimum)
			break
	
		y, x = selected
	
		if selected in visited:	continue
		visited.add(selected)
	
		for neighbour in ((y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)):
			if neighbour in grid:
				if grid[neighbour] - grid[selected] <= 1:
					queue.appendleft((neighbour, dist + 1))

print("Minimum:", minimum)
