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

ROW_NAMES = ("first", "second", "third", "fourth", "fifth" )