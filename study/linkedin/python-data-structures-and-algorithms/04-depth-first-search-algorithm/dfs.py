from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack
import pathlib

_PARENT_PATH = pathlib.Path(__file__).parent.resolve()


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            current_row, current_col = current_cell
            neighbor = (current_row + row_offset,
                        current_col + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze(f"{_PARENT_PATH}/mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze(f"{_PARENT_PATH}/mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
