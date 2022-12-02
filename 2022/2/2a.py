win = {"A": "Y", "B": "Z", "C": "X"}
translate = {"A": "X", "B": "Y", "C": "Z"}
shape_points = {"X": 1, "Y": 2, "Z": 3}
score = 0

for line in open("input.txt"):
    opponent, our_choice = line.strip().split()
    
    if win[opponent] == our_choice:
        score += 6
    elif translate[opponent] == our_choice:
        score += 3
    
    score += shape_points[our_choice]

print(score)