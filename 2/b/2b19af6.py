error_char = None
for char in line:
    if char in OPENING:
        stack.put(char)
    elif char in CLOSING:
        op = stack.get()
        if char != CLOSE_WITH[op]:
            error_char = char  # Update info regarding the error.
            break
if error_char is not None:  # Check if the error character was set.
    scores += SYNTAX_SCORES[error_char]
    api.make_request(char, ...)
    log.warning("Char not properly closed: " + char)
