grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, "a", "b", "c"],
    ["d", "e", "f", "_"]
    ]

flat = [item for sublist in grid for item in sublist]

print(flat)
