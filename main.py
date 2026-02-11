from problem import Problm
from search import search_nodes, queing_nodes
from heuristic_search import get_heuristic
from utils import read_puzzle, read_algorithm, print_summary, trace


def main():
    puzzle, size = read_puzzle()

    algo_choice = read_algorithm()
    heuristic_fn, algo_name = get_heuristic(algo_choice)
    print(f"\nSolving with {algo_name}...\n")

    problem = Problm(puzzle, size)
    result, expanded, max_q = search_nodes(
        problem, queing_nodes, heuristic_fn, trace_fn=trace
    )

    print_summary(result, expanded, max_q)


if __name__ == "__main__":
    main()