from pathlib import Path
from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue

_PARENT_FOLDER = Path(__file__).parent.resolve()


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            current_row, current_col = current_cell
            neighbour = (current_row + row_offset,
                         current_col + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                # the weight of each edge is 1
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
    return None


if __name__ == "__main__":
    # # Test 1
    # maze = [[0] * 3 for row in range(3)]
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = a_star(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # # Test 2
    # maze = read_maze(f"{_PARENT_FOLDER}/mazes/mini_maze_bfs.txt")
    # # for row in maze:
    # #     print(row)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = a_star(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # # Test 3
    # maze = read_maze(f"{_PARENT_FOLDER}/mazes/mini_maze_bfs.txt")
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = a_star(maze, start_pos, goal_pos)
    # assert result is None

    # Test 3
    maze = read_maze(f"{_PARENT_FOLDER}/mazes/challenge_maze.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    print(result)
