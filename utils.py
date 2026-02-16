from config import BLANK, TEST_CASES


def print_state(state):
    for row in state:
        print(" ".join(str(t) if t != BLANK else "b" for t in row))

def print_solution(node):
    path = node.get_path()
    print(f"\nSolution: {len(path) - 1}")
    for step, n in enumerate(path):
        if n.action:
            print(f"\nStep {step}: move {n.action}")
        else:
            print("\nInitial move:")
        print_state(n.state)

def trace(node):
    print(f"The best state to expand with g(n) = {node.g} "
          f"and h(n) = {node.h} is")
    print_state(node.state)
    print()
        

def print_summary(result, expanded, max_q):
    if result == "failure":
        print("No solution found.")
    else:
        print("\nGoal state reached!")
        print(f"Solution depth : {result.g}")
        print(f"Nodes expanded : {expanded}")
        print(f"Max queue size : {max_q}")
        print_solution(result)


def read_puzzle():
    print("Welcome to the n-Puzzle ssolver!")
    print('Type "1" to use a default , "2" to enter your own, or "3" to pick a test case.\n')
    choice = input("Enter choice: ").strip()

    if choice == "2":
        size = int(input("Enter puzzle size (e.g. 3 for 8-puzzle, 4 for 15-puzzle): ").strip())
        print(f"Enter your puzzle, using 0 to represent the blank.")
        print(f"Enter each row as {size} spaceseparated numbers.\n")
        puzzle = []
        for i in range(size):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            assert len(row) == size, f"Expected {size} numbers"
            puzzle.append(row)
        return puzzle, size
    elif choice == "3":
        print("\nTest cases:")
        for i, tc in enumerate(TEST_CASES, 1):
            flat = "/".join("".join(str(t) for t in row) for row in tc)
            print(f"  {i}. {flat}")
        pick = int(input(f"\nPick a test case (1-{len(TEST_CASES)}): ").strip())
        puzzle = TEST_CASES[pick - 1]
        print(f"\nUsing test case {pick}:")
        print_state(puzzle)
        print()
        return puzzle, 3
    else:
        puzzle = [
            [1, 2, 3],
            [5, 0, 6],
            [4, 7, 8],
        ]
        print("Using default :")
        print_state(puzzle)
        print()
        return puzzle, 3

def read_algorithm():
    print("\nSelect an algorithm:")
    print("  1. Uniform Cost Search")
    print("  2. A* with Misplaced Tile Heuristic")
    print("  3. A* with Manhattan Distance Heuristic\n")
    return input("Enter choice (1/2/3): ").strip()