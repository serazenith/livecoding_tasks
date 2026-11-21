"""Task 8 (Medium): Shortest Path Through a Grid

A rectangular grid contains 0 for open cells and 1 for blocked cells.
Return the minimum number of moves from the top-left to bottom-right cell.
You may move up, down, left, or right through open cells only.
Return -1 if no route exists or either endpoint is blocked.
A one-cell open grid requires zero moves. Do not modify the grid.

Examples:
    [[0, 0, 0], [1, 1, 0], [0, 0, 0]] -> 4
    [[0, 1], [1, 0]] -> -1
    [[0]] -> 0

Constraints: 1 <= rows, columns <= 200; all rows have equal length.
Target: O(rows * columns) time and space.
"""


def shortest_path(grid: list[list[int]]) -> int:...

if __name__ == "__main__":
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    original = [row.copy() for row in grid]
    assert shortest_path(grid) == 4
    assert grid == original
    assert shortest_path([[0, 1], [1, 0]]) == -1
    assert shortest_path([[0]]) == 0
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0, 0, 0, 0]]) == 3
    assert shortest_path([[0, 0], [0, 1]]) == -1
    print("All sample checks passed!")
