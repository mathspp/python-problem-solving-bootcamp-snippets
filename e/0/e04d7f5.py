for idx, val in enumerate(reversed(beginning)):
    if isinstance(val, int):
        beginning[-idx - 1] += left  # <-
        break
for idx, val in enumerate(rest):
    if isinstance(val, int):
        rest[idx] += right           # <-
        break
