with open(INPUT_FILE, "r") as f:
    positions = [int(line.strip().split()[-1]) for line in f]

scores = [0] * 2
player, rolls, die = 0, 0, 1

while max(scores) < 1000:
    # Player 1.
    roll = 0
    for _ in range(3):
        roll += die
        die += 1
        if die > 100:
            die = 1
        rolls += 1
    for _ in range(roll):
        p1 += 1
        if p1 > 10:
            p1 = 1
    s1 += p1
    if s1 >= 1000:
        print(s2 * rolls)
        break
