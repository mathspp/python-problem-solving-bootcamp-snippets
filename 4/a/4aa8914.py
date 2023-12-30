roll = 0
rolls_ = rolls
for _ in range(3):
    roll += rolls % 100 + 1
    rolls += 1
