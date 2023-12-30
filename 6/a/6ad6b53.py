roll = 0
rolls_ = rolls
for _ in range(3):
    roll += rolls % 100 + 1
    rolls += 1
assert roll == ((rolls_ % 100 + 1) + ((rolls_ + 1) % 100 + 1) + ((rolls_ + 2) % 100 + 1))
