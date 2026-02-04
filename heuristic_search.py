"""Heautistic functions for A*"""

def h_zero(state,goal,size):
    return 0


def h_mispalced(state, goal,size):

    coutn = 0

    for r in range(size):
        for c in range(size):
            tile = state[r][c]
            if tile != 0 and tile != goal[r][c]:
                count+=1
    return count

def h_manhattan(state,goal,size):

    goal_pos={}
    
    for r in range(size):
        for c in range(size):
            goal_pos[goal[r][c]]= (r,c)

    total = 0

    for r in range(size):
        for c in range(size):
            tile = state[r][c]
            if tile != 0:
                gr,gc = goal_pos[tile]
                total += abs(r-gr) + abs(c-gc)

    return total

HEURISTICS = {
    "1" : (h_zero, "Uniform Cost Search"),
    "2" : (h_mispalced, "A* with Misplaced Heuristic"),
    "3" : (h_manhattan, "A* with Manhattan Heuristic")  
         
    }

def get_heuristic(choice):

    assert choice in HEURISTICS, f"Invalid choice: {choice} "
    return HEURISTICS[choice]