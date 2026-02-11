"""Search algoirthm for n-puzzle"""


import heapq
from node import Node

def make_node(state, parent=None, action=None, g=0, h=0):
    return Node(state, parent,action,g,h)

def make_queue(node):
    queue = []
    heapq.heappush(queue,node)
    return queue

def remove_front_node(nodes):
    return heapq.heappop(nodes)

def empty_nodes(nodes):
    return len(nodes)==0

def expand_nodes(node, problem, heuristic_fn):
    children = []
    for action, new_state in problem.successors(node.state):
        g = node.g+1
        h = heuristic_fn(new_state,problem.goal, problem.size)
        child= make_node(new_state,parent=node, action=action, g=g, h=h)
        children.append(child)
    return children

def queing_nodes(nodes,children):
    for child in children:
        heapq.heappush(nodes,child)
    return nodes


def search_nodes(problem, queuing_fn, heuristic_fn, trace_fn=None):

    h0 = heuristic_fn(problem.start, problem.goal, problem.size)
    initial_node = make_node(problem.start, g=0, h=h0)
    nodes = make_queue(initial_node)

    visited = set()
    nodes_expanded = 0
    max_queue_size = 1

    while True:
        if empty_nodes(nodes):
            return ("failure", nodes_expanded, max_queue_size)
        node = remove_front_node(nodes)
        key = node.key()
        if key in visited:
            continue
        visited.add(key)
        if trace_fn:
            trace_fn(node)
        if problem.is_goal(node.state):
            return (node, nodes_expanded, max_queue_size)
        nodes_expanded += 1
        children = expand_nodes(node, problem, heuristic_fn)
        nodes = queuing_fn(nodes, children)
        if len(nodes) > max_queue_size:
            max_queue_size = len(nodes)
