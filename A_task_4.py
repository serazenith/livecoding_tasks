"""Task 4 (Easy): Move Zeroes

Modify numbers in place so that all zeroes come last, preserving the
relative order of nonzero values. Return None.

Examples:
    [0, 1, 0, 3, 12] becomes [1, 3, 12, 0, 0]
    [0, 0] stays [0, 0]

Constraints: 0 <= len(numbers) <= 100_000.
Target: O(n) time and O(1) extra space.
"""


def move_zeroes(numbers: list[int]) -> None:
    nonzero_index = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[nonzero_index], numbers[i] = numbers[i], numbers[nonzero_index]
            nonzero_index += 1


if __name__ == "__main__":
    for original, expected in [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0], [0, 0]),
        ([], []),
        ([1, -2, 3], [1, -2, 3]),
        ([0, -1, 0, -2], [-1, -2, 0, 0]),
    ]:
        values = original.copy()
        assert move_zeroes(values) is None
        assert values == expected
    print("All sample checks passed!")
