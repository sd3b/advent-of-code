import re
from math import prod
from tqdm import tqdm

WIDTH, HEIGHT = 101, 103

data = re.findall("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", open("inputs/14.txt").read())
robots = [list(map(int, r)) for r in data]

for tick in tqdm(range(int(10e5))):
    for idx, (px, py, vx, vy) in enumerate(robots):
        robots[idx][0] = (px + vx) % WIDTH
        robots[idx][1] = (py + vy) % HEIGHT

quad_count = [0, 0, 0, 0]

for (px, py, _, _) in robots:
    if px != WIDTH // 2 and py != HEIGHT // 2:
        lsb = px < WIDTH / 2
        msb = py < HEIGHT / 2
        idx = msb * 2 + lsb
        quad_count[idx] += 1

print("Part A:", prod(quad_count))
