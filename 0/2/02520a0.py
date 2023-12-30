folded = set(points)
for coord, value in folds:
    int_value = int(value)
    folded = {fold_point(point, coord, int_value) for point in folded}
