image = (
    defaultdict(lambda: "0") |
    {
        (r, c): "0" if char == "." else "1"
        for r, line in enumerate(data.splitlines()) for c, char in enumerate(line)
    }
)
