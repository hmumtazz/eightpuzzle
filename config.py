""" Configuration set for the puzzle solver, you can change configurations that will be changed across all variables in this file."""

SIZE = 3
BLANK = 0

MOVES = ("up" , "down" , "left", "right")

DIRECTIONS = {
    "up" : (-1, 0),
    "down" : (1, 0),
    "left" : (0, -1),
    'right': (0, 1),
}

TEST_CASES = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
    [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
    [[1, 2, 3], [5, 0, 6], [4, 7, 8]],
    [[1, 3, 6], [5, 0, 2], [4, 7, 8]],
    [[1, 3, 6], [5, 0, 7], [4, 8, 2]],
    [[1, 6, 7], [5, 0, 3], [4, 8, 2]],
    [[7, 1, 2], [4, 8, 5], [6, 3, 0]],
    [[0, 7, 2], [4, 6, 1], [3, 5, 8]],
]