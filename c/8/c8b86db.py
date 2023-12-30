if dep < prev_dep:  # If the depth decreased, it corresponds to closing `"]"`.
    for _ in range(prev_dep - dep):
        combine(sub_magnitudes)
