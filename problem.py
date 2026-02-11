"""Problem class for the n-puzzle"""

from config import SIZE, BLANK, MOVES,DIRECTIONS

class Problm:

    def __init__ (self,start,size=SIZE):
        assert len(start) == size, f"Expected {size} rows"
        for row in start:
            assert len(row) == size, f"Expected {size} columns"

        self.start = start
        self.size = size
        self.goal = self._make_goal()
        self.moves = MOVES


    def _make_goal(self):
        goal = []
        num = 1
        total = self.size * self.size

        for i in range(self.size):
            row = []
            for j in range(self.size):
                pose = i * self.size +j
                if pose == total-1:
                    row.append(BLANK)
                else:
                    row.append(num)
                    num+=1
            goal.append(row)
        return goal
    
    def is_goal(self,state):
        return state == self.goal

    def find_blank(self,state):
        for r in range(self.size):
            for c in range(self.size):
                if state[r][c] == BLANK:
                    return (r,c)
                
        assert False, "sorry, no blank tile found!"

    def successors(self,state):
        results = []
        blank_r, blank_c = self.find_blank(state)

        for action in self.moves:
            dr, dc = DIRECTIONS[action]
            new_r = blank_r + dr
            new_c = blank_c + dc

            if 0 <= new_r < self.size and 0 <= new_c < self.size:
                new_state = [row[:] for row in state]
                new_state[blank_r][blank_c] = new_state[new_r][new_c]
                new_state[new_r][new_c] = BLANK
                results.append((action, new_state))

        return results