import itertools

grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, "a", "b", "c"],
    ["d", "e", "f", "_"]
    ]

flat_list = list(itertools.chain.from_iterable(grid))

print(flat_list)


