"""Problem class for the n-puzzle"""

from config import SIZE, BLANK, MOVES

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