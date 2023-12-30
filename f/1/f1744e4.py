with open(INPUT_FILE, "r") as f:
    positions = [int(line.strip().split()[-1]) for line in f]

scores = [0] * 2
player, rolls, die = 0, 0, 1

while max(scores) < 1000:
    ...
