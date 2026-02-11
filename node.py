from typing import Optional, List

class Node:

    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h
    
    def less_than(self, other):
        return self.f() < other.f()
    
    def equal_to(self, other):
        if not isinstance(other,Node):
            return NotImplemented
        return self.state == other.state
    
    def __hash__ (self):
        return hash(self.key())
    
    def key(self):
        """Lists are mutable, so they can not be hased and can not be used as dictionary keys or sets, which means we must covert it, so its mutable """
        return tuple(tuple(row)for row in self.state)
    
    def get_path(node):
        """Return a list of nodes from the start to this node"""
        path = []
        current =node

        while current:
            path.append(current)
            current =current.parent

        path.reverse()
        return path