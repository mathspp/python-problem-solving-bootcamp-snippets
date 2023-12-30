roll = 0
for _ in range(3):
    rolls += 1
    roll += (rolls - 1) % 100 + 1
