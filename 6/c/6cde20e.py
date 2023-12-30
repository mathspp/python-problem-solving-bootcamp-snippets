def handle_closing_mismatch(char):
    api.make_request(char, ...)
    log.warning("Char not properly closed: " + char)
    return SYNTAX_SCORES[error_char]

# ...

if char != CLOSE_WITH[op]:
    scores += handle_closing_mismatch(char, ...)
    break
