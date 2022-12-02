win = {"A": "Y", "B": "Z", "C": "X"}
lose = {"A": "Z", "B": "X", "C": "Y"}
translate = {"A": "X", "B": "Y", "C": "Z"}
shape_points = {"X": 1, "Y": 2, "Z": 3}
score = 0

for line in open("input.txt"):
    opponent, hint = line.strip().split()
    
    if hint == "X":
        score += shape_points[lose[opponent]]
    elif hint == "Y":
        score += 3 + shape_points[translate[opponent]]
    else:
        score += 6 + shape_points[win[opponent]]

print(score)