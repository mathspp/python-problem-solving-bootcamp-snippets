binary += (
    image[r + dr][c + dc]
    if 0 <= r + dr < len(image) and 0 <= c + dc < len(image[0])
    else padding
)
