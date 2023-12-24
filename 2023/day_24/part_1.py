import numpy as np
import re
from itertools import combinations

no_intersections = 0
hailstones = []

for line in open("input.txt"):
    rx, ry, _, vx, vy, _ = map(int, re.findall("-?\d+", line))
    hailstones.append((rx, ry, vx, vy))

for (r_ax, r_ay, v_ax, v_ay), (r_bx, r_by, v_bx, v_by) in combinations(hailstones, 2):
    r_a, r_b = np.array([r_ax, r_ay]), np.array([r_bx, r_by])
    v_a, v_b = np.array([v_ax, v_ay]), np.array([v_bx, v_by])

    velocities = np.array([
        [v_ax, -v_bx],
        [v_ay, -v_by]
    ])

    positions = np.array([
        [r_bx - r_ax],
        [r_by - r_ay]
    ])

    if np.linalg.det(velocities) == 0:
        continue

    params = np.matmul(np.linalg.inv(velocities), positions)

    if (params < 0).any():
        continue

    intersection_a = r_a + params[0] * v_a
    intersection_b = r_b + params[1] * v_b

    if np.allclose(intersection_a, intersection_b):
        if all(200000000000000 <= p <= 400000000000000 for p in intersection_a):
            no_intersections += 1

print("Part 1:", no_intersections)
