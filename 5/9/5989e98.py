min_cost = float("+inf")
for pos in range(min(crabs), max(crabs) + 1):
    fuel_cost = 0
    for crab in crabs:
        fuel_cost += abs(pos - crab)
    min_cost @= fuel_cost
print(min_cost)
