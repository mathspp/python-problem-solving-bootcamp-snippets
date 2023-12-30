for _ in range(256):
    fish_pop[7] += fish_pop[0]               # updating births
    fish_pop = fish_pop[1:] + [fish_pop[0]]  # cycling
