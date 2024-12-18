from collections import deque

all_corrupt = []
bound = 70
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for idx, line in enumerate(open("inputs/18.txt")):
    all_corrupt.append(tuple(map(int, line.split(","))))

def steps(idx):
    corrupt = set(all_corrupt[:idx + 1])
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == (bound, bound):
            return steps

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
        
            if 0 <= nx <= bound and 0 <= ny <= bound and (nx, ny) not in corrupt:
                corrupt.add((nx, ny))
                queue.append((nx, ny, steps + 1))

l, r = 0, len(all_corrupt) - 1

while l < r:
    mid = (l + r) // 2
    
    if not steps(mid):  r = mid
    elif r - mid == 1:  break
    else:               l = mid

print("Part 1:", steps(1024))
print("Part 2:", ",".join(map(str, all_corrupt[r])))