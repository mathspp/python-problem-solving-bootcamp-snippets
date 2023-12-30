for line in lines:
    hints, values = map(str.split, line.split(" | "))
    for ordering in ALL_ORDERINGS:
        found_all = True
        for hint in hints:
            if translate(ordering, hint) not in DIGIT_SEGMENTS:
                found_all = False
                break
        if found_all:
            # If we got here, this is the correct ordering.
            digit_ints = [SEGMENTS.index(translate(ordering, value)) for value in values]
            acc += int("".join(str(digit) for digit in digit_ints))
            break
