"""Task 5 (Medium): Merge Intervals

Given inclusive intervals (start, end), merge overlapping intervals.
Return the merged intervals as tuples sorted by start.
Intervals sharing an endpoint overlap; merely adjacent intervals do not.
Do not modify the input list.

Examples:
    [(8, 10), (1, 3), (2, 6), (15, 18)] -> [(1, 6), (8, 10), (15, 18)]
    [(1, 4), (4, 5)] -> [(1, 5)]
    [(1, 2), (3, 4)] -> [(1, 2), (3, 4)]

Constraints: 0 <= len(intervals) <= 100_000; start <= end.
Target: O(n log n) time.
"""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:...

if __name__ == "__main__":
    intervals = [(8, 10), (1, 3), (2, 6), (15, 18)]
    original = intervals.copy()
    assert merge_intervals(intervals) == [(1, 6), (8, 10), (15, 18)]
    assert intervals == original
    assert merge_intervals([(1, 4), (4, 5)]) == [(1, 5)]
    assert merge_intervals([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
    assert merge_intervals([(1, 10), (2, 3), (1, 10)]) == [(1, 10)]
    assert merge_intervals([]) == []
    print("All sample checks passed!")
