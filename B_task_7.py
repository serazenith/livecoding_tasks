"""Task 7 (Medium): Count Subarrays With a Target Sum

Return the number of nonempty contiguous subarrays whose sum equals target.
Different start/end positions count separately. Values may be negative.
Do not modify the input list.

Examples:
    numbers=[1, 1, 1], target=2 -> 2
    numbers=[1, -1, 0], target=0 -> 3
    numbers=[0, 0], target=0 -> 3

Constraints: 0 <= len(numbers) <= 100_000.
Target: O(n) time and O(n) extra space.
"""


def count_target_subarrays(numbers: list[int], target: int) -> int:...


if __name__ == "__main__":
    assert count_target_subarrays([1, 1, 1], 2) == 2
    assert count_target_subarrays([1, -1, 0], 0) == 3
    assert count_target_subarrays([0, 0], 0) == 3
    assert count_target_subarrays([], 0) == 0
    assert count_target_subarrays([3], 3) == 1
    assert count_target_subarrays([1, 2, 3], 7) == 0
    print("All sample checks passed!")
